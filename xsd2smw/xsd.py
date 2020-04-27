'''
Created on 16.04.2020

@author: wf
'''
import xmlschema

class XSD(object):
    '''
    XSD Parsing wrapper
    see https://stackoverflow.com/questions/54687837/parse-an-xsd-file-using-python
    '''
    
    def __init__(self, url):
        '''
        Constructor
        '''
        self.url=url
        self.schema=xmlschema.XMLSchema11(self.url)
        