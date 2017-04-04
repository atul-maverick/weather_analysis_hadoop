#!/usr/bin/env python
"""A more advanced Mapper, using Python iterators and generators."""

import sys
import operator

def main(separator='\n'):
    # input comes from STDIN (standard input)
    #date = read_date(sys.stdin)
    for words in sys.stdin:
	words=words.split("\t")
	print "{0}\t{1}\t{2}\t{3}".format(words[0],words[2],words[3],words[4])

if __name__ == "__main__":
    main()
