#########################################################
# This file has the function to send email
#
########################################################

import smtplib,ssl,base64
from src.vars import global_vars as vars
from src import utility
from src.project_utility import yaspin_demo as yd

def send_Email(analysis_type,name,email):
    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls
    sender_email = "nlpproject01@gmail.com"
    receiver_email = email


    filename = vars.processed_folder+"results1.txt"
    marker = "AUNIQUEMARKER"

    fo = open(filename, "rb")
    filecontent = fo.read()
    encodedcontent = base64.b64encode(filecontent)  # base64

    password = base64.b64decode("TkxQQFBhc3Npb25AMTI=")

    body ="""
<h2>Hi """+name+""",</h2>
<h3 style="border:2px solid DodgerBlue;">Thanks for using <i>NLP Framework for Curation of Scientific Literature</i><h3><br>
<p>Please find the attachments of the analysis</p>
    """

    part1 = """From: NLP-Project <nlpproject01@gmail.com>
To: The User <003nafs@gmail.com>
MIME-Version: 1.0
Subject: Email From NLP Framework!!!
Content-Type: multipart/mixed; boundary=%s
--%s
""" % (marker, marker)

    part2 = """Content-Type: text/html
Content-Transfer-Encoding:8bit
%s
--%s
""" %(body,marker)

    part3 = """Content-Type: multipart/mixed; name=\"%s\"
Content-Transfer-Encoding:base64
Content-Disposition: attachment; filename=%s

%s
--%s--
""" %(filename, analysis_type+".txt", encodedcontent, marker)

    message = part1 + part2 + part3

    try:
        utility.printLog("Sending Mail To "+ receiver_email)
        s = smtplib.SMTP(smtp_server,port) 
        s.starttls()
        s.login(sender_email, password) 
        s.sendmail(sender_email, receiver_email, message)
        yd.any_spinner_you_like("Please wait until the mail is being sent !!!")
        utility.printLog("Mail has been successfully sent!!!")
        s.quit()
    except:
        utility.printError("Unable to send the mail")

    