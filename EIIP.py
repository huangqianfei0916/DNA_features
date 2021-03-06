import numpy as np
import  pandas as pd
def EIIP(fastas, **kw):

    AA = 'ACGT'

    EIIP_dict ={
        'A': 0.1260,
        'C': 0.1340,
        'G': 0.0806,
        'T': 0.1335,
        '-': 0,

    }

    encodings = []


    for i in fastas:
        sequence = i.strip()
        code = []
        for aa in sequence:
            code.append(EIIP_dict.get(aa, 0))
        encodings.append(code)
    # np.savetxt("eiip", encodings)
    pd.DataFrame(encodings).to_csv("EIIP.csv", header=None, index=False)
    return np.array(encodings)
