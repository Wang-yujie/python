import sys
input1 = open(sys.argv[1],"r")
input2 = open(sys.argv[2],"r")
input3 = open(sys.argv[3],"r")
input4 = open(sys.argv[4],"r")
out1 = open(sys.argv[5],"w")
out2 = open(sys.argv[6],"w")
zongR1_lines = input1.readlines()
zongR2_lines = input2.readlines()
heR1_lines = input3.readlines()
heR2_lines = input4.readlines()
for heR1_line in heR1_lines:
    if '@' in heR1_line:
        name = heR1_line.split()[0]
        if name not in zongR1_lines:
            sys.stdout.write(heR1_line)
