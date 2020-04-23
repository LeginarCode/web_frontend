import sys

sys.path.append('/CaseComponents')

import pandas as pd 
from CaseComponents import *

def main():
    df = pd.read_sas('CaseData/cv70_0.sas7bdat')
    for (index, fields) in df.iterrows():
        #TODO: send fields data through hash map and use that as parameters
        obj = CivilOne(fields.CIRCUIT, fields.DISTRICT, fields.OFFICE, fields.DOCKET, fields.FILEDATE, fields.JURIS, 
                        fields.NOS, fields.ORIGIN, fields.RESIDENC, fields.CLASSACT, fields.TERMJUDG, fields.FILEJUDG,
                        fields.DEMANDED, fields.FILEMAG, fields.COUNTY, fields.CASENAME, fields.TERMDATE, fields.FDATEUSE, 
                        fields.DISP, fields.TERMMAG, fields.PROCPROG, fields.NOJ, fields.AMTREC, fields.JUDGMENT, fields.MAGISINV, 
                        fields.OTHERINV, fields.TDATEUSE, fields.TAPEYEAR)
        break

    print('District: {}'.format(obj.DISTRICT))
    print('Demand: {}'.format(obj.DEMANDED))   




if __name__ == "__main__":
    main()