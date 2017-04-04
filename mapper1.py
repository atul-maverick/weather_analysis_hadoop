#!/usr/bin/env python
"""A more advanced Mapper, using Python iterators and generators."""

import sys
import operator
#http://www.michael-noll.com/tutorials/writing-an-hadoop-mapreduce-program-in-python/#reduce-step-reducerpy
def read_input(file):
    for line in file:
	line=line.split('\t')
	month=int(line[0][4:])
	if month>=3 and month<=5:
	    yield line[0][0:4],"Spring",line[1],line[2],line[3]
	elif month>=6 and month<=8:
	    yield line[0][0:4],"Summer",line[1],line[2],line[3]    
	elif month>=9 and month<=11:
	    yield line[0][0:4],"Fall",line[1],line[2],line[3]	
	else:
	    yield line[0][0:4],"Winter",line[1],line[2],line[3]

def main(separator='\n'):
    # input comes from STDIN (standard input)
    data = read_input(sys.stdin)
    #date = read_date(sys.stdin)
    for words in data:
         # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
	print "{0}\t{1}\t{2}\t{3}\t{4}".format(words[0],words[1],words[2],words[3],words[4])

if __name__ == "__main__":
    main()
