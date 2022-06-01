# import necessary packages
 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from email import encoders
from platform import python_version
from getip import *
from json import *
import json
import sys
# create message object instance
msg = MIMEMultipart()

ipss = json.dumps(ips)
message = ipss
 
# setup the parameters of the message
password = "wwjhkbxufslzknkf"
msg['From'] = "alexeyashitok@gmail.com"
msg['To'] = "supersell2020204@gmail.com"
msg['Subject'] = "new ip"
 
# add in the message body
msg.attach(MIMEText(message, 'plain'))
 
#create server
server = smtplib.SMTP('smtp.gmail.com: 587')
 
server.starttls()
 
# Login Credentials for sending the mail
server.login(msg['From'], password)
 
 
# send the message via the server.
server.sendmail(msg['From'], msg['To'], msg.as_string())
 
server.quit()
 
print ("successfully sent email to %s:" % (msg['To']))
