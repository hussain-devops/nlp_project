import smtplib
import zipfile
import time
from email.mime.multipart import MIMEMultipart 
from email.mime.base import MIMEBase 
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate 
from email import encoders
def sendGmail(user = "hidden",pwd = "NLP@Passion@12",FROM = "hidden",TO = ['hidden'],SUBJECT = 'email',textMessage = 'Sample Massage'):
    #message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
    #""" % (FROM, ", ".join(TO), SUBJECT, textMessage)
    zf = zipfile.ZipFile("/home/hussain/ML/project/nlp_project/result.zip")
    msg = MIMEMultipart()
    msg['From'] = "nlpproject01@gmail.com"
    msg['To'] = "003nafs@gmail.com"
    msg['Date'] = formatdate(localtime = True)
    msg['Subject'] = SUBJECT
    msg.attach (MIMEText(textMessage))
    part = MIMEBase('application', "octet-stream")
    part.set_payload(zf.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="result.zip"')
    msg.attach(part)
    try:
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.ehlo()
        server.login(user, pwd)
        server.sendmail(FROM, TO, str(msg))
        server.close()
        print 'successfully sent the mail'
    except Exception, e:
        print e
def main():
    textMessage = '''
        Email from a script
        The information in here is
        a zip file.
    '''
    sendGmail(textMessage = textMessage)
if __name__ == '__main__':
    main()