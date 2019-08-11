from qzkc/python2.7:v2

WORKDIR /app/nlp

COPY ./src/ src/
COPY start_analysis.py ./

RUN yum install swig python-dev 

RUN pip install PyPDF2 nltk textstat textract