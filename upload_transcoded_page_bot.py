import itertools
import sqlite3
import pywikibot

from pywikibot.bot import SingleSiteBot
from pywikibot.proofreadpage import IndexPage, ProofreadPage

class UploadTranscodedPageBot(SingleSiteBot):
    
    def __init__(self, generator, **kwargs):
        super(UploadTranscodedPageBot, self).__init__(**kwargs)
        self.generator = generator


    def treat(self, page):
        """Process one ProofreadPage page.

        @param page: page to be treated.
        @type page: ProofreadPage
        @raises: pywikibot.Error
        """
        print("processing page %s" % page.title())
        if not isinstance(page, ProofreadPage):
            raise pywikibot.Error('Page %s must be a ProofreadPage object.'
                                  % page)

        if page.exists():
            print("page exists" )
            # return

        # page.get()
        print("page status is %s " % page.status)
        page.header = u"{{rh|2|''THE POPULAR SCIENCE MONTHLY.''}}"
        page.footer = u'\n{{smallrefs}}'
        # page.text = " bot experiment"
        # page.save()
        #sql = "SELECT transcode from table WHERE page = %s ORDER BY seq" % pagenum
        #conn = sqlite3.connect('example.db')
        #c = conn.cursor()

        #text  = ""
        #for data in c.execute(sql):
        #    text = text + data['transcode']
        #    return text

        page.body  = """{{c|{{x-larger|A BID FOR FORTUNE.}}}}


{{rule|5em}}


{{c|{{larger|PROLOGUE.}}

{{smaller|DR. NIKOLA.}}}}

{{sc|The}} manager"""
        # page.save()
        
        # self.userPut(page, page.text, text, summary="from UploadTranscodePageBot")
