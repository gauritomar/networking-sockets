import smtplib
from email import encoders
from email.mime.text import MIMEText   
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

from config import USER_EMAIL, USER_PASSWORD, RECEIVER_EMAIL, MESSAGE

server = smtplib.SMTP('smtp.gmail.com', 587)

server.ehlo() #Extended Hello, part of the Email Protocol

server.login(USER_EMAIL, USER_PASSWORD)


msg = MIMEMultipart()
msg['From'] = USER_EMAIL
msg['To'] = RECEIVER_EMAIL
msg['Subject'] = 'Just a test'

msg.attach(MIMEText(MESSAGE, 'plain'))

filename = 'server.png'
attachment = open(filename, 'rb') #reading byte mode

p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header('Content-Disposition', f'attachment; filename={filename}')
msg.attach(p)

text = msg.as_string()
server.sendmail(USER_EMAIL, RECEIVER_EMAIL, text)
