import argparse

class Parameter():
    def __init__(self):
        self._parser = argparse.ArgumentParser()
    
    def parse(self):
        parser = argparse.ArgumentParser()
        self._parser.add_argument('-l', '--length', type=int, help='promoter length before TSS')
        self._parser.add_argument('-u', '--utr_head', type=int, help='length after TSS')
        self._parser.add_argument('-f', '--genome', type=str, help='genome fasta')
        self._parser.add_argument('-g', '--gff', type=str, help='genome annotation file')
        self._parser.add_argument('-o', '--output', type=str, help = 'output csv file path')
        self._parser.add_argument('-v', '--version', help = 'promoterExtract version information', action = "store_true")

        args = self._parser.parse_args()

        if args.version:
            print("promorerExtract version 0.9.3")
            exit(1)

        self.length = args.length
        self.utr_head = args.utr_head
        self.genome = args.genome
        self.gff = args.gff
        self.output = args.output
        
        if self.length is None:
            raise  Exception("Error: promoter length is required")
        elif self.utr_head is None:
            raise Exception("Error: utr length is required")
        elif self.genome is None:
            raise Exception("Error: genome fasta is required")
        elif self.gff is None:
            raise Exception("Error: gff is required")
        elif self.output is None:
            raise Exception("Error: output is required")

        return self
