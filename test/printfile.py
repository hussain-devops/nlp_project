import os

for file in os.listdir("/home/hussain/ML/project/nlp_project/data/raw/"):
    if file.endswith(".txt"):
        print file