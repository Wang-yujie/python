#!/usr/bin/env python
# coding=utf-8

import os
import argparse

# optional args
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", required=True, help="input file")
parser.add_argument("-maf", "--minor_allele_frequency", type=float, help="minor allele frequency for filter snps[0.02]")
parser.add_argument("-d", "--gene_db", help="HGMD datebase path")
parser.add_argument("-b", "--base_dir", help="base file path")
parser.add_argument("-eye", "--eye_panel", action="store_true", default=False, help="internal eye_panel datebase path")
parser.add_argument("-endo", "--endo_panel", action="store_true", default=False, help="internal endo_panel datebase path")
parser.add_argument("-nerv", "--nerv_panel", action="store_true", default=False, help="internal nerv_panel datebase path")
parser.add_argument("-fh", "--fix_header", action="store_true", default=False, help="fix annovar file header")
parser.add_argument("-mc", "--mu_ch", action="store_true", default=False, help="new_mutation_discover and compound_heterozygous_discover")
parser.add_argument("-f", "--father",type = int,default = 103,help="col of father")
parser.add_argument("-s", "--son",type = int,default = 104,help="col of propositus")
parser.add_argument("-m", "--mom",type = int,default = 105,help="col of mother")
args = parser.parse_args()

if args.input:
    inputFile = args.input

if args.minor_allele_frequency:
    maf = args.minor_allele_frequency
else:
    maf = 0.02

if args.gene_db:
    geneDB = args.gene_db
else:
    geneDB = '/home/jimmy/exon/hg19_genedb.txt'

if args.base_dir:
    baseDir = args.base_dir
else:
    baseDir = './'

# function list
def all_same(items):
    return all(x == '.' for x in items)

def filter_maf(item):
    try:
        if item == '.' or float(item) < maf:
            return True
        else:
            return False
    except ValueError:
        return True

def fix_header(oldLine):
    with open(rawFile) as raw:
        for line in raw:
            if '#CHROM' in line:
                title = oldLine + '\tC1\tC2\t' + line.strip()
                break
    return title

def access_genedb():
    with open(geneDB) as genes:
        next(genes)
        for ln in genes:
            line = ln.strip().split('\t')
            chrPos = 'chr' + line[0] + ':' + line[1]
            mut = chrPos + ':' + line[3] + "-" + line[4]
            disInfo = line[5] + "|" + line[6] + "|" + line[7] + "|" + line[8] + "|" + line[9] + "|" + line[10] + "|" + line[11] + "|" + line[12] + "|" + line[13]

            if chrPos not in chrPosdb.keys():
                chrPosdb[chrPos] = chrPos + "|" + disInfo
            else:
                chrPosDis = chrPosdb[chrPos].split(';')
                for i in range(0, len(chrPosDis)):
                    if chrPosDis[i] != (chrPos + "|" + disInfo):
                        chrPosdb[chrPos] += ';' + chrPos + "|" + disInfo

            if mut not in mutdb.keys():
                mutdb[mut] = mut + "|" + disInfo
            else:
                mutdb[mut] += ';' + mut + "|" + disInfo

            if line[9] not in genedb.keys():
                genedb[line[9]] = line[13]
            else:
                geneDis = genedb[line[9]].split(';')
                if line[13] not in geneDis:
                    genedb[line[9]] += ';' + line[13]

def access_panel(file, lineNum):
    panelDB = {}
    with open(file, 'r') as panel:
        for ln in panel:
            line = ln.strip().split('\t')
            if lineNum > 0:
                try:
                    annoGene = line[7]
                except IndexError:
                    annoGene = line[5]
                lineInfo = line[1] + '(' + line[2] + ',' + line[3] + ')'
            else:
                annoGene = line[0]
                lineInfo = line[1]
            if annoGene not in panelDB.keys():
                panelDB[annoGene] = lineInfo
            else:
                geneDis = panelDB[annoGene].split(';')
                if lineInfo not in geneDis:
                    panelDB[annoGene] += ';' + lineInfo
    return panelDB

