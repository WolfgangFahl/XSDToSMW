import unittest
from wikibot.wikibot import WikiBot
from wikibot.smw import SMW
import pywikibot
import getpass

class TestWikiAccess(unittest.TestCase):
    ''' Test Accessing MediaWiki via pyWikibot API'''
    debug=True
    
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
            
    def test_ask(self):
        """ test using the SMW ask API """
        if not getpass.getuser()=="travis":                 
            wikibot=WikiBot.ofWikiId("rq")
            smw=SMW(wikibot.site) 
            ask="""{{#ask: [[Concept:SchemaProperty]][[SchemaProperty schema::ConfIDentSchema]]
|mainlabel=SchemaProperty
| ?SchemaProperty parent = parent
| ?SchemaProperty cardinality = cardinality
| ?SchemaProperty kind = kind
| ?SchemaProperty definition = definition
| ?SchemaProperty comment = comment 
| ?SchemaProperty allowedValue = allowedValue
| ?SchemaProperty examples = examples
| ?SchemaProperty name = name
| ?SchemaProperty type = type
| ?SchemaProperty mapsTo = mapsTo
| ?SchemaProperty id = id
| ?SchemaProperty schema = schema
|sort=SchemaProperty kind,SchemaProperty name
|order=ascending,ascending
| limit=200 
}}"""
        result=smw.query(ask)
        if TestWikiAccess.debug:
            print(result)

if __name__ == '__main__':
    unittest.main()
