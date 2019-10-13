#!/usr/bin/python
import os
from src import *
from src import helpInfo,utility,userDetail,send_mail,PartialAnalysis
from src.project_utility import yaspin_demo as yd

analysis_type = ''
menu = Menu()

def main():
    # Start of Execution
    os.system('clear')
    utility.patternDraw("Please Enter Your Details !!!")
    userdict = userDetail.getUserDetail()
    yd.any_spinner_you_like("Initialising the Framework!!!")
    os.system('clear')
    utility.patternDraw("Welcome To NLP based Curation Framework")
    utility.initialIOCheck()
    mainMenu(userdict)

def mainMenu(userdict):
    # List the Menu 
    menu.showMenu()
    input1 = menu.getInput()
    utility.printInfo('Entered Input - '+ input1)

    if input1 =='q':
        utility.printError('Exit From Frame Work')
        exit()
    elif input1 == '1':
        analysis_type = {}
        fullanalys = FullAnalysis()
        analysis_type = fullanalys.performFullAnalysis()
        if(userdict['email_option'] == 'Y'):
            sendmail(userdict,analysis_type)
    elif input1 == '2':
        analysis_type = PartialAnalysis.getInput()
        if(userdict['email_option'] == 'Y'):
            sendmail(userdict,analysis_type)
    elif input1 == 'h':
        utility.printInfo(helpInfo.menu1)
        mainMenu(userdict)
    else:
        utility.printInfo('Please Enter Choice within the given range\n')
        mainMenu(userdict)

def sendmail(userdict,analysis_type):
    send_mail.send_Email(analysis_type['keyword'],userdict['userName'],userdict['userEmail'],analysis_type['file_status'])

if __name__ == "__main__":
    main()

