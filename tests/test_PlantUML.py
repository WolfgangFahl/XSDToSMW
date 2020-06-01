'''
Created on 01.06.2020

@author: wf
'''
import unittest
from wikibot.wikibot import WikiBot
from xsd2smw.plantuml import PlantUML
from wikibot.smw import SMW
import getpass

class TestPlantUML(unittest.TestCase):
    debug=True

    def testPlantUML(self):
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
            if TestPlantUML.debug:
                print(result)
            pu=PlantUML()
            pu.generate(result)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()