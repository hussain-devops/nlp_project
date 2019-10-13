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