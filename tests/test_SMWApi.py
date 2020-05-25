'''
Created on 25.05.2020

@author: wf
'''
import unittest
import getpass
from wikibot.wikibot import WikiBot
from pywikibot.data.api import APIGenerator


class Test(unittest.TestCase):


    def testSMWApi(self):
        if not getpass.getuser()=="travis":                 
            wikibot=WikiBot.ofWikiId("rq")
            site = wikibot.site
            api=APIGenerator("ask",query="[[Topic name::Fixme]]",site=site)
            #for item in api:
            #    print (item)
            
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testSMWApi']
    unittest.main()