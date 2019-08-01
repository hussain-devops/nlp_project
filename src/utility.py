import logging,os
from src.vars import global_vars as vars

# logging.getLogger('example_logger')
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',datefmt='%d-%b-%y %H:%M:%S',level=logging.INFO)
def printLog(msg):
    logging.info(msg)

def printError(msg):
    logging.error(msg)


# printError('testing')

# logging.debug('This is a debug message')
# logging.info('This is an info message')
# logging.warning('This is a warning message')
# logging.error('This is an error message')
# logging.critical('This is a critical message')

def initialIOCheck():
    if not os.listdir(vars.raw_folder):
        printError('Input Directory is empty' + + vars.raw_folder)
        exit()
    else:
        printLog("Directory is not empty" + vars.raw_folder)




# def userDetail():
#     dict = {}
#     username = getInput('EnterYour Name: ')
#     dict['userName'] = username
#     useremail = getInput('Enter Your Email: ')
#     dict['userEmail'] = useremail
#     print dict