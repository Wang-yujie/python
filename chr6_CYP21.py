import sys
input1 = open(sys.argv[1],"r")
out1 = open(sys.argv[2],"w")
sys.stdout = out1
lines = input1.readlines()
# for line in lines:
#     if ">chr6" in line and "chr6_" not in line:
#         sys.stdout.write(line)
#         count = lines.index(line)
#         while True:
#             ne = lines[count+1]
#             if ">chr7" in ne or "chr6_" in ne:
#                 break
#             else:
#                 sys.stdout.write(ne)
#                 count = count+1
# for line in lines:
#     if "CTTTGGACTTTGAGGGGGGCATGCCCAGTTGTGCTGGGAATCCATACTTT" in line:
#         count = lines.index(line)
#         # if "CCCTGGCTGGAGTAGAACCTGTGGACTGTAGTCCTGAGGGCAGTCATGTT" in lines[count+1]:
#         print(line)
#         print(lines[count-1])
# i=int(range(1,10000000))
# seqq=''
# for line in lines:
#     if ">chr6" in line:
#        sys.stdout.write(line)
#     else:
#         seq = line.strip('\n')
#         seq1 = seq.strip()
#         sys.stdout.write(seq1)
# i=1
# for line in lines:
#     # count = lines.index(line)
#     if ">chr6" in line:
#         sys.stdout.write(line)
#     else:
#         seq = line.strip('\n')
#         seq1 = seq.strip()
#         for st in seq1:
#             if i%50 == 0:
#                 sys.stdout.write(st+"\n")
#             else:
#                 sys.stdout.write(st)
#             i=i+1

