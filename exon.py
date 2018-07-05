#!usr/bin/python
import sys
gtf = open(sys.argv[1],"r")
re = open(sys.argv[2],"w")
sys.stdout = re
lines = gtf.readlines()
for line in lines:
    if "A" in line or "T" in line or "C" in line or "G" in line or "a" in line or "g" in line or "c" in line or "t" in line:
        sys.stdout.write(line)