import sys
import re
import os
import sqlite3
conn = sqlite3.connect('ipResults_try.db')
#c = conn.cursor()

pattern = re.compile(r'([0-9])')

#f_input = sys.arg[1]
#f_output = sys.arg[2]
f_input = "raw_IT_First_Shift_Ist_Sem_txt.txt"
f_output = "output_" + f_input
records = []
n = 0
ctr = 0
record = []

with open(f_input) as f_in:
  for line in f_in:
    ctr += 1
    record.append(line.rstrip())
    if ctr == 41:
      ctr = 0
      n += 1
      records.append(record)
      record = []

def form_marks(n,i):
  return records[n][i].split()[0]+' '+records[n][i].split()[1]+' '+records[n][i+1].strip()

def sub_total(data,sub):
  x,y,z = data[sub].split()
  z = re.sub("[^0-9]","",z)
  if z:
    return int(z)
  else:
    return 0

def calc_perc(data):
  total = 0
  sub = ['maths','physics','evs','itp','em','es','cs','phylab','evslab','clab','emlab','eslab']
  for s in sub:
    total += sub_total(data,s)
  return "%.3f" %(total/12.0)

def calc_perc_credit(data):
  total = 0
  credit_string = "4 3 3 2 3 3 1 1 1 2 2 1"
  sub = dict(maths=4,physics=3,evs=3,itp=2,em=3,es=3,cs=1,phylab=1,evslab=1,clab=2,emlab=2,eslab=1)
  for s in sub:
    total = total + (sub_total(data,s)*int(sub[s]))
  return "%.3f" %(total/26.0)

ctr = 0
for n in xrange(n):
  x = 5
  query_str = "INSERT INTO result({}) VALUES({})"
  data = dict(rollno=re.sub("[^0-9]","",records[n][0]),name=records[n][1],perc_credit=None,perc=None,
            credit_string="4 3 3 2 3 3 1 1 1 2 2 1",maths=form_marks(n,x),
            physics=form_marks(n,x+3),evs=form_marks(n,x+6),itp=form_marks(n,x+9),
            em=form_marks(n,x+12),es=form_marks(n,x+15),cs=form_marks(n,x+18),
            phylab=form_marks(n,x+21),evslab=form_marks(n,x+24),clab=form_marks(n,x+27),
            emlab=form_marks(n,x+30),eslab=form_marks(n,x+33))
  data['perc'] = calc_perc(data)
  data['perc_credit'] = calc_perc_credit(data)
  print data
  columns, values = zip(*data.items())
  with open(f_output,mode='a') as f_out:
    if ctr == 0:
      for col in columns:
        f_out.write(col + ',')
      f_out.write("\n")
    for val in values:
      f_out.write(val + ',')
    f_out.write("\n")
    ctr += 1
  '''q = query_str.format(",".join(columns),",".join("?"*len(values)))
  conn.execute(q, values)
  conn.commit()

#Read from db
c = conn.cursor()
c.execute('Select * FROM result')
for r in c.fetchall():
  for member in r:
    print member'''