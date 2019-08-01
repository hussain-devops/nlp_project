import PyPDF2

pdf_document_reader = PyPDF2.PdfFileReader("/home/hussain/sample_pdf/sample_data.pdf") 
pdf_document_writer = PyPDF2.PdfFileWriter()


page_one = pdf_document_reader.getPage(0)  

# pdf_document_writer.addPage(page_one)
text = 'adfasdfjalskdjflasjdf'
pdf_document_writer.addMetadata(text)
pdf_output_file = open('/home/hussain/sample_pdf/new_pdf1_file.pdf', 'wb')

pdf_document_writer.write(pdf_output_file)