

import sqlite3

def accessDB(addrto,addrfrom,mailtext):

	db=sqlite3.connect('smtpDB.db')
        cur=db.cursor()
	sql='''insert into mailsdata(addrto,addrfrom,maildata) values(?,?,?)'''
	cur.execute(sql,(addrto,addrfrom,mailtext))
	db.commit()
	print 'Data Inserted'
        db.close()

'''def readDB():
        db=sqlite3.connect('smtpDB.db')
        cur=db.cursor()
'''        
	