def anno_panel(geneList, db):
    dbInfo = []
    for gene in geneList:
        if gene in db.keys():
            dbInfo.append(db[gene])
        else:
            dbInfo.append('.')
    if all_same(dbInfo):
        dbStr = '.'
    else:
        dbStr = ','.join(dbInfo)
    return dbStr

# def high_fre_intron(txt):
#     re = []
#     for line in txt:
#         line = line.strip()
#         item = line.split("\t")
#         if ("0" in item[12]) or ("1" in item[12]):
#             dbscSNV_ADA_SCORE = float(item[12])
#             Func_refGene = item[5]   #### !="."
#             if dbscSNV_ADA_SCORE > 0.6 and Func_refGene == "intronic":
#                 re.append(line)
#     return re

def filter_MT(item):
    # try:
    if item != "chrMT":
        return True
    else:
        return False
    # except ValueError:
    #     return True

def contain_exon_Utr_spli(item):
    if ("ncRNA_exonic" not in item) and (("exonic") in item  or ("splicing" in item) or ("UTR" in item)):
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
# variables
chrPosdb, mutdb, genedb = {}, {}, {}
results = []
channel1 = []
result_part1 = []
input_for_intron = []
dbDir = '/mnt/workshop/xinchen.pan/pipeline/bio_informatics/wh_db'
omimDir = dbDir + '/omim_pheno_gene.txt'
eyeDir = dbDir + '/eye_panel.txt'
rpDir = dbDir + '/rplca_panel.txt'
fevrDir = dbDir + '/fevr_panel.txt'
endoDir = dbDir + '/endocrine_panel.txt'
nervDir = dbDir + '/nervous_panel.txt'
secondary_genes = ['BRCA1','BRCA2','TP53','STK11','MLH1','MSH2','MSH6','PMS2','APC','MUTYH','VHL','MEN1','RET','PTEN','RB1','SDHD','SDHAF2','SDHC','SDHB','TSC1','TSC2','WT1','NF2','COL3A1','FBN1','TGFBR1','TGFBR2','SMAD3','ACTA2','MYLK','MYH11','MYBPC3','MYH7','TNNT2','TNNI3','TPM1','MYL3','ACTC1','PRKAG2','GLA','MYL2','LMNA','RYR2','PKP2','DSP','DSC2','TMEM43','DSG2','KCNQ1','KCNH2','SCN5A','LDLR','APOB','PCSK9','RYR1','CACNA1S','BMPR1A','SMAD4','ATP7B','OTC']
predLines = [27, 30, 33, 36, 39, 42, 45, 48, 53, 56, 59, 67]

