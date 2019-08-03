from src import *
from src import utility
from src.analysis import Full_Analysis as fa

menu = Menu()

class FullAnalysis(object):
    def __init__(self, *args):
        utility.printLog('You are inside Full Analysis Class')
        menu.ShowFullAnalysis()

