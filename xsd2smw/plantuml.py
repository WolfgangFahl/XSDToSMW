'''
Created on 01.06.2020

@author: wf
'''

class PlantUML(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
    def fixName(self,name):
        name=name.replace(" ","_")
        return name
            
    def genClasses(self,result):
        for elementKey in result.keys():
            element=result[elementKey]
            #print(element)
            if element["kind"]=='Entity':
                template="""
  note top of %s: %s
  class %s {
"""
                classname=self.fixName(element["name"])
                comment=element["comment"]
                if not comment: comment=""
                print (template % (classname,comment,classname))
                self.genAttributes(elementKey)
                print ("  }")
                
    def prepareAttributes(self,result): 
        self.classMap={}           
        for elementKey in result.keys():
            element=result[elementKey]
            if element["kind"]=='Entity':
                self.classMap[elementKey]={}
        for elementKey in result.keys():
            element=result[elementKey]
            if element["kind"]=='Property':
                parent=element["parent"]
                if parent in self.classMap:
                    self.classMap[parent][elementKey]=element
                else:
                    print ("Warning parent %s is not defined" % parent)    
                #print("%s->%s" % (elementKey,element["parent"]))
        
    def genAttributes(self,classKey):
        attributes=self.classMap[classKey]
        for attrKey in attributes:
            element=attributes[attrKey]
            attrName=self.fixName(element["name"])
            print("   %s" % (attrName))
            
    def generate(self,result):
        self.prepareAttributes(result)
        self.intro()
        self.genClasses(result)
        self.outro()
        
    def intro(self):    
        template="""
<uml>
  hide circle"""                
        print (template % ())       
        
    def outro(self):
        print ("</uml>")