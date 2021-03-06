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
    debug=False

    def setUp(self):
        pass


    def tearDown(self):
        pass
    
    def treeWalk(self,root,parent=None,indent=''):
        if parent is None or (not root==parent):
            if self.debug:
                pprint("%s%s" % (indent,root))
            if hasattr(root,'iter_components') and callable(root.iter_components):
                for subnode in root.iter_components():
                    self.treeWalk(subnode,root,indent+"  ")

    def testXSDParsing(self):
        #crossRefUrl="https://gitlab.com/crossref/schema/-/raw/Conference_ID/schemas/crossref4.5.0.xsd"
        # since 403 forbidden is the result use a workaround
        # git clone --single-branch --branch Conference_ID https://gitlab.com/crossref/schema
        script=os.path.realpath(__file__)
        crossRefUrl=os.path.dirname(script)+"/../schema/schemas/crossref4.5.0.xsd"
        if self.debug:
            print("parsing %s" % crossRefUrl)
        xsd=XSD(crossRefUrl)
        xsdDict=dict(xsd.schema.elements)
        pprint(xsdDict)
        self.assertTrue("conference_name" in xsdDict)
        for schemaElement in sorted(xsdDict):
            self.treeWalk(xsdDict[schemaElement])
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()