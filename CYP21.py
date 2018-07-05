import sys
before = open(sys.argv[1],"r")
after = open(sys.argv[2],"w")
sys.stdout = after
first = before.readlines()
for line in first:
    if "#" in line:
        sys.stdout.write(line)
    else:
        pos = int(line.split()[1])+32005092
        ch = "chr6"
        # re = ch + str(pos) + line.split()[2:]
        # re = ch + str(pos) +
        re = ch + '\t' + str(pos) + '\t' + line.split()[2] + '\t' + line.split()[3] + '\t' + line.split()[4] + '\t' + line.split()[5] + '\t' + line.split()[6] + '\t' + line.split()[7] + '\t' + line.split()[8] + '\t' + line.split()[9] + '\n'
        sys.stdout.write(re)

