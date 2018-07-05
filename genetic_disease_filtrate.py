#!/usr/bin/env python
# # coding=utf-8

import os
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--whanno_txt", required = True, help ="whanno.txt")
parser.add_argument("-i2", "--intron_txt", required = True, help ="intron.txt")
parser.add_argument("-s", "--son",type = int,default = 104,help="col of propositus")
parser.add_argument("-f", "--father",type = int,default = 103,help="col of father")
parser.add_argument("-m", "--mom",type = int,default = 105,help="col of mother")
args = parser.parse_args()

def contain_exon_Utr_spli(item):
    if ("ncRNA_exonic" not in item) and (("exonic" in item)  or ("splicing" in item) or ("UTR" in item)):
        return True
    else:
        return False

def new_mutation_discover(item,snp_son,snp_father,snp_mom):
    if (snp_son[0] not in snp_father) and  (snp_son[1] not in snp_father) and  (snp_son[1] not in snp_father) and  (snp_son[1] not in snp_father):
        new_item = item + "\t" + "new mutation detective"
    else:
        if snp_son[0] in snp_father:
            if snp_son[1] not in snp_mom:
                if snp_son[0]not in snp_mom:
                    new_item = item + "\t" + "new mutation detective"
                else:
                    if snp_son[1] not in snp_father:
                        new_item = item + "\t" + "new mutation detective"
                    else:
                        new_item = item
            else:
                new_item = item
        elif snp_son[0] in snp_mom:
            if snp_son[1] not in snp_father:
                new_item = item + "\t" + "new mutation detective"
            else:
                new_item = item
        else:
            new_item = item + "\t" + "new mutation detective"
    return new_item


# result_part2 = []
def compound_heterozygous_discover(lines):
    after_compound_heterozygous_discover = []
    num = 0
    length = len(lines)
    while True:
        gene_test = []
        in_line = []
        snp_par = {}
        new_line = ''
        if num == length:
            break
        else:
            target_line = lines[num]
            gene = target_line.split("\t")[6]
            gene_test.append(gene)
            in_line.append(target_line)
            while True:
                num += 1
                if num == length:
                    break
                else:
                    next2 = lines[num]
                    gene2 = next2.split("\t")[6]
                    if gene2 in gene_test:
                        in_line.append(next2)
                    else:
                        break
            if len(in_line) > 1:
                direction = []
                for item in in_line:
                    snp_son = item.split("\t")[args.son].split(":")[0].split("/")
                    snp_par["fa"] = item.split("\t")[args.father].split(":")[0].split("/")
                    snp_par["mo"] = item.split("\t")[args.mom].split(":")[0].split("/")
                    if "1" in snp_son or "2" in snp_son or "3" in snp_son or "4" in snp_son or "5" in snp_son:
                        for snp in snp_son:
                            if snp != "0":
                                if snp in snp_par["fa"]:
                                    if snp not in snp_par["mo"]:
                                        direction.append("fa")
                                    else:
                                        pass
                                if snp in snp_par["mo"]:
                                    if snp not in snp_par["fa"]:
                                        direction.append("mo")
                                    else:
                                        pass
                                else:
                                    pass
                            else:
                                pass
                    else:
                        pass
                if "mo" in direction and "fa" in direction:
                    for in_lin in in_line:
                        new_line = in_lin + "\t"+"compound heterozygous"
                        after_compound_heterozygous_discover.append(new_line)
                else:
                    for in_lin in in_line:
                        new_line = in_lin
                        after_compound_heterozygous_discover.append(new_line)
            else:
                new_line = target_line
                after_compound_heterozygous_discover.append(new_line)
    return after_compound_heterozygous_discover

out_file = os.path.splitext(fileName)[0] + "mutation_compound_heterozygous_discover.txt"

if __name__ == "__main__":
    #  = os.path.basename(inputFile)
    with open(args.whanno_txt,"r") as txt:
        after_mutation_list = []
        for line1 in txt:
            line = line1.strip()
            snp = line.split("\t")
            Chr = snp[0]
            Func_refGene = snp[5]
            father = snp[args.father]
            mom = snp[args.mom]
            son = snp[args.son]
            snp_par = {}
            snp_son = son.split(":")[0].split("/")
            snp_par["fa"] = father.split(":")[0].split("/")
            snp_par["mo"] = mom.split(":")[0].split("/")
            if contain_exon_Utr_spli(Func_refGene):
                if ("." not in snp_son and  "." not in snp_par["fa"] and  "." not in snp_par["mo"]):
                    after_mutation = new_mutation_discover(line,snp_son,snp_par["fa"],snp_par["mo"])
                    after_mutation_list.append(after_mutation)
        result = compound_heterozygous_discover(after_mutation_list)

    with open(args.whanno_txt,"r") as txt2:
        intron = txt2.readlines()
    intron.extend(result)
    output = "\n".join(intron)

    with open(out_file, 'w', encoding='utf-16') as out:
        out.write(output)




