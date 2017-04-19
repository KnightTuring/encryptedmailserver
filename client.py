from crypto_secure import AESCipher

import smtplib
import email.utils
from email.mime.text import MIMEText

#CipherClass=AESCipher(<specify key here>)


# Create the message
#to
inp_to=raw_input('To:\t')
inp_to_name=raw_input('Name of reciever\t')

#from
inp_from=raw_input('From:\t')
inp_from_name=raw_input('Name of sender:\t')



#subject and body of mail
inp_subj=raw_input('Subject:\t')
inp_body=raw_input('Body:\t')

msg = MIMEText(inp_body)
msg['To'] = email.utils.formataddr((inp_to_name, inp_to))
msg['From'] = email.utils.formataddr((inp_from_name, inp_from))
msg['Subject'] = inp_subj

server = smtplib.SMTP('192.168.137.128', 1025)
server.set_debuglevel(True) # show communication with the server
try:
    server.sendmail(inp_from, [inp_to], msg.as_string())
finally:
    server.quit()
