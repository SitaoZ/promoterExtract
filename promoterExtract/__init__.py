from promoterExtract.promoter import get_promoter
from promoterExtract.parameter import Parameter

def get_prom():
    para = Parameter().parse()
    print("running...")
    promoter_seq = get_promoter(para.length, para.utr_head, para.genome, para.gff, para.output)
    print("writing output...")
    promoter_seq.to_csv('%s'%(para.output), index=False)
    print("writing output finished.")

