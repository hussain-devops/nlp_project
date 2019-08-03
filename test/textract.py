import textract


path = '/home/hussain/ML/project/nlp_project/data/raw/iPSC_OCRL_MolAut.pdf'
text = textract.process(path)
print text