import smtpd
import asyncore
from dbconn import accessDB
#from dbconn import closeDB
from crypto_secure import AESCipher
class CustomSMTPServer(smtpd.SMTPServer):
    
    def process_message(self, peer, mailfrom, rcpttos, data):
        print 'Receiving message from:', peer
        print 'Message addressed from:', mailfrom
        print 'Message addressed to  :', rcpttos
        print 'Message length        :', len(data)
        print '---------------------' 
        
        #all methods below are for DB insertion
        
        mail_to=''.join(rcpttos)		#rcpttos is list, converted to string here
                                                #print 'STRING: ', recieptto
        mail_from=mailfrom
        mail_data=data

        cipherobj=AESCipher('thisisthekey')
        cipher_text=cipherobj.encrypt(mail_data)
        print 'Original mail data is:',data
        print 'Encrypted is\n',cipher_text

        
        accessDB(mail_to,mail_from,cipher_text)
        
        
server = CustomSMTPServer(('192.168.137.128', 1025), None)
print 'SMTP server running...'

asyncore.loop()
