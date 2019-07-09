#!/usr/bin/python
import os
from src.aws import * 
from src import *
from src import helpInfo,utility

menu = Menu()
mybucket = S3Bucket()
#mybucket.getBuckets()
os.system('clear')
print("\t*****Welcome To NLP based Curation Framework*****\n")

# List the Menu 
menu.showMenu()
input1 = menu.getInput()

if input1 =='q':
    utility.printError('Exit From Frame Work')
    exit()
elif input1 == '1':
    print ('Entered Input '+ input1)
    fullanalys = FullAnalysis()
elif input1 == '2':
    print ('Entered Input '+ input1)
    partanalys = PartialAnalysis()
    input2 = partanalys.getInput()
    partanalys.validateInput(input2)
elif input1 == 'h':
    print ('Entered Input '+ input1)
    print helpInfo.help1
else:
    print ('Please Enter Choice within the range')
    


