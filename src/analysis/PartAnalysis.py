import os,subprocess,re,nltk,shutil,textstat,textract
from textwrap import wrap
from gensim.summarization import summarize
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import BytesIO
from src import utility

# hichri
# iPSC_OCRL_MolAut
# splicing_analysis_genes-09-00015

# path = '/home/hussain/ML/project/nlp_project/data/raw/iPSC_OCRL_MolAut.pdf'
# outputpath = '/home/hussain/ML/project/nlp_project/data/result.txt'

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

def pdf_textract(filepath):
    text = textract.process(filepath)
    return text

def patternCheck(keytext,data):
    if keytext == 'abstract':
        keytext = r"^A([b|B][s|S][t|T][r|R][a|A][c|C][t|T])"

    if keytext == 'results':
        keytext = r"^R([e|E|\s][s|S|\s][u|U|\s][l|L|\s][t|T|\s][s|S|\s])"

    if keytext == 'conclusions':
        keytext = r"^C([o|O][n|N|\s][c|C|\s][l|L|\s][u|U|\s][s|S|\s][i|I|\s][o|O|\s][n|N|\s][s|S|\s])"

    if keytext == 'methods':
        keytext = r"^M([ethods|aterials])"

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
    emptyFileList = []
    for filename in os.listdir(inputpath):
        filepath = ''
        if filename.endswith(".pdf"):
            filepath = inputpath + filename
            partialData = getPartialData(filepath,keyinput)
            if partialData == '':
                emptyFileList.append(filename)
                continue
            fileObj.write("File Name : \t"+filename+"\n")
            fileObj.write("-----------------------------------------------------------\n")
            fileObj.write(partialData+"\n")
            fileObj.write("-----------------------------------------------------------\n")
    utility.printLog("Empty File LIST " + str(emptyFileList))
    utility.printLog("Moving the Output to Processed Folder")
    shutil.move(keyinput+".txt","data/processed/"+keyinput+".txt")

def getAllFilesToPdf(path,keyinput):
    fileObj = open(keyinput+".txt", "wb")

def perfomPartAnalysis(path,keyinput):
    utility.printLog('Performing Partial Analysis : '+keyinput)
    getAllFilesToText(path,keyinput)



# path = '/home/hussain/ML/project/nlp_project/data/raw/CD009645.pdf'

# data =getPartialData(path,'analysis')
# print data 