from src import *
from src import helpInfo,utility
from src.analysis import PartAnalysis
from src.vars import global_vars as vars

menu = Menu()
status ={}
input2=''
def getInput():
    print ('You are inside Partial Analysis class')
    menu.ShowPartialAnalysis()
    input2 = menu.getInput()
    keyword = validateInput(input2)
    return keyword

def validateInput(input2):
    if input2 == 'q':
        utility.printError('Exit From Frame Work')
        exit()
    elif input2 == '1': 
        status['keyword'] = 'abstract'
        status['file_status'] = PartAnalysis.perfomPartAnalysis(vars.raw_folder,'abstract')
        return status
    elif input2 == '2':
        status['keyword'] = 'methods'
        status['file_status'] = PartAnalysis.perfomPartAnalysis(vars.raw_folder,'methods')
        return status
    elif input2 == '3':
        status['keyword'] = 'conclusions'
        status['file_status'] = PartAnalysis.perfomPartAnalysis(vars.raw_folder,'conclusions')
        return status
    elif input2 == '4':
        status['keyword'] = 'results'
        status['file_status'] = PartAnalysis.perfomPartAnalysis(vars.raw_folder,'results')
        return status
    elif input2 == 'h':
        print helpInfo.menu2
        getInput()
    else:
        print ('Please Enter Choice within the range')
        getInput()
