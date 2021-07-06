# Overview

The promoterExtract is python package for bioinformatics. 
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
    get_promoter -l 200 -u 100 -f ath.fa -g ath.gff3 -o promoter.csv
    ```
