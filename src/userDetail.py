import re

def getInput(attr): 
        choice = raw_input('Enter your '+attr+': ')
        return choice

def validateEmail(email):
    if re.match(r'[a-zA-Z0-9]+@[a-z]+\.[a-z]+',email):
        return True

def getUserDetail():
    name = getInput('Name')
    print name 
    email = getInput('Email')
    if validateEmail(email) and name != '':
        print "Success"



getUserDetail()