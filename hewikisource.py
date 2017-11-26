import itertools
import sqlite3
import pywikibot

from pywikibot.bot import SingleSiteBot
from pywikibot.proofreadpage import IndexPage, ProofreadPage
# import UploadTranscodedPageBot
import  upload_transcoded_page_bot as ubot # import UploadTranscodedPageBot

def main():
    site = pywikibot.Site('en','wikisource')
    
    # filename = "מפתח:ספר_השרשים.pdf"
    # filename = "Index:ספר_השרשים.pdf"
    filename = "Index:Catholic_Encyclopedia,_volume_17.djvu"
    index = IndexPage(site,filename)

    #sql = "SELECT DISTINCT page table WHERE page = %s ORDER BY page"     
    #conn = sqlite3.connect('example.db')
    #c = conn.cursor()

    gen_list = []
    #for p in c.execute(sql):
    for p in range(6,7):
        #todo - what is content parameter ? and what should we put in filter_ql ?
        #TODO - here I get exception qualityN prp-pagequality-N" or class="new"

        # I added a patch proffread.patch to fix it
        gen = index.page_gen(start=p, end=p,
                             filter_ql= None, content=False)
        gen_list.append(gen)

    gen = itertools.chain(*gen_list)

    pywikibot.output('\nUploading text to %s\n' % index.title(asLink=True))

    bot = ubot.UploadTranscodedPageBot(gen, site=index.site)
    bot.run()

if __name__ == '__main__':
    try:
        main()
    except Exception:
        pywikibot.error('Fatal error:', exc_info=True)

    
    
