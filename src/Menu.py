from src import FileInfo as FileInfo
from src.vars import global_vars as vars
from src.nlp import pdf_data as pdata
from src import utility

input_count = ''

class Menu():
    def __init__(self):
        self.input_count = str(FileInfo.getFileCount(self,vars.raw_folder))

    def showMenu(self):
        print ('\t 1. Perform Full Analysis\n')
        print ('\t 2. Perform Partial Analysis\n')
        print ("\tPress 'h' for help and 'q' to quit\n")
    
    def getInput(self): 
        choice = raw_input('Enter your Choice: ')
        return choice

    def ShowFullAnalysis(self):
        print ('===========================================================')
        print('\t ***** Performing Full Analysis on the Raw Data *****\n')
        utility.printLog (' Total Number of Files    : ' + self.input_count)
        # utility.printLog (' Estimated Time Duration  :')

    def ShowPartialAnalysis(self):
        print ('\n')
        print ('\t ====================================================')
        print ('\t ***** Performing Partial Analysis on the Raw Data *****')
        print ('\t 1. Abstraction\n')
        print ('\t 2. Methods\n')
        print ('\t 3. Conclusions\n')
        print ('\t 4. Results\n')
        print ("\tPress 'h' for help and 'q' to quit")
        print ('\t ====================================================')