#!/usr/bin/python
import os
from goto import with_goto
from src import *
from src import helpInfo,utility,userDetail,send_mail,PartialAnalysis
from src.project_utility import yaspin_demo as yd

analysis_type = ''
menu = Menu()
window_size = utility.terminal_size()
window_half = window_size/2
window_quater = window_half/2

@with_goto
def main():


    os.system('clear')
    # print "*" * window_half
    size = window_quater - 10
    # print(" " * size + "Please Enter Your Details !!!\n")
    utility.patternDraw("Please Enter Your Details !!!")
    userdict = userDetail.getUserDetail()
    yd.any_spinner_you_like("Initialising the Framework!!!")
    os.system('clear')
    # size = window_quater - 20
    # print("*" * window_half)
    # print(" " * size +"Welcome To NLP based Curation Framework\n")
    utility.patternDraw("Welcome To NLP based Curation Framework")
    utility.initialIOCheck()
    mainMenu(userdict)
    # sendmail(userdict,sendEmail)

def mainMenu(userdict):
    # List the Menu 
    menu.showMenu()
    input1 = menu.getInput()
    utility.printInfo('Entered Input '+ input1)

    if input1 =='q':
        utility.printError('Exit From Frame Work')
        exit()
    elif input1 == '1':
        fullanalys = FullAnalysis()
        analysis_type = 'full_analysis'
        sendmail(userdict,analysis_type)
    elif input1 == '2':
        # partanalys = PartialAnalysis()
        analysis_type = PartialAnalysis.getInput()
        # analysis_type = partanalys.validateInput(input2)
        # analysis_type = 'partial_analysis'
        # sendmail(userdict,analysis_type)
    elif input1 == 'h':
        utility.printInfo(helpInfo.menu1)
        mainMenu(userdict)
    else:
        utility.printInfo('Please Enter Choice within the given range\n')
        mainMenu(userdict)

def sendmail(userdict,analysis_type):
    send_mail.send_Email(analysis_type,userdict['userName'],userdict['userEmail'])


if __name__ == "__main__":
    main()

