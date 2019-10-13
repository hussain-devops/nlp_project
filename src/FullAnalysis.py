from src import *
from src import utility
from src.analysis import Full_Analysis as fa
from src.vars import global_vars as vars

menu = Menu()
status = {}

class FullAnalysis(object):
    def __init__(self, *args):
        utility.printLog('You are inside Full Analysis Class')
        menu.ShowFullAnalysis()

    def performFullAnalysis(self):
        status['keyword'] = 'full_analysis'
        status['file_status'] = fa.getAllFilesToText(vars.raw_folder,'full_analysis')   
        return status     

