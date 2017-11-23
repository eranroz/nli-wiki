import itertools
import sqlite3
import pywikibot

from pywikibot.bot import SingleSiteBot
from pywikibot.proofreadpage import IndexPage, ProofreadPage

class UploadTextBot(SingleSiteBot):
    
"""
A bot that uploads text-layer to Page:namespace.
Works only on sites with Proofread Page extension installed.
"""

    def __init__(self, generator, **kwargs):
        super(UploadTextBot, self).__init__(**kwargs)
        self.generator = generator


    def treat(self, page):
        """Process one ProofreadPage page.

        @param page: page to be treated.
        @type page: ProofreadPage
        @raises: pywikibot.Error
        """
        if not isinstance(page, ProofreadPage):
            raise pywikibot.Error('Page %s must be a ProofreadPage object.'
                                  % page)

        if page.exists():
            return


        sql = "SELECT transcode from table WHERE page = %s ORDER BY seq" % pagenum

        conn = sqlite3.connect('example.db')
        c = conn.cursor()

        text  = ""
        for data in c.execute(sql):
            text = text + data['transcode']
            return text

        self.userPut(page, old_text, text, summary="from UploadTranscodePageBot")
