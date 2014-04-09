#! /usr/bin/env python

import sys
import getopt

import csv

def main(argv):
	inputfile = ''
	outputfile = ''
	try:
		opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
	except getopt.GetoptError:
		print 'convert_to_arff.py -i <inputfile> -o <outputfile>'
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print 'test.py -i <inputfile> -o <outputfile>'
			sys.exit()
		elif opt in ("-i", "--ifile"):
			inputfile = arg
		elif opt in ("-o", "--ofile"):
			outputfile = arg

	snps = {}
	line_num = 0
	header = []
	all_lines = []
	single = []
	for line in inputfile:
		if(line_num == 0):
			header = line.split('\t')
		else:
			#print line
			single = line.split('\t')
			all_lines.append(single)
			pass
		line_num += 1
	print header

	#lets get the snps with the alleles
	count = 0
	for item in all_lines:
		for i in range(14,293):
			print all_lines[count][i]

		count += 1



def import_text(filename, separator):
    for line in csv.reader(open(filename), delimiter=separator, 
                           skipinitialspace=True):
        if line:
            yield line

for data in import_text('somefile.txt', '/'):
    print (data)

if __name__ == "__main__":
   main(sys.argv[1:])
