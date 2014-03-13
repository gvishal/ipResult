import sys
import re

pattern = re.compile(r'([0-9])')

#f_input = sys.arg[1]
#f_output = sys.arg[2]
f_input = "raw_result_sample.txt"
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

x,y = records[0][5].split()
print x + '+' + y
'''
for n in xrange(n):
  for i in xrange(41):
    print i,records[n][i]
'''