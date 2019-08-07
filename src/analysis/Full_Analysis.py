# from src import utility,FileInfo
# from src.vars import global_vars as vars
# from src.analysis import PartAnalysis as pa
import pandas as pd
import tabula,nltk,re,csv
import textract,parawrap,os,shutil
from textwrap3 import wrap
from flashtext import KeywordProcessor
from gensim.summarization.summarizer import summarize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from src import utility

nltk.download('stopwords')

en_stops = set(stopwords.words('english'))

def pdf_textract(filepath):
    text = textract.process(filepath)
    # print summarize(text)
    return text

def linesFormat(filepath):
    lines = pdf_textract(filepath).split("\n")
    index = 0
    output = ''
    # write = true
    for line in lines:
        write = 'true'
        # Check for line which has upto 2 words
        if len(line.split()) <= 2:
            write = 'false'
        # Check for lines which contains empty space
        elif line == '\n':
            write = 'false'
        index = index + 1

        if write == 'true':
            output = output +"\n"+ line
    return output

def individualAnalysis(filepath):
    paras = linesFormat(filepath).split(".")
    keywords = ["ABSTRACT","Conclusions","Materials","syndrome","disease","disorder","behavioral","impairment","results","mutations","symptoms","patient","sibling","predicted","termination","detected","analytics","spectrum","neurons","spine"]
    result = ''
    for line in paras:
        upline = re.sub("\n"," ",line)
        line = ''
        words = upline.split()
        for word in words:
            if word not in en_stops or word in keywords:
                line = line +" "+ word
        result = result +"\n"+ line
    return summarize(result)


def getAllFilesToText(inputpath,keyinput):
    fileObj = open(keyinput+".txt", "wb")
    emptyFileList = []
    for filename in os.listdir(inputpath):
        filepath = ''
        if filename.endswith(".pdf"):
            filepath = inputpath + filename
            partialData = individualAnalysis(filepath)
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

def performFullAnalysis(path,keyinput):
    utility.printLog('Performing Partial Analysis : '+keyinput)
    getAllFilesToText(path,keyinput)