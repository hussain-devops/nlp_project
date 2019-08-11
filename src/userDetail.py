import re,utility

def getInput(attr): 
        choice = raw_input(attr)
        return choice

def validateEmail(email):
    if re.match(r'[a-zA-Z0-9\.]+@[a-z]{3,6}\.[a-z]{2,3}',email):
        return True

def getUserDetail():
    dict={}
    username = getInput('Enter your Name : ')
    useremail = getInput('Enter your Email : ')
    email_option = getInput('Do you want the output in email? (Y/N) : ')
    if validateEmail(useremail) and username != '' and re.match(r'(Y|N)',email_option):
        dict['userName'] = username 
        dict['userEmail'] = useremail
        dict['email_option'] = email_option
        return dict
    else:
        utility.printError("Please enter valid user data!!!")
        exit()
