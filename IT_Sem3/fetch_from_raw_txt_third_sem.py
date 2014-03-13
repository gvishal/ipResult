import sys
import re
import os
import sqlite3
conn = sqlite3.connect('ipResults_try.db')
#c = conn.cursor()

pattern = re.compile(r'([0-9])')

#f_input = sys.arg[1]
#f_output = sys.arg[2]
f_input = "raw_IT_First_Shift_third_Sem_txt.txt"
f_output = "output_" + f_input
records = []
n = 0
ctr = 0
record = []

with open(f_input) as f_in:
  for line in f_in:
    ctr += 1
    record.append(line.rstrip())
    if ctr == 35:
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
  sub = ['maths','analog','cns','fcs','oop','ds','analoglab','cnslab','ooplab','dslab']
  for s in sub:
    total += sub_total(data,s)
  return "%.3f" %(total/10.0)

def calc_perc_credit(data):
  total = 0
  credit_string = "4 4 4 4 4 4 1 1 1 1"
  sub = dict(maths=4,analog=4,cns=4,fcs=4,oop=4,ds=4,analoglab=1,cnslab=1,ooplab=1,dslab=1)
  for s in sub:
    total = total + (sub_total(data,s)*int(sub[s]))
  return "%.3f" %(total/28.0)

ctr = 0
for n in xrange(n):
  x = 5
  query_str = "INSERT INTO result({}) VALUES({})"
  data = dict(rollno=re.sub("[^0-9]","",records[n][0]),name=records[n][1],perc_credit=None,perc=None,
            credit_string="4 4 4 4 4 4 1 1 1 1",maths=form_marks(n,x),
            analog=form_marks(n,x+3),cns=form_marks(n,x+6),fcs=form_marks(n,x+9),
            oop=form_marks(n,x+12),ds=form_marks(n,x+15),analoglab=form_marks(n,x+18),
            cnslab=form_marks(n,x+21),ooplab=form_marks(n,x+24),dslab=form_marks(n,x+27))
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
c.execute('Select * FROM rdsult')
for r in c.fetchall():
  for moopber in r:
    print moopber'''