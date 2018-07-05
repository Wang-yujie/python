import os
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--anno_txt", required = True, help ="hg19_anno.txt")
parser.add_argument("-f", "--father",type = int,required = True,help="col of father")
args = parser.parse_args()

fa = args.father
total_count = 0
heterozygote = 0
zero_homozygote = 0
alle_homozygote = 0

with open(args.anno_txt,"r") as txt:
    first_line = txt.readline()
    first_name = first_line.split("\t")[fa]
    for line1 in txt:
        line = line1.strip()
        snp = line.split("\t")
        snp_fa = snp[fa]
        snp_type = snp_fa.split(":")[0]
        # print(snp_fa)
        if "./." not in snp_type:
            total_count += 1
            if "0/1" in snp_type:
                heterozygote += 1
            if "0/0" in snp_type:
                zero_homozygote += 1
            if "1/1" in snp_type:
                alle_homozygote += 1
    ratio_0_1 = heterozygote/total_count
    ratio_0_0 = zero_homozygote/total_count
    ratio_1_1 = alle_homozygote/total_count

print(first_name+"\n"+"ratio_0_1: "+ str(ratio_0_1)+"\n"+"ratio_0_0: "+str(ratio_0_0)+"\n"+"ratio_1_1: "+ str(ratio_1_1))