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


    def testCreateSheet(self):
        '''testing the creation of a Google spreadsheet'''
        if not getpass.getuser()=="travis":
            gc = gspread.oauth()
            sh = gc.create('A new spreadsheet')
            sh.share('philip.streoemert@tib.eu', perm_type='user', role='writer')
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()