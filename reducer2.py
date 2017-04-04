#!/usr/bin/env python
"""A more advanced Mapper, using Python iterators and generators."""

import sys
import operator
#http://www.michael-noll.com/tutorials/writing-an-hadoop-mapreduce-program-in-python/#reduce-step-reducerpy
def read_input(file):
    season=[0]*3
    py=''
    cy=''
    for line in file:
	line=line.strip().strip("\n")
	if line=='':
	    continue
	line=line.split('\t')
	cy=line[0]
	if py=='':
	    py=cy
        if py==cy:
	    try:
   	        season=map(operator.add,season,map(float,line[1:]))
	    except ValueError:
	        continue
	else:
	    yield py,season[0]/4,season[1]/4,season[2]/4
	    py=cy
	    del season
	    season=[0]*3
    if py==cy:
        yield py,season[0]/4,season[1]/4,season[2]/4
def main(separator='\n'):
    # input comes from STDIN (standard input)
    data = read_input(sys.stdin)
    #date = read_date(sys.stdin)
    for words in data:
	print "{0}\t{1}\t{2}\t{3}".format(words[0],words[1],words[2],words[3])

if __name__ == "__main__":
    main()
