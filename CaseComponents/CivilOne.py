class CivilOne:

#Data from this link -- https://www.fjc.gov/research/idb/interactive/IDB-civil-1970-1987
#This class represents the cases from 1970 to 1987

    def __init__(self, CIRCUIT, DISTRICT, OFFICE, DOCKET, FILEDATE, JURIS, NOS, ORIGIN, RESIDENC, CLASSACT,
        TERMJUDG, FILEJUDG, DEMANDED, FILEMAG, COUNTY, CASENAME, TERMDATE, FDATEUSE, DISP, TERMMAG, PROCPROG, 
        NOJ, AMTREC, JUDGMENT, MAGISINV, OTHERINV, TDATEUSE, TAPEYEAR):

        self.CIRCUIT = CIRCUIT
        self.DISTRICT = DISTRICT
        self.OFFICE = OFFICE
        self.DOCKET = DOCKET
        self.FILEDATE = FILEDATE
        self.JURIS = JURIS
        self.NOS = NOS
        self.ORIGIN = ORIGIN
        self.RESIDENC = RESIDENC
        self.CLASSACT = CLASSACT
        self.TERMJUDG = TERMJUDG
        self.FILEJUDG = FILEJUDG
        self.DEMANDED = DEMANDED
        self.FILEMAG = FILEMAG
        self.COUNTY = COUNTY
        self.CASENAME = CASENAME
        self.TERMDATE = TERMDATE
        self.FDATEUSE = FDATEUSE
        self.DISP = DISP
        self.TERMMAG = TERMMAG
        self.PROCPROG = PROCPROG
        self.NOJ = NOJ
        self.AMTREC = AMTREC
        self.JUDGMENT = JUDGMENT
        self.MAGISINV = MAGISINV
        self.OTHERINV = OTHERINV
        self.TDATEUSE = TDATEUSE
        self.TAPEYEAR = TAPEYEAR

        
#Need to add some methods to update certain fields and use thhe map class to pass in the right values in 