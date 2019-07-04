import os,subprocess,re,nltk
from textwrap import wrap
from gensim.summarization import summarize
# from src.vars import global_vars as vars
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import BytesIO
from src import utility

# hichri
# iPSC_OCRL_MolAut
# splicing_analysis_genes-09-00015

path = '/home/hussain/ML/project/nlp_project/data/raw/iPSC_OCRL_MolAut.pdf'
outputpath = '/home/hussain/ML/project/nlp_project/data/result.txt'

def pdf_to_text(path):
    manager = PDFResourceManager()
    retstr = BytesIO()
    layout = LAParams(all_texts=True)
    device = TextConverter(manager, retstr, laparams=layout)
    filepath = open(path, 'rb')
    interpreter = PDFPageInterpreter(manager, device)

    for page in PDFPage.get_pages(filepath, check_extractable=True):
        interpreter.process_page(page)

    text = retstr.getvalue()

    filepath.close()
    device.close()
    retstr.close()
    return text

def patternCheck(text,data):
    if text == 'abstract':
        text = r"^A([b|B][s|S][t|T][r|R][a|A][c|C][t|T])"
    if text == 'results':
        text = r"^R([e|E|\s][s|S|\s][u|U|\s][l|L|\s][t|T|\s][s|S|\s])"
    if text == 'conclusions':
        text = r"^C([o|O|\s][n|N|\s][c|C|\s][l|L|\s][u|U|\s][s|S|\s][i|I|\s][o|O|\s][n|N|\s][s|S|\s])"
    if re.search(text,data):
        return True

def cutPara(data,feature):
    fo = open("test.txt", "wb")
    fo.write(data)
    fo = open("test.txt", "rb")
    extract = 'false'
    para = ''
    lines = fo.readlines()
    index = 0
    
    for line in lines:
        if patternCheck(feature,line):
            extract = 'true'
            if lines[index+1] == '\n':
                lines[index+1] = ''
        if line == '\n':
            extract = 'false'
        if extract == 'true':
            para = para + line
        index = index + 1
    fo.close()
    os.remove("test.txt")
    return para



def getPartialData(path,keyinput):
    data = pdf_to_text(path)
    partialData = cutPara(data,keyinput).replace('\n',' ')
    summarizeData = summarize(partialData)
    return summarizeData

def getAllFiles(path,keyinput):
    fileObj = open("partial1.txt", "wb")
    fileList = []
    for filename in os.listdir(path):
        filepath = ''
        if filename.endswith(".pdf"):
            filepath = path + filename
            partialData = getPartialData(filepath,keyinput)
            if partialData == '':
                fileList.append(filename)
                continue
            fileObj.write(filename+"\n")
            fileObj.write(partialData)
            fileObj.write("\n\n")
    print "FIle LIST " + str(fileList)

def printMessage(msg):
    print "############# " + msg + " ############"

def perfomPartAnalysis(path,keyinput):
    printMessage('Performing Partial Analysis : '+keyinput)
    path = '/home/hussain/ML/project/nlp_project/data/raw/'
    getAllFiles(path,keyinput)




# path = '/home/hussain/ML/project/nlp_project/data/raw/'
# getAllFiles(path,'abstract')