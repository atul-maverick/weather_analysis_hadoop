#!/usr/bin/env python
"""A more advanced Mapper, using Python iterators and generators."""

import sys
import operator
#http://www.michael-noll.com/tutorials/writing-an-hadoop-mapreduce-program-in-python/#reduce-step-reducerpy
def read_input(file):
    season=[0]*3
    pcomb=''
    ccomb=''
    for line in file:
	line=line.strip().strip("\n")
	if not line:
	    continue
	line=line.split('\t')
	ccomb=line[0]+":"+line[1]
	if pcomb=='':
	    pcomb=ccomb
        if pcomb==ccomb:
	    try:
	        season=map(operator.add,season,map(float,line[2:]))
	    except ValueError:
	        continue
	else:
	    year,ss=pcomb.split(":")
	    yield year,ss,season[0]/3,season[1]/3,season[2]/3
	    pcomb=ccomb
	    del season
	    season=[0]*3
    if pcomb==ccomb:
	year,ss=pcomb.split(":")
        yield year,ss,season[0]/3,season[1]/3,season[2]/3
def main(separator='\n'):
    # input comes from STDIN (standard input)
    data = read_input(sys.stdin)
    #date = read_date(sys.stdin)
    for words in data:
	print "{0}\t{1}\t{2}\t{3}\t{4}".format(words[0],words[1],words[2],words[3],words[4])

if __name__ == "__main__":
    main()
