#!/bin/bash
cat ../orthology_classification.tsv | grep "one2one" > one2one_orthologs.tsv
cut -f4 one2one_orthologs.tsv > one2oneIDs
seqtk subseq ../nucleotide.fasta one2oneIDs > test_nt
awk '/^>/ {P=index($0,"REFERENCE")==0} {if(P) print} ' test_nt > OUTPUT_one2one_NT.fasta
