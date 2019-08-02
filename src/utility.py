import logging,os,glob,fcntl, termios, struct
from src.vars import global_vars as vars


logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',datefmt='%d-%b-%y %H:%M:%S',level=logging.INFO)
def printLog(msg):
    logging.info(msg)

def printError(msg):
    logging.error(msg)

def printInfo(msg):
    print "\n"+msg+"\n"

def initialIOCheck():
    if not os.listdir(vars.raw_folder):
        printError('Input Directory is empty' + + vars.raw_folder)
        exit()
    
    files = glob.glob(vars.processed_folder+"*")
    for f in files:
        os.remove(f)

def terminal_size():
    th, tw, hp, wp = struct.unpack('HHHH',
        fcntl.ioctl(0, termios.TIOCGWINSZ,
        struct.pack('HHHH', 0, 0, 0, 0)))
    return tw


def patternDraw(msg):
    text = msg.splitlines()
    width = terminal_size()/2

    maxlen = max(width for s in text)
    colwidth = maxlen + 2

    print '+' + '-'*colwidth + '+'
    for s in text:
        print '| %-*.*s |' % (maxlen, maxlen, s)
    print '+' + '-'*colwidth + '+'




# def userDetail():
#     dict = {}
#     username = getInput('EnterYour Name: ')
#     dict['userName'] = username
#     useremail = getInput('Enter Your Email: ')
#     dict['userEmail'] = useremail
#     print dict


# printError('testing')

# logging.debug('This is a debug message')
# logging.info('This is an info message')
# logging.warning('This is a warning message')
# logging.error('This is an error message')
# logging.critical('This is a critical message')
