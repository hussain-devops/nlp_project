import PyPDF2

def getPdfInfo(path):
    pdfObj = pdfReadObject(path)
    info = pdfObj.getDocumentInfo()
    print 'Title : '+ info.title
    print 'Creator : '+ info.creator
    print 'Producer : '+ info.producer

def pdfReadObject(path):
    pdfReadObj = PyPDF2.PdfFileReader(path,"rb")
    return pdfReadObj

def pdfWriteObject(path):
    pdfWriteObj = PyPDF2.PdfFileWriter() 
    return pdfWriteObj