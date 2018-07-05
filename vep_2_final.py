import re
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-r', '--RAWVCF', required=True, help='raw.vcf')
parser.add_argument('-v', '--VEP', required=True, help='vep.anno')
parser.add_argument('-d', '--dir', required=True, help='dir locate')
parser.add_argument('-t', '--type', required=True, help='brca or 50gene')
args = parser.parse_args()

In_VCF = args.dir+"/results/RAW_VCF/"+args.RAWVCF
In_VEP = args.dir+"/results/"+args.VEP
ReName = args.dir+"/results/"+args.RAWVCF+'.final.out'
RE =  open(ReName,"w")
sys.stdout = RE





if args.type == "50gene":
    sys.stdout.write("Chrom"+"\t"+"locate"+"\t"+"Gene_Name"+"\t"+"Exon|Intron"+"\t"+"dbSNP_ID"+"\t"+"Codon_Change"+"\t"+"ref"+"\t"+"alt1"+"\t"+"alt2"+"\t"+"alt3"+"\t"+"ref_fre"+"\t"+"Alt_fre1"+"\t"+"alt_fre2"+"\t"+"alt_fre3"+"\t"+"AA_Change"+"\t"+"Eff_Effect"+"\n")
elif args.type == "brca":
    sys.stdout.write("gene\tlocate\tbase_change\tid\texac_af\texac_af_eas\tHGMD_dna\tclnhgvs\tvar_type\tgene_id\thgvs_c\thgvs_p\texon_intron\tsite_explain\tgeno\tdepth\tfrequence\n")
gene_list=['NM_005157', 'NM_005163', 'NM_004304', 'NM_001127511', 'NM_000051', 'NM_004333', 'NM_004360', 'NM_000077', 'NM_005211', 'NM_001904', 'NM_005228', 'NM_004448', 'NM_005235', 'NM_004456', 'NM_033632', 'NM_023110', 'NM_000141', 'NM_000142', 'NM_004119', 'NM_002067', 'NM_002072', 'NM_000516', 'NM_000545', 'NM_005343', 'NM_005896', 'NM_002168', 'NM_004972', 'NM_000215', 'NM_002253', 'NM_000222', 'NM_033360', 'NM_001127500', 'NM_000249', 'NM_005373', 'NM_017617', 'NM_002520', 'NM_002524', 'NM_006206', 'NM_006218', 'NM_000314', 'NM_002834', 'NM_000321', 'NM_020975', 'NM_005359', 'NM_003073', 'NM_005631', 'NM_005417', 'NM_000455', 'NM_000546', 'NM_000551']
rs_list =  {'NM_000927': ['rs1045642', 'rs1128503'], 'NM_000771': ['rs1057910'], 'NM_000106': ['rs1065852', 'rs28371725', 'rs3892097'], 'NM_001072': ['rs10929302', 'rs3064744'], 'NM_202001': ['rs11615'], 'NM_000400': ['rs13181'], 'NM_000852': ['rs1695'], 'NM_000903': ['rs1800566'], 'NM_005957': ['rs1801131', 'rs1801133'], 'NM_004628': ['rs2228001'], 'NM_006297': ['rs25487'], 'NM_017460': ['rs28371759'], 'NM_000110': ['rs3918290', 'rs67376798'], 'NM_000463': ['rs4148323'], 'NM_000769': ['rs4244285'], 'NM_000103': ['rs4646', 'rs6493497', 'rs7176005'], 'NM_001785': ['rs60369023'], 'NM_001012716': ['rs45445694'], 'NM_001071': ['rs45445694']}
dic = {}
# NM_005957 NM_006297 NM_000106
with open(In_VCF,"r") as RAWVCF:
    for line in RAWVCF:
        # line = line.strip()
        if "##" and "#" not in line:
            pos = str(line.split()[1])
            ref = line.split()[3]
            alt = line.split()[4]
            if line.split()[3] == "_":
                pos = str(line.split()[1]+1)
            if len(line.split()[3]) > 1:
                pos = str(int(line.split()[1]) + 1)
                ref = line.split()[3][1:]
                alt = line.split()[4][1:]
            key = line.split()[0]+pos+"\\"+ref+alt
            total_depth = int(line.split()[9].split(":")[2])
            all_alt_depth = line.split()[9].split(":")[3].split(",")
            leng = len(all_alt_depth)
            depth_ref = int(all_alt_depth[0])
            depth_alt1 = int(all_alt_depth[1])
            fre_ref = depth_ref/total_depth
            fre_alt1 = depth_alt1/total_depth
            if "0/1" in line.split()[9]:
                geno = "heterozygosis"
            elif "1/1" in line.split()[9]:
                geno = "homozygosis"
            if leng >3:
                depth_alt3 = int(all_alt_depth[3])
                fre_alt3 = depth_alt3/total_depth
            elif leng >2:
                depth_alt2 = int(all_alt_depth[2])
                fre_alt2 = depth_alt2/total_depth
            else:
                depth_alt3 = ''
                fre_alt3 = ''
                depth_alt2 = ''
                fre_alt2 = ''
            if args.type == "50gene":
                dic[key]= str(depth_ref)+"\t"+str(depth_alt1)+"\t"+str(depth_alt2)+"\t"+str(depth_alt3)+"\t"+str(fre_ref)+"\t"+str(fre_alt1)+"\t"+str(fre_alt2)+"\t"+str(fre_alt3)
            elif args.type == "brca":
                dic[key]= geno+"\t"+ line.split()[9]+"\t"+str(fre_alt1)


