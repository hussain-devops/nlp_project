# Python code to illustrate Sending mail from 
# your Gmail account 
import smtplib,ssl,base64

smtp_server = "smtp.gmail.com"
port = 587  # For starttls
sender_email = "nlpproject01@gmail.com"
receiver_email = "003nafs@gmail.com"
# password = raw_input("Type your password and press enter: ")

filename = "/home/hussain/ML/project/nlp_project/sample.txt"
marker = "AUNIQUEMARKER"

fo = open(filename, "rb")
filecontent = fo.read()
encodedcontent = base64.b64encode(filecontent)  # base64

body ="""
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
""" %(filename, "analysis_result.txt", encodedcontent, marker)

message = part1 + part2 + part3

try:

# creates SMTP session 
    s = smtplib.SMTP(smtp_server,port) 

# start TLS for security 
    s.starttls()
 # Secure the connection

# Authentication 
    s.login(sender_email, password) 

# message to be sent 
# message = "This is a sample TEST MAIL"

# sending the mail 
    s.sendmail(sender_email, receiver_email, message) 

# terminating the session 
    s.quit()
except:
    print("Error: Unable to send the mail")

print("Session has been terminated")