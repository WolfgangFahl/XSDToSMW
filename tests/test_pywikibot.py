import unittest
from wikibot.wikibot import WikiBot
import pywikibot

class TestWikiAccess(unittest.TestCase):
    def test_rq(self):
        wikibot=WikiBot.ofWikiId("rq")
        site = wikibot.site
        page = pywikibot.Page(site, u"WikiCFP")
        text = page.text


        #self.assertEqual(True, False)
        self.assertTrue('Nonprofit' in text)

if __name__ == '__main__':
    unittest.main()
