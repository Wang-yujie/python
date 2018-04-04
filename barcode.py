#!usr/bin/python
import sys

out1 = open(sys.argv[3],"w")
out2 = open(sys.argv[4],"w")
a = {}
b = {}

with open(sys.argv[1],"r") as R1:
    read1s = R1.readlines()
    for read1 in read1s:
        if "@" in read1:
            key1 = read1.split(' ')[0]
            if key1 in a.keys():
                pass
            else:
                count1 = read1s.index(read1)
                a[key1] = (read1 + read1s[count1+1] + read1s[count1+2] + read1s[count1+3])


with open(sys.argv[2],"r") as R2:
    read2s = R2.readlines()
    for read2 in read2s:
        if "@" in read2:
            key2 = read2.split(' ')[0]
            if key2 in b.keys():
                pass
            else:
                count2 = read2s.index(read2)
                b[key2] = (read2 + read2s[count2+1] + read2s[count2+2] + read2s[count2+3])
for key in a.keys():
    sys.stdout = out1
    sys.stdout.write(a[key])
    sys.stdout = out2
    sys.stdout.write(b[key])



