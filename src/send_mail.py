#########################################################
# This file has the function to send email
#
########################################################

import smtplib,ssl,base64,os
from src.vars import global_vars as vars
from src import utility
from src.project_utility import yaspin_demo as yd

def generate_table_data(status):
    table_row =''
    for i in status:
        status_style = '' 
        if i['status']=='FAILURE':
            status_style = "background:red"
        table_row = table_row + """<tr> <td>"""+i['name']+"""</td><td style="""+status_style+""">"""+i['status']+"""</td></tr>"""
    return table_row

def send_Email(analysis_type,name,email,status):
    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls
    sender_email = os.environ['nlp_sender_email']
    receiver_email = email
    execution_status=generate_table_data(status)
    # print status['file_status]

    # filename = vars.processed_folder+"results1.txt"
    filename = utility.getFileName(vars.processed_folder)
    marker = "AUNIQUEMARKER"

    fo = open(filename, "rb")
    filecontent = fo.read()
    encodedcontent = base64.b64encode(filecontent)  # base64

    password = base64.b64decode(os.environ['nlp_sender_email_password'])

    body ="""
    <head>
      <style>
         table, th, td {
            border: 1px solid black;
         }
      </style>
   </head>
<h2>Hi """+name+""",</h2>
<h3 style="border:2px solid DodgerBlue;">Thanks for using <i>NLP Framework for Curation of Scientific Literature</i><h3><br>

<br>
<table border="0">
<tr>
<th> File Name</th>
<th>Status</th>
</tr>
"""+execution_status+"""
</table>
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

    