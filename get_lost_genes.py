#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 15 13:48:55 2023

@author: justus
"""
import glob
import os
import re


files = glob.glob("*_finished/INPUT_GENOME/loss_summ_data.tsv") #Adjust path

os.system("mkdir lost_genes")
for x in range(len(files)):
    species = re.split("/",files[x])[-2] #Adjust name extraction
    species = re.split("_", species)[-1] #Adjust name extraction
    os.system("cat "+files[x]+" | grep \"GENE\" | grep \"L\" | awk \'$3==\"L\"\' |grep -v \"UL\" > lost_genes/"+species+"_lost.tsv")
