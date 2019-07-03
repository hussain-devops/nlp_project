import os;

def getFileCount(self,path):
    length = len([name for name in os.listdir(path) if os.path.isfile(os.path.join(path, name))])
    return length

    