import re,utility

def getInput(attr): 
        choice = raw_input('\tEnter your '+attr+': ')
        return choice

def validateEmail(email):
    if re.match(r'[a-zA-Z0-9\.]+@[a-z]{3,6}\.[a-z]{2,3}',email):
        return True

def getUserDetail():
    dict={}
    username = getInput('Name')
    useremail = getInput('Email')
    if validateEmail(useremail) and username != '':
        dict['userName'] = username 
        dict['userEmail'] = useremail
        return dict
    else:
        utility.printError("Please enter valid user data!!!")
        exit()


# getUserDetail()