#!/usr/bin/env python
import sys

# input comes from STDIN
prevm=""
count=0
ctemp=0
cap=0
cw=0
for line in sys.stdin:
    # remove leading and trailing whitespace
    line=line.strip().strip("\n")
    if not line:
	continue
    #Splitting based on TAB
    try:
        line=map(int,line.split("\t"))
    except ValueError:
        continue
    currm=line[0]
    if prevm=="":
        prevm=currm
    if currm==prevm:
        count+=1
        ctemp+=line[1]
        cap+=line[2]
        cw+=line[3]
	#print(currrec)
    else:
	#print(currrec)
        print '{0}\t{1}\t{2}\t{3}'.format(prevm,float(ctemp)/(count*10),float(cap)/count,float(cw)/count)
	ctemp=0
	cap=0
	cw=0
	prevm=currm
        count=0
	#print(currec,prevm,currm,count)
if currm==prevm:
    print '{0}\t{1}\t{2}\t{3}'.format(prevm,float(ctemp)/(count*10),float(cap)/count,float(cw)/count)
