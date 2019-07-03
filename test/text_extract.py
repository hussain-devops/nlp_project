import PyPDF2
import nltk
from gensim.summarization import summarize

#pdf = PyPDF2.PdfFileReader('../sample_pdf/sample_data.pdf')

pdf = PyPDF2.PdfFileReader('/home/hussain/sample_pdf/lit_OCRL/iPSC_OCRL_MolAut.pdf',"rb")
pdf_document_writer = PyPDF2.PdfFileWriter() 

#pdf.numPages()

page = pdf.getPage(0)
content = page.extractText()

# info = content1.extractText()
# content = content.replace('\n\n',', ').replace('\n',' ').strip()
# content = nltk.word_tokenize(content)


print content


# pdf_document_writer.addBlankPage()
# pdf_output_file = open('/home/hussain/sample_pdf/test.pdf', 'wb')
# pdf_document_writer.write(pdf_output_file)