#!/usr/bin/env python
"""A more advanced Mapper, using Python iterators and generators."""

import sys
#http://www.michael-noll.com/tutorials/writing-an-hadoop-mapreduce-program-in-python/#reduce-step-reducerpy
def read_input(file):
    for line in file:
        #Extract the attributes based on the position of the attributes
	#replace the value if its +9999 with value 0 (Total number of values will remain same as the hour count in month/year for each attribute)
        if line[87:87+5] != "+9999":
            temp=line[87:87+5]
	    if line[99:99+4] != "+9999":
                atm_pressure=line[99:99+4]
            else:
                atm_pressure=0
	    if line[65:65+4] != "+9999":
	        wind_speed= line[65:65+4]
            else:
	        wind_speed= 0
            yield line[15:15+6],temp,atm_pressure,wind_speed
    	

def main(separator='\n'):
    # input comes from STDIN (standard input)
    data = read_input(sys.stdin)
    #date = read_date(sys.stdin)
    for words in data:
         # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
	print "{0}\t{1}\t{2}\t{3}".format(words[0],words[1],words[2],words[3])

if __name__ == "__main__":
    main()
