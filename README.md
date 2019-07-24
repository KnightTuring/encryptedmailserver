# Encrypted Mail Server 
This is my very first attempt at developing something of this sort. :D 
This was originally developed as a mini project for Computer Networks, a subject taught in the 6th semester of the B.E degree course in Computer Engg at PCCOE, Pune.
It is a simple demonstration of a SMTP server that after recieving mail from a client, encrypts it using the AES standard and 
stores the cipher in its database (SQLITE3 in this case).
As of now, the functionality for allowing a client to retrieve mail(s) from the server db has not been implemented. However, the plan is
that once a client request for a mail, it is decrypted using the key and is then displayed. 


The description of the various files in the repo is as follows:
server.py
  -- This, as the name suggests is the code running on the SMTP server. It uses the smtpd library available in Python.
  -- On receiving a mail, it displays the contents of the mail, then encrypts it (using <cipherobject>.encrypt(<maildata>)) and
  then adds it into the sqlite3 database it is connected to.
  
client.py
   -- The program needed to run on the client system. It uses the smtplib library to send the mail to the server running the 
   server.py code. 
   -- The IP address and the port number of the server have to be specified (see code for further clarity)

 dbconn.py
   -- This file establishes the connection with the sqlite3 db. It contains the function definition of accessDB() used by 
   server.py to push the mail recieved into the db. Refer code for schema details.
  
 crypto_secure.py
   -- This file handles all the encryption/decryption using the AES algorithm. 
   -- The function definition of encrypt() and decrypt() used in server.py are contained within this file. 
   -- AES has some restrictions on the length of the key and the text that it encypts, both of these have to be in
   multiples of 32. Therefore, for freedom to choose a key and text of any length, both of them have to be padded(using the _pad()
   and _unpad() method )
   
   Feel free to use the code available here subject to standard GitHub license terms and conditions.
   :)
 
