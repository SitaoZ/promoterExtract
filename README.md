# Overview

The promoterExtract is python package for bioinformatics. 
The packages contains two subcommands.
The create subcommand is used for creating database and
extract subcomand is used for extracting promoter sequence.
Argument -l means the length of promoter, int type.
Argument -u utr5 after TSS, int type.
Argument -f reference genome fasta of a specific organism.
Argument -g annotation file including GTF and GFF.
Argument -o means output file path.

## Brief introduction of format package

1. **Install** <br>
    ```bash
    pip install promoterExtract
    # other
    git clone https://github.com/SitaoZ/promoterExtract.git
    cd promoterExtract; python setup.py install
    ```

2. **Usage** <br>
    ```bash
    which get_promoter
    get_promoter -h 
        Program:  get_promoter (pipeline for promoter extract)
        Version:  0.9.4
        Contact:  Sitao Zhu <zhusitao1990@163.com>
        Usage  :  get_promoter <command>
        Command: 
             create     create database for GTF or GFF
             extract    extract promoter for genome or gene
    get_promoter create -h 
        usage: get_promoter create [-h] [-g GFF]

        optional arguments:
            -h, --help         show this help message and exit
            -g GFF, --gff GFF  genome annotation file
    get_promoter extract -h 
        usage: get_promoter extract [-h] [-l LENGTH] [-u UTR_HEAD] [-f GENOME]
                                    [-o OUTPUT] [-v]

    optional arguments:
       -h, --help            show this help message and exit
       -l LENGTH, --length LENGTH
                             promoter length before TSS
       -g GFF,    --gff GFF
                             gff binary database created before
       -u UTR_HEAD, --utr_head UTR_HEAD
                             length after TSS
       -f GENOME, --genome GENOME
                             genome fasta
       -o OUTPUT, --output OUTPUT
                             output csv file path
       -v, --version         promoterExtract version
    ```

    ```bash
    # step 1 
    get_promoter create -g ath.gff3 
    # step 2
    get_promoter extract -l 200 -u 100 -f ath.fa -g gff.db -o promoter.csv
    ```
    
