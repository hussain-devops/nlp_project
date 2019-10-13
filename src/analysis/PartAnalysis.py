import os,subprocess,re,nltk,shutil,textstat,textract
from gensim.summarization import summarize
from src import utility


def pdf_textract(filepath):
    text = textract.process(filepath)
    re.sub(r'[^\x00-\x7F]+',' ', text)
    # text = str.replace("!@#$%^&*()[]{};:,./<>?\|`~-=_+", " ")
    return text

def patternCheck(keytext,data):
    if keytext == 'abstract':
        keytext = r"^\d*\.*\s*(Abstract|A B S T R A C T|ABSTRACT|Purpose|PURPOSE|A([b|B|\s][s|S|B][t|T|\s][a-zA-Z\s]*))"

    if keytext == 'results':
        keytext = r"^\d*\.*\s*R([e|E|\s][s|S|\s][u|U|\s][l|L|\s][t|T|\s][s|S|\s])"

    if keytext == 'conclusions':
        keytext = r"^\d*\.*\s*C([o|O][n|N|\s][c|C|\s][l|L|\s][u|U|\s][s|S|\s][i|I|\s][o|O|\s][n|N|\s][s|S|\s])"

    if keytext == 'methods':
        keytext = r"^\d*\.*\s*M([ethods|aterials])"

    if re.search(keytext,data):
        return True

def cutPara(data,feature):
    fo = open("test.txt", "wb")
    fo.write(data)
    fo.close()
    fo = open("test.txt", "rb")
    extract = 'false'
    para = ''
    lines = fo.readlines()
    index = 0
    # Extract para from Keyword to empty line
    for line in lines:
        # line = re.sub(r'^[\x00-\x7F\|]+',' ', line)
        if patternCheck(feature,line):
            extract = 'true'
            if lines[index+1] == '\n':
                lines[index+1] = ''
            if lines[index+3] == '\n':
                lines[index+3] = ''
        if line == '\n':
            extract = 'false'
        if extract == 'true':
            para = para + line
        index = index + 1
    fo.close()
    os.remove("test.txt")
    return para

def getPartialData(filepath,keyinput):
    data = pdf_textract(filepath)
    partialData = cutPara(data,keyinput).replace('\n',' ')
    utility.printLog("Sentence Stat: "+str(textstat.sentence_count(partialData)))
    if textstat.sentence_count(partialData) > 3:
        partialData = summarize(partialData, ratio=0.3)
    return partialData

def getAllFilesToText(inputpath,keyinput): 
    fileObj = open(keyinput+".txt", "wb")
    file_status = []
    for filename in os.listdir(inputpath):
        filepath = ''
        if filename.endswith(".pdf"):
            filepath = inputpath + filename
            partialData = getPartialData(filepath,keyinput)
            file_dict = {'name': filename,'status':'SUCCESS'}
            if partialData == '':
                file_dict['status'] = 'FAILURE'
                file_status.append(file_dict)
                continue
            file_status.append(file_dict)
            fileObj.write("File Name : \t"+filename+"\n")
            fileObj.write("-----------------------------------------------------------\n")
            fileObj.write(partialData+"\n")
            fileObj.write("-----------------------------------------------------------\n")
    utility.printLog("Empty File LIST " + str(file_status))
    utility.printLog("Moving the Output to Processed Folder")
    shutil.move(keyinput+".txt","data/processed/"+keyinput+".txt")
    return file_status

def perfomPartAnalysis(path,keyinput):
    utility.printLog('Performing Partial Analysis : '+keyinput)
    file_status = getAllFilesToText(path,keyinput)
    return file_status


# path = '/home/hussain/ML/project/nlp_project/data/raw/'
# # data = pdf_textract(path)
# getAllFilesToText(path,'abstract')