with open(In_VEP,"r") as VEP:
    for line in VEP:
        if "##" not in line and "#" not in line:
            Chr = "chr"+line.split()[0].split("_")[0]
            pos2 = line.split()[0].split("_")[1]
            ref2 = line.split()[0].split("_")[2].split("/")[0]
            alt2 = line.split()[0].split("_")[2].split("/")[1]
            key2 = Chr+pos2+"\\"+ref2+alt2
            NM = line.split()[32].split(":")[0].split(".")[0]
            if 'c.' in line.split()[32]:
                coden_change = line.split()[32].split(":")[1]
            else:
                coden_change =''
            exon_intron = line.split()[30]+"|"+line.split()[31]
            if "rs" in line.split()[12]:
                if len(line.split()[12])>1:
                    rs = line.split()[12].split(",")[0]
                else:
                    rs =line.split()[12]
            else:
                rs = ''
            if "p." in line.split()[33]:
                if "%" in line.split()[33]:
                    AA = str(line.split()[33].split(":")[1])
                    middle = str(AA[2:5])
                    AA_total = line.split()[33].replace("%3D",middle)
                    AA = AA.replace("%3D",middle)
                else:
                    AA_total = line.split()[33]
                    AA = line.split()[33].split(":")[1]
            else:
                AA_total = ''
                AA = ''
            if args.type == "50gene":
                if key2 in dic.keys() and ((NM in gene_list) or (NM in rs_list.keys() and rs in rs_list[NM]) or (line.split()[32] == 'NM_006182.3:c.392C>G')):
                    sys.stdout.write(Chr+"\t"+pos2+"\t"+line.split()[17]+"\t"+exon_intron+"\t"+line.split()[12]+"\t"+coden_change+"\t"+dic[key2]+"\t"+AA+"\t"+line.split()[6]+"\n")
            elif args.type == "brca":
                if key2 in dic.keys() and NM in ['NM_000059','NM_007294']:
                    typ = ref2+">"+alt2
                    if 'BRCA2' in line.split()[17]:
                        gene_id="ENSG00000139618"
                    elif "BRCA1" in line.split()[17]:
                        gene_id="ENSG00000012048"
                    sys.stdout.write(line.split()[17]+"\t"+pos2+"\t"+typ+"\t"+line.split()[12]+"\t"+line.split()[44]+"\t"+line.split()[49]+"\t"+line.split()[32]+"\t"+AA_total+"\t"+line.split()[6]+"\t"+gene_id+"\t"+coden_change+"\t"+AA+"\t"+exon_intron+"\t"+line.split()[35]+"\t"+dic[key2]+"\n")