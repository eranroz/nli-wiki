import itertools
import sqlite3
import pywikibot

from pywikibot.bot import SingleSiteBot
from pywikibot.proofreadpage import IndexPage, ProofreadPage


def main:
    site = pywikibot.Site('he','wikisource')
    
    filename = "ספר השרשים.pdf"
    index = IndexPage(site,filename)

    sql = "SELECT DISTINCT page table WHERE page = %s ORDER BY page" 

    
    conn = sqlite3.connect('example.db')
    c = conn.cursor()

    gen_list = []
    for p in c.execute(sql):
        #todo - what is content parameter ? and what should we put in filter_ql ?
        gen = index.page_gen(start=start, end=end,
                             filter_ql=[0,1,2,3,4], content=False)
        gen_list.append(gen)

    gen = itertools.chain(*gen_list)

    pywikibot.output('\nUploading text to %s\n' % index.title(asLink=True))

    bot = UploadTranscodedPageBot(gen, site=index.site)
    bot.run()

if __name__ == '__main__':
    try:
        main()
    except Exception:
        pywikibot.error('Fatal error:', exc_info=True)

    
    
