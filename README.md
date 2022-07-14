# Overview

The promoterExtract is python package for nucleotide manipulation 
in bioinformatics. The package contains two subcommands including 
create and extract. The create subcommand is used for creating 
database and extract subcomand is used for extracting promoter sequence.
Both two subcomand is executed through get_promoter command in command line.
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
    get_promoter create -h 
    get_promoter extract -h 
    ```

    ```bash
    # step 1 
    get_promoter create -g ath.gff3 
    # step 2
    get_promoter extract -l 200 -u 100 -f ath.fa -g gff.db -o promoter.csv
    ```
    
