#!/usr/bin/python
import os
from src import *
from src import helpInfo,utility,userDetail,send_mail
from src.project_utility import yaspin_demo as yd

def main():

    analysis_type = ''
    menu = Menu()
    os.system('clear')
    print("\t*****Please Enter Your Details*****\n")
    userdict = userDetail.getUserDetail()
    yd.any_spinner_you_like("Initialising the Framework!!!")
    os.system('clear')
    print("\t*****Welcome To NLP based Curation Framework*****\n")
    # utility.initialIOCheck()
    
    
    # List the Menu 
    menu.showMenu()
    input1 = menu.getInput()

    if input1 =='q':
        utility.printError('Exit From Frame Work')
        exit()
    elif input1 == '1':
        print ('Entered Input '+ input1)
        fullanalys = FullAnalysis()
        analysis_type = 'full_analysis'
    elif input1 == '2':
        print ('Entered Input '+ input1)
        partanalys = PartialAnalysis()
        input2 = partanalys.getInput()
        partanalys.validateInput(input2)
        analysis_type = 'partial_analysis'
    elif input1 == 'h':
        print ('Entered Input '+ input1)
        print helpInfo.menu1
    else:
        print ('Please Enter Choice within the range')

    send_mail.sendEmail(analysis_type,userdict['userName'],userdict['userEmail'])

if __name__ == "__main__":
    main()

