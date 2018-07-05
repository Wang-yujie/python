#!usr/bin/python
import sys
cnv = open(sys.argv[1],"r")
re = open(sys.argv[2],"w")
sys.stdout = re
lines = cnv.readlines()
for line in lines:
    if line.split()[6] != "NA":
        sys.stdout.write(line)