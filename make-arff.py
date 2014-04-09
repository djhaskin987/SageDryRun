#! /usr/bin/env python

import sys
import getopt
import csv

def usage():
    print 'convert_to_arff.py -i <inputfile> -o <outputfile>'
    sys.exit(2)

def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        usage()
    for opt, arg in opts:
        if opt == '-h':
            print 'test.py -i <inputfile> -o <outputfile>'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
    if len(outputfile) == 0 or len(inputfile) == 0:
        usage()
    with open(inputfile, 'rU') as f:
        reader = csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONE)
        for row in reader:
            print row[0]

def import_text(filename, separator):
    for line in csv.reader(open(filename), delimiter=separator, 
                           skipinitialspace=True):
        if line:
            yield line

if __name__ == "__main__":
   main(sys.argv[1:])
