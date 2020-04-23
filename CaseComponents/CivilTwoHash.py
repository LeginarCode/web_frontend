#This class is for cases from 1987 to present day
class CivilTwoHash:


    #This define the circuit code to the corrsponding circuit
    circuit = {
        "0" : "District of Columbia", 
        "6" : "Sixth Circuit",
        "1" : "First Circuit", 
        "7" : "Seventh Circuit",
        "2" : "Second Circuit", 
        "8" : "Eighth Circuit",
        "3" : "Third Circuit", 
        "9" : "Ninth Circuit",
        "4" : "Fourth Circuit", 
        "10" : "Tenth Circuit",
        "5" : "Fifth Circuit", 
        "11" : "Eleventh Circuit",
        "-8" : "Missing"
    }

    #This defines the district of the case
    district = {
        "00" : "Maine",
        "47" : "Ohio - Northern",
        "01" : "Massachusetts", 
        "48" : "Ohio - Southern",
        "02" : "New Hampshire", 
        "49" : "Tennessee - Eastern",
        "03" : "Rhode Island",
        "50" : "Tennessee - Middle",
        "04" : "Puerto Rico", 
        "51" : "Tennessee - Western",
        "05" : "Connecticut", 
        "52" : "Illinois - Northern",
        "06" : "New York - Northern", 
        "53" : "Illinois - Central",
        "07" : "New York - Eastern", 
        "54" : "Illinois - Southern",
        "08" : "New York - Southern", 
        "55" : "Indiana - Northern",
        "09" : "New York - Western", 
        "56" : "Indiana - Southern",
        "10" : "Vermont", 
        "57" : "Wisconsin - Eastern",
        "11" : "Delaware", 
        "58" : "Wisconsin - Western",
        "12" : "New Jersey", 
        "60" : "Arkansas - Eastern",
        "13" : "Pennsylvania - Eastern", 
        "61" : "Arkansas - Western",
        "14" : "Pennsylvania - Middle", 
        "62" : "Iowa - Northern",
        "15" : "Pennsylvania - Western", 
        "63" : "Iowa - Southern",
        "16" : "Maryland", 
        "64" : "Minnesota",
        "17" : "North Carolina - Eastern", 
        "65" : "Missouri - Eastern",
        "18" : "North Carolina - Middle", 
        "66" : "Missouri - Western",
        "19" : "North Carolina - Western", 
        "67" : "Nebraska",
        "20" : "South Carolina", 
        "68" : "North Dakota",
        "22" : "Virginia - Eastern", 
        "69" : "South Dakota",
        "23" : "Virginia - Western", 
        "7-" : "Alaska",
        "24" : "West Virginia - Northern", 
        "70" : "Arizona",
        "25" : "West Virginia - Southern", 
        "71" : "California - Northern",
        "26" : "Alabama - Northern", 
        "72" : "California - Eastern",
        "27" : "Alabama - Middle", 
        "73" : "California - Central",
        "28" : "Alabama - Southern", 
        "74" : "California - Southern",
        "29" : "Florida - Northern", 
        "75" : "Hawaii",
        "3A" : "Florida - Middle", 
        "76" : "Idaho",
        "3C" : "Florida - Southern", 
        "77" : "Montana",
        "3E" : "Georgia - Northern", 
        "78" : "Nevada",
        "3G" : "Georgia - Middle", 
        "79" : "Oregon",
        "3J" : "Georgia - Southern", 
        "80" : "Washington - Eastern",
        "3L" : "Louisiana - Eastern", 
        "81" : "Washington - Western",
        "3N" : "Louisiana - Middle", 
        "82" : "Colorado",
        "36" : "Louisiana - Western", 
        "83" : "Kansas",
        "37" : "Mississippi - Northern", 
        "84" : "New Mexico",
        "38" : "Mississippi - Southern", 
        "85" : "Oklahoma - Northern",
        "39" : "Texas - Northern",
        "86" : "Oklahoma - Eastern",
        "40" : "Texas - Eastern",
        "87" : "Oklahoma - Western",
        "41" : "Texas - Southern", 
        "88" : "Utah",
        "42" : "Texas - Western", 
        "89" : "Wyoming",
        "43" : "Kentucky - Eastern", 
        "90" : "District of Columbia",
        "44" : "Kentucky - Western", 
        "91" : "Virgin Islands",
        "45" : "Michigan - Eastern", 
        "93" : "Guam",
        "46" : "Michigan - Western", 
        "94" : "Northern Mariana Islands",
        "-8" : "Missing",
    }

    #Origin of the case
    origin = {
        "1" : "original proceeding",
        "2" : "removed (began in the state court, removed to the district court)",
        "3" : "remanded for further action (removal from court of appeals)",
        "4" : "reinstated/reopened (previously opened and closed, reopened for additional action)",
        "5" : "transferred from another district(pursuant to 28 USC 1404)",
        "6" : "multi district litigation (cases transferred to this district by an order entered by Judicial Panel on Multi District Litigation pursuant to 28 USC 1407)",
        "7" : "appeal to a district judge of a magistrate judge's decision",
        "8" : "second reopen",
        "9" : "third reopen",
        "10" : "fourth reopen",
        "11" : "fifth reopen",
        "12" : "sixth reopen",
        "13" : "multi district litigation originating in the district (valid beginning July 1, 2016)",
    }

    #Jurisdiction of the case
    jurisdiction = {
        "1" : "US government plaintiff",
        "2" : "US government defendant",
        "3" : "federal question",
        "4" : "diversity of citizenship",
        "5" : "local question",
    }

    #Nature of the suit
    nature_of_suit = {
        "110" : "INSURANCE",
        "120" : "MARINE CONTRACT ACTIONS",
        "130" : "MILLER ACT",
        "140" : "NEGOTIABLE INSTRUMENTS",
        "150" : "OVERPAYMENTS & ENFORCEMENT OF JUDGMENTS",
        "151" : "OVERPAYMENTS UNDER THE MEDICARE ACT",
        "152" : "RECOVERY OF DEFAULTED STUDENT LOANS",
        "153" : "RECOVERY OF OVERPAYMENTS OF VET BENEFITS",
        "160" : "STOCKHOLDER'S SUITS",
        "190" : "OTHER CONTRACT ACTIONS",
        "195" : "CONTRACT PRODUCT LIABILITY",
        "196" : "CONTRACT FRANCHISE",
        "210" : "LAND CONDEMNATION",
        "220" : "FORECLOSURE",
        "230" : "RENT, LEASE, EJECTMENT",
        "240" : "TORTS TO LAND",
        "245" : "TORT PRODUCT LIABILITY",
        "290" : "OTHER REAL PROPERTY ACTIONS",
        "310" : "AIRPLANE PERSONAL INJURY",
        "315" : "AIRPLANE PRODUCT LIABILITY",
        "320" : "ASSAULT, LIBEL, AND SLANDER",
        "330" : "FEDERAL EMPLOYERS' LIABILITY",
        "340" : "MARINE PERSONAL INJURY",
        "345" : "MARINE - PRODUCT LIABILITY",
        "350" : "MOTOR VEHICLE PERSONAL INJURY",
        "355" : "MOTOR VEHICLE PRODUCT LIABILITY",
        "360" : "OTHER PERSONAL INJURY",
        "362" : "MEDICAL MALPRACTICE",
        "365" : "PERSONAL INJURY -PRODUCT LIABILITY",
        "367" : "HEALTH CARE / PHARM",
        "368" : "ASBESTOS PERSONAL INJURY - PROD.LIAB.",
        "370" : "OTHER FRAUD",
        "371" : "TRUTH IN LENDING",
        "375" : "FALSE CLAIMS ACT",
        "380" : "OTHER PERSONAL PROPERTY DAMAGE",
        "385" : "PROPERTY DAMAGE -PRODUCT LIABILTY",
        "400" : "STATE RE-APPORTIONMENT",
        "410" : "ANTITRUST",
        "422" : "BANKRUPTCY APPEALS RULE 28 USC 158",
        "423" : "BANKRUPTCY WITHDRAWAL 28 USC 157",
        "430" : "BANKS AND BANKING",
        "440" : "OTHER CIVIL RIGHTS",
        "441" : "CIVIL RIGHTS VOTING",
        "442" : "CIVIL RIGHTS JOBS",
        "443" : "CIVIL RIGHTS ACCOMMODATIONS",
        "444" : "CIVIL RIGHTS WELFARE",
        "445" : "CIVIL RIGHTS ADA EMPLOYMENT",
        "446" : "CIVIL RIGHTS ADA OTHER",
        "448" : "EDUCATION",
        "450" : "INTERSTATE COMMERCE",
        "460" : "DEPORTATION",
        "462" : "NATURALIZATION, PETITION FOR HEARING OF DENIAL",
        "463" : "HABEAS CORPUS - ALIEN DETAINEE",
        "465" : "OTHER IMMIGRATION ACTIONS",
        "470" : "CIVIL (RICO)",
        "480" : "CONSUMER CREDIT",
        "490" : "CABLE/SATELLITE TV",
        "510" : "PRISONER PETITIONS -VACATE SENTENCE",
        "530" : "PRISONER PETITIONS -HABEAS CORPUS",
        "535" : "HABEAS CORPUS: DEATH PENALTY",
        "540" : "PRISONER PETITIONS -MANDAMUS AND OTHER",
        "550" : "PRISONER - CIVIL RIGHTS",
        "555" : "PRISONER - PRISON CONDITION",
        "560" : "CIVIL DETAINEE",
        "610" : "AGRICULTURAL ACTS",
        "620" : "FOOD AND DRUG ACTS",
        "625" : "DRUG RELATED SEIZURE OF PROPERTY",
        "630" : " LIQUOR LAWS",
        "640" : "RAILROAD AND TRUCKS",
        "650" : "AIRLINE REGULATIONS",
        "660" : "OCCUPATIONAL SAFETY/HEALTH",
        "690" : "OTHER FORFEITURE AND PENALTY SUITS",
        "710" : "FAIR LABOR STANDARDS ACT",
        "720" : "LABOR/MANAGEMENT RELATIONS ACT",
        "730" : "LABOR/MANAGEMENT REPORT & DISCLOSURE",
        "740" : "RAILWAY LABOR ACT",
        "751" : "FAMILY AND MEDICAL LEAVE ACT",
        "790" : "OTHER LABOR LITIGATION",
        "791" : "EMPLOYEE RETIREMENT INCOME SECURITY ACT",
        "810" : "SELECTIVE SERVICE",
        "820" : "COPYRIGHT",
        "830" : "PATENT",
        "840" : "TRADEMARK",
        "850" : "SECURITIES, COMMODITIES, EXCHANGE",
        "860" : "SOCIAL SECURITY",
        "861" : "HIA (1395 FF)/ MEDICARE",
        "862" : "BLACK LUNG",
        "863" : "D.I.W.C./D.I.W.W.",
        "864" : "S.S.I.D.",
        "865" : "R.S.I.",
        "870" : "TAX SUITS",
        "871" : "IRS 3RD PARTY SUITS 26 USC 7609",
        "875" : "CUSTOMER CHALLENGE 12 USC 3410",
        "890" : "OTHER STATUTORY ACTIONS",
        "891" : "AGRICULTURAL ACTS",
        "892" : "ECONOMIC STABILIZATION ACT",
        "893" : "ENVIRONMENTAL MATTERS",
        "894" : "ENERGY ALLOCATION ACT",
        "895" : "FREEDOM OF INFORMATION ACT OF 1974",
        "896" : "ARBITRATION",
        "899" : "ADMINISTRATIVE PROCEDURE ACT/REVIEW OR APPEAL OF AGENCY DECISION",
        "900" : "APPEAL OF FEE -EQUAL ACCESS TO JUSTICE",
        "910" : "DOMESTIC RELATIONS",
        "920" : "INSANITY",
        "930" : "PROBATE",
        "940" : "SUBSTITUTE TRUSTEE",
        "950" : "CONSTITUTIONALITY OF STATE STATUTES",
        "990" : "OTHER",
        "992" : "LOCAL JURISDICTIONAL APPEAL",
        "999" : "MISCELLANEOUS",

    }

    #Reseidence of the peerson in question. The data will be 2 digits and will need to be isolaed and hashed
    residence = {
        "1" : "Citizen of this State",
        "2" : "Citizen of another State",
        "3" : "Citizen or Subject of a Foreign Country",
        "4" : "Incorporated or principal place of business in this State",
        "5" : "Incorporated or principal place of business in another State",
        "6" : "Foreign Nation",
    }

    #Data about jury demands of both parties
    jury_demand = {
        "B" : "Both plaintiff and defendant demand jury",
        "D" : "Defendant demands jury",
        "P" : "Plaintiff demands jury",
        "N" : "Neither plaintiff nor defendant demands jury",
        "-8" : "missing",
    }

    #Method of participation at arbitation if any
    arbitration_at_filing = {
        "M" : "mandatory",
        "V" : "voluntary",
        "E" : "exempt",
        "Y" : "yes, but type unknown",
        "-8" : "missing",
    }

    #Is the case a class action
    class_action = {
        "1" : "Class action",
        "0" : "Not a Class Action",
        "-8" : "missing",
    }

    #Description of wheether a class action was alowed
    term_class_action = {
        "2" : "denied",
        "3" : "granted",
        "-8" : "missing",
    }

    #Point till where the case went on till before it was dismissed
    procedural_progress = {
    #  a) before issue joined
        "1" : "no court action",
        "2" : "order entered",
        "11" : "hearing held",
        "12" : "order decided",
    #    b) after issued joined
        "3" : "no court action",
        "4" : "judgement on motion",
        "5" : "pretrial conference held",
        "6" : "during court trial",
        "7" : "during jury trial",
        "8" : "after court trial",
        "9" : "after jury trial",
        "10" : "other",
        "13" : "request for trial de novo after arbitration",
    }

    
    #Mehod in which the casee was dismissed
    disposition = {
        #Cases transferred or remanded:
        "0" : "transfer to another district",
        "1" : "remanded to state court",
        "10" : "multi district litigation transfer",
        "11" : "remanded to U.S. Agency",
        #Dismissals:
        "2" : "want of prosecution",
        "3" : "lack of jurisdiction",
        "12" : "voluntarily",
        "13" : "settled",
        "14" : "other",
        #Judgment on:
        "4" : "default",
        "5" : "consent",
        "6" : "motion before trial",
        "7" : "jury verdict",
        "8" : "directed verdict",
        "9" : "court trial",
        "15" : "award of arbitrator",
        "16" : "stayed pending bankruptcy",
        "17" : "other",
        "18" : "statistical closing",
        "19" : "appeal affirmed (magistrate judge)",
        "20" : "appeal denied (magistrate judge)",
        "-8" : "missing",
    }

    #Nature the judgement -- aka what happened
    nature_of_judgement = {
        "0" : "no monetary award",
        "1" : "monetary award only",
        "2" : "monetary award and other",
        "3" : "injunction",
        "4" : "forfeiture/foreclosure/condemnation, etc.",
        "5" : "costs only",
        "6" : "costs and attorney fees",
    }

    #Case dismissed ot decided in favor of
    judgement = {
        "1" : "plaintiff",
        "2" : "defendant",
        "3" : "both",
        "4" : "unknown",
        "0" : "missing",
        "-8" : "missing",
    }

    #Arbritaration in thee terminationstage
    arbitration_at_termination = {
        "M" : "mandatory",
        "V" : "voluntary",
        "E" : "exempt",
        "-8" : "missing",
    }


    pro_se = {
        "0" : "no Pro Se plaintiffs or defendants",
        "1" : "Pro Se plaintiffs, but no Pro Se defendants",
        "2" : "Pro Se defendants, but no Pro Se plaintiffs",
        "3" : "both Pro Se plaintiffs & defendants",
        "-8" : "missing",
    }

    fee_status = {
        "FP" : "Informa Pauperis (IFP cases)",
        "-8" : "not IFP cases",
    }


    status_code = {
        "S" : "pending record",
        "L" : "terminated record",
    }

