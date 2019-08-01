# from src import utility,FileInfo
# from src.vars import global_vars as vars
# from src.analysis import PartAnalysis as pa
import pandas as pd
import tabula,nltk,re
import textract,parawrap
from textwrap3 import wrap
from flashtext import KeywordProcessor
import gensim.summarization as summarize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

en_stops = set(stopwords.words('english'))

# nltk.download('stopwords')

# hichri
# iPSC_OCRL_MolAut
# splicing_analysis_genes-09-00015

# processor = KeywordProcessor()
path = '/home/hussain/ML/project/nlp_project/data/raw/hichri.pdf'
# list = FileInfo.extractPdfMeta(path)

def pdf_textract(filepath):
    text = textract.process(filepath)
    # print summarize(text)
    return text

# def textProcessor(filepath):
#     num_words = 0
#     text = pdf_textract(path).strip()

#     # processor.add_keyword('Dent')
#     # found = processor.extract_keywords(text)
#     # for line in text:
#     #     words = line.split()
#     #     num_words += len(words)
#     # print num_words
#     # print parawrap.wrap(text)
#     # df = tabula.read_pdf(path, pages = '4', multiple_tables = True)
#     # print(df)
#     return text


# textProcessor(path)

def linesFormat():
    lines = pdf_textract(path).split("\n")
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


def paraFormat():
    paras = ''
    para = ''
    lines = linesFormat().split("\n")
    for line in lines:
        if line != '' and len(line.split()) > 3:
            para = 'start'
        elif line == '':
            para = 'end'
        
        if para == 'start':
            paras = paras + "\n" + line
        elif para == 'end':
            paras = paras + "\n"
    return paras


def individualPara():
    paras = linesFormat().split("\n")
    para = ['ABSTRACT',"Conclusions","Materials"]
    data = 'abstract'
    # fo = open("test.txt", "wb")
    # fo.write(paras)
    # fo.close()
    # fo = open("test.txt", "rb")
    # lines = fo.readlines()
    for line in paras:
        words = line.split(" ")
        for word in words: 
            if word not in en_stops:
                para = para + " "+word
                line = line + " " +  word
            # print line
        # if re.match("ABSTRACT",line):
        #     # x = re.split(r"ABSTRACT",line)
        #     # print x


        # result = summarize(line)
        # print words
    # for para in paras:
    #     if (para == ""):
    #         print "Para"
    # #     print para
    # fo.close()
    # os.remove("test.txt")
    # print para


# linesFormat()
individualPara()