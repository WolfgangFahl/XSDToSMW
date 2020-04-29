'''
Created on 2020-04-16

@author: wf
'''
import unittest
import os
from xsd2smw.xsd import XSD
from pprint import pprint

class TestXSD2SMW(unittest.TestCase):
    """ unit test for XSD schema to Semantic MediaWiki import
    """
    debug=True

    def setUp(self):
        pass


    def tearDown(self):
        pass

    def testXSDParsing(self):
        #crossRefUrl="https://gitlab.com/crossref/schema/-/raw/Conference_ID/schemas/crossref4.5.0.xsd"
        # since 403 forbidden is the result use a workaround
        # git clone --single-branch --branch Conference_ID https://gitlab.com/crossref/schema
        script=os.path.realpath(__file__)
        crossRefUrl=os.path.dirname(script)+"/../schema/schemas/crossref4.5.0.xsd"
        if TestXSD2SMW.debug:
            print("parsing %s" % crossRefUrl)
        xsd=XSD(crossRefUrl)
        pprint(dict(xsd.schema.elements))
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()