import os
import sqlite3
conn = sqlite3.connect('ipResults_try.db')
c = conn.cursor()
c.execute('''CREATE TABLE result
			(rollno text,name text,perc_credit text,perc text,credit_string text,maths text,physics text,evs text,itp text,
				em text,es text,cs text,phylab text,evslab text,clab text,
				emlab text,eslab text
				)''')

'''Design of database
	perc_credit is percentage with credits and is numeric and so is perc
	credit_string is "4 3 3 3 3 3 3 1 1 1 2 1"
	Each subject field has following format and is text:"Internal Externam Total"  '''

'''c.execute("INSERT INTO result VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
			(rollno,name,perc_credit,perc,credit_string,maths,physics,evs,itp,em,es,cs,
				phylab,evslab,clab,emlab,eslab))'''
conn.commit()
conn.close()
print "Done...Trying to fetch from database"