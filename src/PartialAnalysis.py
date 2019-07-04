from src import *
from src import helpInfo,utility
from src.analysis import PartAnalysis
from src.vars import global_vars as vars

menu = Menu()

class PartialAnalysis():
    input2=''
    def getInput(self):
        print ('You are inside Partial Analysis class')
        menu.ShowPartialAnalysis()
        self.input2 = menu.getInput()
        return self.input2

    def validateInput(self,input2):
        path = vars.raw_folder + 'iPSC_OCRL_MolAut.pdf' # needs to be modified
        if self.input2 == 'q':
            utility.printError('Exit From Frame Work')
            exit()
        elif self.input2 == '1': 
            # print ('Entered Input '+ self.input2)
            utility.printLog(self.input2)
            PartAnalysis.perfomPartAnalysis(path,'abstract')
        elif self.input2 == '2':
            # print ('Entered Input '+ self.input2)
            PartAnalysis.perfomPartAnalysis(path,'conclusions')
        elif self.input2 == '3':
            # print ('Entered Input '+ self.input2)
            PartAnalysis.perfomPartAnalysis(path,'results')
        elif self.input2 == '4':
            print ('Entered Input '+ self.input2)
        elif self.input2 == 'h':
            print ('Entered Input '+ self.input2)
            print helpInfo.help2
        else:
            print ('Please Enter Choice within the range')
