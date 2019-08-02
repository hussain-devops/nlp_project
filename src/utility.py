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
    print "\n"

def getFileName(path):
    for file in os.listdir(path):
        if file.endswith(".txt"):
            return path+file