# code start
if __name__ == "__main__":
    fileName = os.path.basename(inputFile)
    rawFile = baseDir + 'RAW_VCF/' + fileName.split('anno.hg19_multianno')[0] + 'raw.vcf'
    output = baseDir + os.path.splitext(fileName)[0] + '.whanno.txt'
    print (maf, geneDB, args.eye_panel, args.endo_panel, args.nerv_panel)
    with open(inputFile) as f:
        oldLine = f.readline().strip()
        access_genedb()
        omimDataSet = access_panel(omimDir, 7)
        if args.fix_header:
            newLine = fix_header(oldLine) + '\tmut_dis\tsite_dis\tgene_dis\tomim\tpred_ratio\tpred_stats'
            print ('header fixed!')
        else:
            newLine = oldLine

        if args.eye_panel:
            eyeDataSet = access_panel(eyeDir, 0)
            rpDataSet = access_panel(rpDir, 0)
            fevrDataSet = access_panel(fevrDir, 0)
            newLine += '\teye\tRP/LCA\tFEVR'
            print ('eye_panel accessed!')

        if args.endo_panel:
            endoDataSet = access_panel(endoDir, 0)
            newLine += '\tendo'
            print ('endo_panel accessed!')

        if args.nerv_panel:
            nervDataSet = access_panel(nervDir, 0)
            newLine += '\tnerv'
            print ('nerv_panel accessed!')

        results.append(newLine)
        after_mutation_list = []
        for snpLine in f:
            snpLine = snpLine.strip()
            snp = snpLine.split('\t')
            gene = snp[6].split(',')
            chrSite = snp[0] + ':' + snp[1]
            mutation = chrSite + ':' + snp[3] + '-' + snp[4]

            if mutation not in mutdb.keys():
                snp.append('.')
            else:
                snp.append(mutdb[mutation])

            if chrSite not in chrPosdb.keys():
                snp.append('.')
            else:
                snp.append(chrPosdb[chrSite])

            # HGMD annotation
            gene_dis = []
            for g_idx in range(0, len(gene)):
                if (gene[g_idx] != '.') and (gene[g_idx] in genedb.keys()):
                    gene_dis.append(genedb[gene[g_idx]])
                else:
                    gene_dis.append('.')
            if all_same(gene_dis):
                geneDisStr = '.'
            else:
                geneDisStr = ','.join(gene_dis)
            snp.append(geneDisStr)

            # omim annotation
            omimAnno = anno_panel(gene, omimDataSet)
            snp.append(omimAnno)

            # count preds
            predHigh = 0
            predLow = 0
            for pred in predLines:
                if snp[pred] and (snp[pred] != '.'):
                    if (snp[pred] == 'D') or (snp[pred] == 'A') or (snp[pred] == 'H'):
                        predHigh += 1
                    else:
                        predLow += 1
            if predHigh > 0 or predLow > 0:
                predCounts =  predHigh + predLow
                predRatio = round((predHigh/predCounts)*100, 2)
                predStats = str(predRatio) + '%\t' + str(predHigh) + '|' + str(predCounts)
            else:
                predStats = '.\t.'
            snp.append(predStats)

            # internal panel annotation
            if args.eye_panel:
                eyeAnno = anno_panel(gene, eyeDataSet)
                rpAnno = anno_panel(gene, rpDataSet)
                fevrAnno = anno_panel(gene, fevrDataSet)
                eyeAnnoStr = eyeAnno + '\t' + rpAnno +'\t' + fevrAnno
                snp.append(eyeAnnoStr)

            if args.endo_panel:
                endoAnno = anno_panel(gene, endoDataSet)
                snp.append(endoAnno)

            if args.nerv_panel:
                nervAnno = anno_panel(gene, nervDataSet)
                snp.append(nervAnno)

            # secondary gene annotation
            for g in range(0, len(gene)):
                if gene[g] in secondary_genes:
                    gene[g] += '*'
            snp[6] = ','.join(gene)

            newSnpLine = '\t'.join(snp)
            input_for_intron.append(newSnpLine)

            if filter_maf(snp[10]) and filter_maf(snp[11]) and filter_maf(snp[19]) and filter_maf(snp[20]) and filter_maf(snp[21]) and filter_maf(snp[22]) and filter_MT(snp[0]):
                # newSnpLine = '\t'.join(snp)
                channel1.append(newSnpLine)
                if args.mu_ch:
                    father = snp[args.father]
                    mom = snp[args.mom]
                    son = snp[args.son]
                    snp_par = {}
                    snp_son = son.split(":")[0].split("/")
                    snp_par["fa"] = father.split(":")[0].split("/")
                    snp_par["mo"] = mom.split(":")[0].split("/")
                    if contain_exon_Utr_spli(snp[5]):
                        if ("." not in snp_son and  "." not in snp_par["fa"] and  "." not in snp_par["mo"]):
                            after_mutation = new_mutation_discover(newSnpLine,snp_son,snp_par["fa"],snp_par["mo"])
                            after_mutation_list.append(after_mutation)
        # print(after_mutation_list)
        if args.mu_ch:
            result_part1 = high_fre_intron(input_for_intron)
            results.extend(result_part1)
            result_part2 = compound_heterozygous_discover(after_mutation_list)
            results.extend(result_part2)
        else:
            results.extend(channel1)




    outResults = '\n'.join(results)
    with open(output, 'w', encoding='utf-16') as text_file:
        text_file.write(outResults)
