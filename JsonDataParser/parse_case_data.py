import sys

sys.path.append('/CaseComponents')

import pandas as pd 
from CaseComponents import *
import json

def main():
    df = pd.read_sas('CaseData/CivilCases/CaseData70-87/1972.sas7bdat')
    for (index, fields) in df.iterrows():
        #print(index)
        #print(fields)
        data_dict = fields.to_dict()
        json_data = json.dumps(data_dict, indent=4, sort_keys=True, default=str)
        #print(json_data)
        file = open("1972.json", "a")
        file.write(json_data)
        file.write(",")
        file.write("\n")
       # HttpResponse(json_data, content_type='application/json')
        #TODO: send fields data through hash map and use that as parameters
        # obj = CivilOne(fields.CIRCUIT, fields.DISTRICT, fields.OFFICE, fields.DOCKET, fields.FILEDATE, fields.JURIS, 
        #                 fields.NOS, fields.ORIGIN, fields.RESIDENC, fields.CLASSACT, fields.TERMJUDG, fields.FILEJUDG,
        #                 fields.DEMANDED, fields.FILEMAG, fields.COUNTY, fields.CASENAME, fields.TERMDATE, fields.FDATEUSE, 
        #                 fields.DISP, fields.TERMMAG, fields.PROCPROG, fields.NOJ, fields.AMTREC, fields.JUDGMENT, fields.MAGISINV, 
        #                 fields.OTHERINV, fields.TDATEUSE, fields.TAPEYEAR)
        

  #  print('District: {}'.format(obj.DISTRICT))
  #  print('Demand: {}'.format(obj.DEMANDED))   




if __name__ == "__main__":
    main()