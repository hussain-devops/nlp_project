#!/usr/bin/python

from src import *

menu = Menu()

class FullAnalysis(object):
    def __init__(self, *args):
        print('You are inside Full Analysis Class')
        menu.ShowFullAnalysis()