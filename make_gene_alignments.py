#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 09:39:01 2022

@author: justus
"""


import os
import re
from Bio import SeqIO
import glob

fasta_files = glob.glob("*.fasta")

os.system("rm -r gene_alignments")
os.system("mkdir gene_alignments")
for i in range(len(fasta_files)):
    sample_ID = re.split("_",fasta_files[i])[0]
    with open(fasta_files[i],"r") as handle:
        for record in SeqIO.parse(handle, "fasta"):
            ref_id = re.split("\.",record.id)[0]
            record.id = sample_ID #####!!!!!!!!!! CHECK out what happens when more than one gene is assocaiated to the same referecne scaffold!!!!!
            record.description = ""
            with open("gene_alignments/"+ref_id+".fasta","a") as new:
                SeqIO.write(record,new,"fasta")

###### Remove alignments with less entries than len(fasta_files)
number_of_occurence =[]
alignment_files = glob.glob("gene_alignments/*.fasta")
for x in range(len(alignment_files)):
    records = list(SeqIO.parse(alignment_files[x],"fasta"))
    number_of_occurence.append(len(records))
    if len(records) < len(fasta_files):
        os.system("rm "+alignment_files[x])          
for x in range(len(fasta_files)):
  
    print(str(number_of_occurence.count(x+1))+" alignments with "+str(x+1)+" entries")
    
###### calculate alignments
os.system("rm -r mafft_alignments")
os.system("mkdir mafft_alignments")
alignment_files = glob.glob("gene_alignments/*.fasta")
for x in range(len(alignment_files)):
    name = re.split("/",re.split("\.", alignment_files[x])[0])[-1]      
    os.system("mafft "+alignment_files[x]+" > mafft_alignments/"+name+".mafft")

# ####################################################
# record_ids =[]
# with open(fasta_files[0],"r") as handle:
#     for record in SeqIO.parse(handle,"fasta"):
#         ref_id = re.split("\.",record.id)[0]
#         record_ids.append(ref_id)
#         # if record.id == sequence_to_extract:
#         #     with open("extracted_result","w") as new:
#         #         SeqIO.write(record,new,"fasta")
                
# record_ids = sorted(record_ids)
# print(len(record_ids))
