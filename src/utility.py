import logging

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
