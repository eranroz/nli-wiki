import json
import http.client

identifies = ['FL7070748','FL7071077']
scheme = "http"
server = "iiif.nli.org.il"
prefix = "IIIFv21"
def main():
    conn = http.client.HTTPConnection(server)
    for id in identifies:
        conn.request("GET","/"+prefix+"/"+id+"/info.json")
        response = conn.getresponse()
        if response.status != 200:
            print("response to %s was: %d - continue to next" % (id,response.status))
        else:
            datastore = json.loads(response.read().decode("utf-8"))
            w = datastore['width']
            h = datastore['height']
            print("width = %d, height = %d" % (w,h))
    
if __name__ == '__main__':
    main()
    
    
