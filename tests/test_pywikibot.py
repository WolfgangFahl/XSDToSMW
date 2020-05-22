import unittest
from wikibot.wikibot import WikiBot
import pywikibot
import getpass

class TestWikiAccess(unittest.TestCase):
    ''' Test Accessing MediaWiki viy pyWikibot API'''
    
    def test_rq(self):
        ''' test accessing wiki with id "rq" using encrypted credentials'''
        # can not test this on travis
        if not getpass.getuser()=="travis":                 
            wikibot=WikiBot.ofWikiId("rq")
            site = wikibot.site
            page = pywikibot.Page(site, u"WikiCFP")
            text = page.text

            #self.assertEqual(True, False)
            self.assertTrue('Nonprofit' in text)

if __name__ == '__main__':
    unittest.main()
