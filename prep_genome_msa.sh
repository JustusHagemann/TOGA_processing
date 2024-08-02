#!/bin/bash

chainToAxt humanENS.CAS29752.allfilled.chain.gz ../humanENS.2bit ../../../../genomes/2bit/CAS29752.2bit Ftest.axt
axtToMaf Ftest.axt humanENS.chrom.sizes CAS29752.chrom.sizes -qPrefix=CAS29752 -tPrefix=human CAS29752.maf
