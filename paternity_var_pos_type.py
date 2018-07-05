import argparse
import json
import random
import time

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--txt', required=True, help='str txt or txt file')
parser.add_argument('-l', '--list', required=True, help='list.json')
parser.add_argument('-f', '--fnum', type=int, help='father_data_column')
parser.add_argument('-m', '--mnum', type=int, help='mother_data_column')
parser.add_argument('-s', '--snum', type=int, help='mother_data_column')
parser.add_argument('-d', '--depth', type=int, help='min_var_depth')
args = parser.parse_args()

equal_number = []
result ={}
exist_number = []

with open(args.list) as plist:
    point = json.load(plist)
    CHR = ["chr1","chr2","chr3","chr4","chr5","chr6","chr7","chr8","chr9","chr10","chr11","chr12","chr13","chr14","chr15","chr16","chr17","chr18","chr19","chr20","chr21","chr22"]
    for i in CHR:
        b = point[i]["snp"].keys()
        for j in b:
            a = point[i]["snp"][j]["num"]
            exist_number.append(a)



with open(args.txt) as txt:
    header = txt.readline()
    for line in txt:
        line = line.strip()
        if line.split("\t")[1] in point[line.split("\t")[0]]["snp"].keys():
            number = int(point[line.split("\t")[0]]["snp"][line.split("\t")[1]]["num"])
        else:
            number = random.randint(point[line.split("\t")[0]]["start"],point[line.split("\t")[0]]["end"])
            while number in equal_number or number in exist_number:
                number = random.randint(point[line.split("\t")[0]]["start"],point[line.split("\t")[0]]["end"])
            equal_number.append(number)
        point[line.split("\t")[0]]["snp"][line.split("\t")[1]] = {}
        point[line.split("\t")[0]]["snp"][line.split("\t")[1]]["ref"] = line.split("\t")[3]
        point[line.split("\t")[0]]["snp"][line.split("\t")[1]]["alt"] = line.split("\t")[4]
        point[line.split("\t")[0]]["snp"][line.split("\t")[1]]["num"] = str(number)
        # type.txt中基因型生成
        son_type = line.split("\t")[3]+"/"+line.split("\t")[4]
        a = {"0": line.split("\t")[3],"1":line.split("\t")[4]}
        dad_type = a[(line.split("\t")[args.fnum].split(":")[0]).split("/")[0]]+"/"+a[(line.split("\t")[args.fnum].split(":")[0]).split("/")[1]]
        mom_type = a[line.split("\t")[args.mnum].split(":")[0].split("/")[0]]+"/"+a[line.split("\t")[args.mnum].split(":")[0].split("/")[1]]
        result[number] = str(number) +"\t"+ line.split("\t")[0] +"\t"+ dad_type +"\t"+ mom_type +"\t"+ son_type +"\t"+ line.split("\t")[-1] + "\n"

with open("./type.txt","w") as RE:
    RE.write("point_number\t染色体\t父本基因型\t母本基因型\t胎儿基因型\t是否匹配\n")
    for key in sorted(result.keys()):
        RE.write(result[key])

time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
name = "/mnt/workshop/SC/script_hub/paternity/json/"+time+"new.json"
# name = time+"new.json"
with open(name,"w") as new:
    data = json.dumps(point,sort_keys=True,indent=4, separators=(',', ': '))
    new.write(data)
