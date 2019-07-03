from src import FileInfo as FileInfo
from src.vars import global_vars as vars
from src.nlp import pdf_data as pdata

input_count = '3'

class Menu():
    def __init__(self):
        self.input_count = str(FileInfo.getFileCount(self,vars.raw_folder))
        #     print vars.processed_folder

    def showMenu(self):
        print ('\t 1. Perform Full Analysis\n')
        print ('\t 2. Perform Partial Analysis\n')
        print ("\tPress 'h' for help and 'q' to quit")
    
    def getInput(self): 
        choice = raw_input('Enter your Choice: ')
        return choice

    def ShowFullAnalysis(self):
        print ('\n')
        print ('\t ====================================================')
        print ('\t ***** Performing Full Analysis on the Raw Data *****')
        print ('\t Total Number of Files    :' + self.input_count)
        print ('\t Estimated Time Duration  :')
        print ('\t ========================================')

    def ShowPartialAnalysis(self):
        print ('\n')
        print ('\t ====================================================')
        print ('\t ***** Performing Partial Analysis on the Raw Data *****')
        print ('\t 1. Abstraction\n')
        print ('\t 2. Conclusion\n')
        print ('\t 3. Results\n')
        print ('\t 4. Search\n')
        print ("\tPress 'h' for help and 'q' to quit")
        print ('\t ========================================')