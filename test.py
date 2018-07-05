import re
import sys
with open(sys.argv[1],"w") as RE:
    sys.stdout = RE
gene_list=["NM_005157","NM_005163","NM_004304","NM_001127511","NM_000051","NM_004333","NM_004360","NM_000077","NM_005211","NM_001904","NM_005228","NM_004448","NM_005235","NM_004456","NM_033632","NM_023110","NM_000141","NM_000142","NM_004119","NM_002067","NM_002072","NM_000516","NM_000545","NM_005343","NM_005896","NM_002168","NM_004972","NM_000215","NM_002253","NM_000222","NM_033360","NM_001127500","NM_000249","NM_002834","NM_017617","NM_002520","NM_002524","NM_006206","NM_006218","NM_000314","NM_002834","NM_000321","NM_020975","NM_005359","NM_003073","NM_005631","NM_005417","NM_000455","NM_000546","NM_000551","NM_000927","NM_000771","NM_000106","NM_001072","NM_000927","NM_202001","NM_000400","NM_000852","NM_000903","NM_005957","NM_005957","NM_004628","NM_006297","NM_000106","NM_017460","NM_001072","NM_000106","NM_000110","NM_000463","NM_000769","NM_000103","NM_001785","NM_000103","NM_000110","NM_000103","NM_001012716","NM_001071","NM_006182","NM_005373"]

dic = {}
lis = []
with open(sys.argv[2],"r") as RAWVCF:
    for line in RAWVCF:
        # line = line.strip()
        if "##" and "#" not in line:
            pos = line.split()[1]
            ref = line.split()[3]
            alt = line.split()[4]
            if line.split()[3] == "_":
                pos = line.split()[1]+1
            if len(line.split()[3]) > 1:
                pos = line.split()[1]+1
                ref = line.split()[3][1:]
                alt = line.split()[4][1:]
            key = line.split()[0]+pos+"\\"+ref+alt
            total_depth = line.split()[9].split(":")[2]
            all_alt_depth = line.split()[9].split(":")[3].split(",")
            depth_ref = all_alt_depth[0]
            depth_alt1 = all_alt_depth[1]
            depth_alt2 = all_alt_depth[2]
            depth_alt3 = all_alt_depth[3]
            fre_ref = depth_ref/total_depth
            fre_alt1 = depth_alt1/total_depth
            fre_alt2 = depth_alt2/total_depth
            fre_alt3 = depth_alt3/total_depth
            dic[key]= depth_ref+"\t"+depth_alt1+"\t"+"\t"+depth_alt2+"\t"+depth_alt3+"\t"+fre_ref+"\t"+fre_alt1+"\t"+fre_alt2+"\t"+fre_alt3

sys.stdout.write("Chrom"+"\t"+"locate"+"\t"+"Gene_Name"+"\t"+"Exon|Intron"+"\t"+"dbSNP_ID"+"\t"+"Codon_Change"+"\t"+"ref"+"\t"+"alt1"+"\t"+"alt2"+"\t"+"alt3"+"\t"+"ref_fre"+"\t"+"Alt_fre1"+"\t"+"alt_fre2"+"\t"+"alt_fre3"+"\t"+"AA_Change"+"\t"+"Eff_Effect")
with open(sys.argv[3],"r") as VEP:
    for line in VEP:
        if "##" and "#" not in line:
            Chr = "chr"+line.split()[0].split("_")[0]
            pos2 = line.split()[0].split("_")[1]
            ref2 = line.split()[0].split("_")[2].split("/")[0]
            alt2 = line.split()[0].split("_")[2].split("/")[1]
            key2 = Chr+pos2+"\\"+ref2+alt2
            NM = line.split()[32].split(":")[0].split(".")[0]
            coden_change = line.split()[32].split(":")[1]
            exon_intron = line.split()[30]+"|"+line.split()[31]
            AA = line.split()[33].split(":")[1][2:]
            middle = AA[1][:3]
            if "%" in line.split()[33]:
                cg = re.compile(r'[%3D]')
                AA1 = cg.sub(middle,AA)
            if key2 in dic.keys() and NM in gene_list:
                sys.stdout.write(Chr+"\t"+pos2+"\t"+line.split()[17]+"\t"+exon_intron+"\t"+line.split()[12]+"\t"+coden_change+"\t"+dic[key2]+"\t"+AA1+"\t"+line.split()[6])