# #!usr/bin/python

import sys
IN = open(sys.argv[1],"r")
# RE = open("bed_name","w")
# sys.stdout = RE
# BedName = sys.argv[1].split("_")[0]
# sys.stdout.write(BedName+"\n")
# # for line in IN:
# #     name = line.split()[3]+".bed"
# #     RE= open(name,"w")
# #     sys.stdout = RE
# #     sys.stdout.write(line)

ALL = open(sys.argv[2],"a")
sys.stdout = ALL
first_line = sys.argv[1]
sys.stdout.write(first_line+"\n")
for line in IN:
    sys.stdout.write(line)
sys.stdout.write("\n")
