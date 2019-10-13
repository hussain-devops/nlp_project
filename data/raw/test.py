from src.vars import global_vars as vars
from src.nlp import pdf_data as pdata

#print (global_vars.raw_folder)
print vars.raw_folder
print vars.processed_folder

path = vars.raw_folder + '/hichri.pdf'

pdata.getPdfInfo(path)