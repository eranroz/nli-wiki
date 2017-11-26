import json
import http.client

import sys
from PIL import Image
import urllib.request

from pathlib import Path

identifies = ['FL7070748','FL7071077']
scheme = "http"
server = "iiif.nli.org.il"
prefix = "IIIFv21"
def main():

    for id in identifies:
        image_file = Path("%s.jpg" % id)
        if image_file.is_file():
            print("%s.jpg already exist" % id)
            continue
        conn = http.client.HTTPConnection(server)
        conn.request("GET","/"+prefix+"/"+id+"/info.json")
        response = conn.getresponse()
        if response.status != 200:
            print("response to %s was: %d - continue to next" % (id,response.status))
        else:
            datastore = json.loads(response.read().decode("utf-8"))
            conn.close()
            print(datastore)
            w = datastore['width']
            h = datastore['height']

            maxw = datastore['profile'][1]['maxWidth']
            maxh = datastore['profile'][1]['maxHeight']
            
            print("width = %d, height = %d" % (w,h))
            print("maxw = %d, maxh = %d" % (maxw,maxh))
            
            restore_image = Image.new('RGB',(w,h))
            wi = hi = 0
            while hi < h:
                tmph = 0;
                while wi < w:
                    print("%d %d" % (hi,wi))
                    # conn.request("GET","/"+prefix+"/"+id+"/%d,%d,%d,%d/full/0/default.jpg" % (wi,hi,maxw,maxh))
                    url = scheme+"://"+server+"/"+prefix+"/"+id+"/%d,%d,%d,%d/full/0/default.jpg" % (wi,hi,maxw,maxh)
                    # reg_response = conn.getresponse()
                    #if reg_response.status != 200:
                    #    print("response for id %s in region %d,%d,%d,%d is %d" % (id,wi,hi,maxw,maxh,reg_response.status))
                    #else:
                    im = Image.open(urllib.request.urlopen(url))
                    restore_image.paste(im,(wi,hi))
                    # (wi,hi) = tuple(map(sum,zip(im.size,(wi,hi))))
                    tmpw,tmph = im.size
                    if wi == 0:
                        im.save("%s_%d_%d_%d_%d.jpg" % (id,wi,hi,tmpw,tmph)

                    print("tmph = %d " % (tmph))
                    wi = wi + tmpw
                hi = hi + tmph
                wi = 0
                    
            restore_image.save("%s.jpg" % id)
    
if __name__ == '__main__':
    main()
    
    
