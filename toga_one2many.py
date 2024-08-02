#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 18:26:13 2022

@author: justus
"""
import glob
import os
import re
import pandas as pd



genomes = glob.glob("*/orthology_classification.tsv")

#### extract all possible one2many othologs

for x in range(len(genomes)):
    os.system("grep \"one2many\" "+genomes[x]+" | cut -f1  | sort| uniq >> tmp")
os.system("cat tmp | sort| uniq > tmp2")    

os.system("rm tmp")

frame = pd.read_csv("tmp2",names=["ref_genes"])



global_dataframe =pd.DataFrame()
for x in range(len(genomes)):
    genome = re.split("/",genomes[x])[0]

    os.system("grep \"one2many\" "+genomes[x]+" | cut -f1  | sort| uniq > tmp")
    query_frame = pd.read_csv("tmp",names=["query_genes"])
    query_list=query_frame["query_genes"].values.tolist()
    ref_list=frame["ref_genes"].values.tolist()
    temp_dic={}
    for y in range(len(ref_list)):
        if ref_list[y] in query_list:
            temp_dic[ref_list[y]]=1
            
        else:
            temp_dic[ref_list[y]]=0
           
    
    global_dataframe=global_dataframe.append(pd.DataFrame(temp_dic,index=[genome]))
global_dataframe=global_dataframe.transpose()
global_dataframe.to_csv("toga_gene_gain.csv")

    
os.system("rm tmp2")
os.system("rm tmp")