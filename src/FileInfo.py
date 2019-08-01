import os;
from PyPDF2 import PdfFileReader

def extractPdfMeta(pdf_path):
    with open(pdf_path, 'rb') as f:
        pdf = PdfFileReader(f)
        meta = pdf.getDocumentInfo()
        number_of_pages = pdf.getNumPages()
        mylist = [meta.title,meta.creator]
        return mylist

def getFileCount(self,path):
    length = len([name for name in os.listdir(path) if os.path.isfile(os.path.join(path, name))])
    return length

