# import re
# result = re.compile(r'\w*  Nakamoto')
# txt = 'Satoshi Nakamoto Alice NakamotoRoboCop Nakamoto  satoshi Nakamoto Mr. Nakamoto Nakamoto Satoshi nakamoto'
# result.findall(txt).group()

# /opt/seqtools/gatk/gatk4/gatk --java-options -XX:ParallelGCThreads=1 HaplotypeCaller \
#     -R /opt/seqtools/gatk/ucsc.hg19.fasta \
#     -I $results/recal_bam/$1.recal.dedup.sorted.bam \
#     -L $bed \
#     -ip 100 \
#     -ERC GVCF \
#     -O $results/GVCF/$1.g.vcf.gz 2>$log/$1.call_gvcf.log
# GATK=/opt/seqtools/gatk/gatk4/gatk
#   6 GATK_options="-XX:ParallelGCThreads=1"
import os
myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
for filename in myFiles:
    print(os.path.join('C:/Users/asweigart', filename))
