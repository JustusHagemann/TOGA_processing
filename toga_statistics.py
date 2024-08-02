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

search_strings = ["Extracted","After filters","reference genes on graph","query genes on graph","Graph contains","Detected"]
                  
files = glob.glob("*toga.txt")
frame=pd.DataFrame(columns=["sample","extracted_query_transcripts","filtered_query_transcripts","reference_genes_on_graph","query_genes_on_graph","graph_connections","detected_orthology_component","one2one","one2zero","many2one","one2many","many2many"])

for x in range(len(files)):
    sample = re.split("_",files[x])[0]
    os.system("cat "+files[x]+"| tail -n 18 > tmp.txt")
    
    
    os.system("grep \"query transcripts\" tmp.txt > tmp1")
    with open("tmp1") as f:
        for line in f:
            testx=line
            extracted_query_transcripts=re.split(" ",testx)[1]
            
    os.system("grep \"transcripts left\" tmp.txt > tmp1")
    with open("tmp1") as f:
        for line in f:
            testx=line
            filtered_query_transcripts=re.split(" ",testx)[2]
    
    os.system("grep \"reference genes on graph\" tmp.txt > tmp1")
    with open("tmp1") as f:
        for line in f:
            testx=line
            reference_gene_on_graph=re.split(" ",testx)[1]    

    os.system("grep \"query genes on graph\" tmp.txt > tmp1")
    with open("tmp1") as f:
        for line in f:
            testx=line
            query_gene_on_graph=re.split(" ",testx)[1]    

    os.system("grep \"connections\" tmp.txt > tmp1")
    with open("tmp1") as f:
        for line in f:
            testx=line
            graph_connections=re.split(" ",testx)[2] 
            
    os.system("grep \"orthology components\" tmp.txt > tmp1")
    with open("tmp1") as f:
        for line in f:
            testx=line
            detected_orthology_components=re.split(" ",testx)[1] 
    
    os.system("grep \"one2one\" tmp.txt > tmp1")
    with open("tmp1") as f:
        for line in f:
            test=line
            one2one=re.split(" ",test)[-1][:-1]
    os.system("grep \"one2zero\" tmp.txt > tmp1")
    with open("tmp1") as f:
        for line in f:
            test=line
            one2zero=re.split(" ",test)[-1][:-1]
    os.system("grep \"many2one\" tmp.txt > tmp1")
    with open("tmp1") as f:
        for line in f:
            test=line
            many2one=re.split(" ",test)[-1][:-1]
    os.system("grep \"one2many\" tmp.txt > tmp1")
    with open("tmp1") as f:
        for line in f:
            test=line
            one2many=re.split(" ",test)[-1][:-1]
    os.system("grep \"many2many\" tmp.txt > tmp1")
    with open("tmp1") as f:
        for line in f:
            test=line
            many2many=re.split(" ",test)[-1][:-1]
    tmp_dic={"sample":sample,"extracted_query_transcripts":extracted_query_transcripts,"filtered_query_transcripts":filtered_query_transcripts,"reference_genes_on_graph":reference_gene_on_graph,"query_genes_on_graph":query_gene_on_graph,"graph_connections":graph_connections,"detected_orthology_component":detected_orthology_components,"one2one":one2one,"one2zero":one2zero,"many2one":many2one,"one2many":one2many,"many2many":many2many}
    frame=frame.append(tmp_dic,ignore_index=True)
os.system("rm tmp1")
os.system("rm tmp.txt")
frame.to_csv("total_annotation_summary.csv")
            

            
    # with open("tmp.txt") as f:
    #     for line in f:
            
    #         for y in range(len(search_strings)):
    #             os.system