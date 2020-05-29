'''
Created on 25.05.2020

@author: StroemertP
'''
import unittest
import gspread
import getpass


class TestGspread(unittest.TestCase):
    '''Testing the export of SMW data into a Google Spreadsheet.
    Google APIs "Drive" & "Sheets" must be activated, see: 
    https://gspread.readthedocs.io/en/latest/oauth2.html#enable-api-access-for-a-project'''

    def createGSheet(self, spreadsheetName='My Spreadsheet', email='philip.stroemert@tib.eu'):
        # log into Google API
        gc = gspread.oauth()
        # create new spreadsheet
        sh = gc.create(spreadsheetName)
        # share spreadsheet, so it is accessible
        sh.share(email, perm_type='user', role='writer')
        return sh
    
    def openGSheet(self, spreadsheetName=None):
        # log into Google API
        gc = gspread.oauth()
        # try to open existing spreadsheet
        if spreadsheetName != None:
            try:
                result = gc.open(spreadsheetName)
                return result
            except gspread.exceptions.SpreadsheetNotFound:
                print(f'ERROR: There is no spreadsheet named "{spreadsheetName}"\n')
                pass
         
       
    def testCreateSheet(self):
        '''testing the creation of a Google spreadsheet'''
        if not getpass.getuser()=="travis":
            sh = self.createGSheet(spreadsheetName='ConfIDent Metadata Schema')
            sh = self.openGSheet(spreadsheetName='aaarrrggg')
            if sh != None:
                # Select worksheet by index. Worksheet indexes start from zero
                wks = sh.get_worksheet(0)
                # Update a range of cells using the top left corner address
                wks.update('A1', [['name','definition', 'cardinality' ], ['Event Name', 'The official title or name of the academic event, including Number if present','1-n']])
                
                # Format the header
                wks.format('A1:C1', {'textFormat': {'bold': True}})
                # Select worksheet by index. Worksheet indexes start from zero
            
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()