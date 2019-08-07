from src import *
from src import utility
from src.analysis import Full_Analysis as fa
from src.vars import global_vars as vars

menu = Menu()

class FullAnalysis(object):
    def __init__(self, *args):
        utility.printLog('You are inside Full Analysis Class')
        menu.ShowFullAnalysis()

    def performFullAnalysis(self,analysis_type):
        fa.getAllFilesToText(vars.raw_folder,analysis_type)        

