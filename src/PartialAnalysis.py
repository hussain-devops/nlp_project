from src import *
from src import helpInfo,utility
from src.analysis import PartAnalysis
from src.vars import global_vars as vars

menu = Menu()

input2=''
def getInput():
    print ('You are inside Partial Analysis class')
    menu.ShowPartialAnalysis()
    input2 = menu.getInput()
    keyword = validateInput(input2)
    return keyword

def validateInput(input2):
        # path = vars.raw_folder + 'iPSC_OCRL_MolAut.pdf' # needs to be modified by taking out the pdf file
    if input2 == 'q':
        utility.printError('Exit From Frame Work')
        exit()
    elif input2 == '1': 
            # print ('Entered Input '+ self.input2)
        keyword = 'abstract'
        PartAnalysis.perfomPartAnalysis(vars.raw_folder,'abstract')
        return keyword
    elif input2 == '2':
        keyword = 'methods'
        PartAnalysis.perfomPartAnalysis(vars.raw_folder,'methods')
        return keyword
    elif input2 == '3':
        keyword = 'conclusions'
        PartAnalysis.perfomPartAnalysis(vars.raw_folder,'conclusions')
        return keyword
    elif input2 == '4':
        keyword = 'results'
        PartAnalysis.perfomPartAnalysis(vars.raw_folder,'results')
        return keyword
    elif input2 == 'h':
        print helpInfo.menu2
        getInput()
    else:
        print ('Please Enter Choice within the range')
        getInput()
