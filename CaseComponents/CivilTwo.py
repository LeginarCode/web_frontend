#https://www.fjc.gov/research/idb/interactive/IDB-civil-since-1988 is the link with the variables. Read it 

class CivilTwo:

#Data from this link -- https://www.fjc.gov/research/idb/interactive/IDB-civil-since-1988 
#This class represents the cases from 1987 to present

    def __init__(self, CIRCUIT, DISTRICT, OFFICE, DOCKET, ORIGIN, FILEDATE, FDATEUSE,  JURIS, NOS, TITLE, SECTION, SUBSECTION, RESIDENC, JURY, 
        CLASSACT, DEMANDED, FILEJUDG, FILEMAG, COUNTY, ARBIT, MDLDOCK, PLT, DEF, TRANSDAT, TRANSOFF, TRANSDOC, TRANSORG, TERMDATE, TDATEUSE, TRCLACT, 
        TERMJUDG, TERMMAG, PROCPROG, DISP, NOJ, AMTREC, JUDGEMENT, DJOINED, PRETRIAL, TRIBEGAN, TRIALEND, TRMARB, PROSE, IFP, STATUSCD, TAPEYEAR):

        self.CIRCUIT = CIRCUIT
        self.DISTRICT = DISTRICT
        self.OFFICE = OFFICE
        self.DOCKET = DOCKET
        self.ORIGIN = ORIGIN
        self.FILEDATE = FILEDATE
        self.FDATEUSE = FDATEUSE
        self.JURIS = JURIS
        self.NOS = NOS
        self.TITLE = TITLE
        self.SECTION = SECTION
        self.SUBSECTION = SUBSECTION
        self.RESIDENC = RESIDENC
        self.JURY = JURY
        self.CLASSACT = CLASSACT
        self.DEMANDED = DEMANDED
        self.FILEJUDG = FILEJUDG
        self.FILEMAG = FILEMAG
        self.COUNTY = COUNTY
        self.ARBIT = ARBIT
        self.MDLDOCK = MDLDOCK
        self.PLT = PLT
        self.DEF = DEF
        self.TRANSDAT = TRANSDAT
        self.TRANSOFF = TRANSOFF
        self.TRANSDOC = TRANSDOC
        self.TRANSORG = TRANSORG
        self.TERMDATE = TERMDATE
        self.TDATEUSE = TDATEUSE
        self.TRCLACT = TRCLACT
        self.TERMJUDG = TERMJUDG
        self.TERMMAG = TERMMAG
        self.PROPROG = PROCPROG
        self.DISP = DISP
        self.NOJ = NOJ
        self.AMTREC = AMTREC 
        self.JUDGEMENT = JUDGEMENT
        self.DJOINED = DJOINED
        self.PRETRIAL = PRETRIAL
        self.TRIBEGAN = TRIBEGAN
        self.TRIALEND = TRIALEND 
        self.TRMARB = TRMARB
        self.PROSE = PROSE 
        self.IFP = IFP
        self.STATUSCD = STATUSCD
        self.TAPEYEAR = TAPEYEAR

        
#Need to add some methods to update certain fields and use thhe map class to pass in the right values in 