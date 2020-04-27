'''
Created on 16.04.2020

@author: wf
'''
import unittest
from xsd2smw.xsd import XSD
from pprint import pprint

class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testXSDParsing(self):
        crossRefUrl="https://gitlab.com/crossref/schema/-/raw/Conference_ID/schemas/crossref4.5.0.xsd"
        # since 403 forbidden is the result use a workaround
        # git clone --single-branch --branch Conference_ID https://gitlab.com/crossref/schema
        crossRefUrl="/Users/wf/Projekte/2020/ConfIDent/crossref/schema/schemas/crossref4.5.0.xsd"
        xsd=XSD(crossRefUrl)
        pprint(dict(xsd.schema.elements))
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()