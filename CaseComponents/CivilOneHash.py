#This class is for cases from 1971 - 1987 to present day
class CivilOneHash:
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

    #Jurisdiction of the case
    jurisdiction = {
        "1" : "US government plaintiff",
        "2" : "US government defendant",
        "3" : "federal question",
        "4" : "diversity of citizenship",
        "5" : "local question",
    }

    #Origin of the case
    origin = {
        "1" : "original proceeding",
        "2" : "Removed from state court",
        "3" : "Remanded from appellate court ",
        "4" : "Reinstated or reopened ",
        "5" : "Transferred from another district ",
        "6" : "Multi-district litigation (Transfer by order of Panel for Multi-district Litigation)",
        "7" : "Appeal of magistrate judgment to a district judge (since SY81)",
        "8" : "2nd reopening (since SY83)",
        "9" : "3rd reopening (since SY83)",
        "10" : "4th reopening (since SY83)",
        "11" : "5th reopening (since SY83)",
        "12" : "6th reopening (since SY83)",
        "0" : "Missing",
        "-8": "Out-of-range"
    }

    #Residence ?


    #Is the case a class action
    class_action = {
        "0": "No allegation of class action made",
        "1": "Allegation of class action",
        "2": "Allegation dismissed",
        "3": "Allegation affirmed",
        "-8": "Out-of-range",
        "-9": "Data not collected (SY70 - SY72)"
    }

    #Demand Amount demanded in 1000s of dollars
    demand = {
        "9999": "coded for amounts greater than $9,999,000",
        "0": "missing (blank)"
    }

    #the method of disposition
    disposition_SY70_SY71= {
        "0": "Transferred to another district",
        "1": "Default judgment",
        "2": "Consent judgment",
        "3": "Dismissed for want of prosecution",
        "4": "Dismissed by action of parties",
        "5": "Remanded to state court",
        "6": "Judgment for plaintiff",
        "7": "Judgment for defendant",
        "8": "Judgment for both or other party",
        "9": "Outcome unknown"
    }

    #the method of disposition
    disposition_SY79_SY86= {
        "0": "Transferred to another district",
        "1": "Remanded",
        "2": "Dismissed for want of prosecution",
        "3": "Dismissed, discontinued, settled, withdrawn, etc.",
        "4": "Judgment on default",
        "5": "Judgment on consent",
        "6": "Judgment on motion before trial",
        "7": "Judgment on jury verdict",
        "8": "Judgment on directed verdict",
        "9": "Judgment on court trial",
        "10": "Judgment on other",
        "11": "Statistical closing (since SY84)"
    }

    disposition_SY86_SY87 = {
        "0": "Transferred to another district",
        "1": "Remanded to state court",
        "2": "Dismissed for want of prosecution",
        "3": "Dismissed for lack of jurisdiction",
        "4": "Judgment on default",
        "5": "Judgment on consent",
        "6": "Judgment on motion before trial",
        "7": "Judgment on jury verdict",
        "8": "Judgment on directed verdict",
        "9": "Judgment on court trial",
        "10": "Multi-district litigation transfer",
        "11": "Remanded to U.S. agency",
        "12": "Dismissed: voluntarily",
        "13": "Dismissed: settled",
        "14": "Dismissed: other",
        "15": "Judgment on award of arbitrator",
        "16": "Judgment on trial de novo after arbitration",
        "17": "Judgment on other",
        "18": "Statistical closing"
    }

    disposition_SY70_SY87 = {
        "-8": "Missing or out-of-range",
        "-9": "Data not collected (SY72 - SY78)"
    }

    #Procedural progress at termination.
    procedural_progress_SY70_SY75 = {
        "1": "No issue - no action",
        "2": "No issue - action",
        "3": "Issue, no pretrial - no action",
        "4": "Issue, no pretrial - action",
        "5": "Pretrial but no trial",
        "6": "Terminated during court trial",
        "7": "Terminated during jury trial",
        "8": "Judgment after court trial",
        "9": "Judgment after jury trial",
        "0": "Land condemnation cases"
    }

    procedural_progress_SY76_SY86 = {
        "1": "Before issue joined",
        "2": "After motion decided but before issue joined",
        "3": "Issue joined, no other court action",
        "4": "Issue joined, and after judgment of court on motion",
        "5": "Issue joined, and after pretrial conference but before trial",
        "6": "During court trial",
        "7": "During jury trial",
        "8": "After court trial",
        "9": "After jury trial",
        "0": "Other"
    }

    procedural_progress_S86_SY87 = {
        "1": "Before issue joined, no court action",
        "2": "Before issue joined, order entered",
        "3": "After issue joined, no court action",
        "4": "After issue joined, judgment on motion",
        "5": "After issue joined, pretrial conference held",
        "6": "After issue joined, during court trial",
        "7": "After issue joined, during jury trial",
        "8": "After issue joined, after court trial",
        "9": "After issue joined, after jury trial",
        "10": "After issue joined, other",
        "11": "Before issue joined, hearing held",
        "12": "Before issue joined, motion decided"
    }

    procedural_progress_S86_SY87 = {
        "-8": "Out-of-range (also missing in SY87)"
    }

    #The nature of the judgment for those actions disposed of by the entry of a final judgment.
    nature_of_judgment_SY70_SY71  = {
        "0": "No judgment entered",
        "1": "Money",
        "2": "Money and other",
        "3": "Injunction",
        "4": "Other, foreclosure, condemnation, HEW remand divorce"
    }

    nature_of_judgment_SY79_SY86  = {
        "0": "No monetary award",
        "1": "Monetary award only",
        "2": "Monetary award and other",
        "3": "Injunction",
        "4": "Other, foreclosure, condemnation, remand, etc.",
        "5": "Costs only"
    }

    nature_of_judgment_SY86_SY87  = {
        "0": "No monetary award",
        "1": "Monetary award only",
        "2": "Monetary award and other",
        "3": "Injunction",
        "4": "Forfeiture, foreclosure, condemnation, etc.",
        "5": "Costs only",
        "6": "Costs and attorney fees"
    }

    nature_of_judgment_SY70_SY87  = {
        "-8": "Missing or out-of-range",
        "-9": "Data not collected (SY72 - SY78)"
    }

    #The monetary judgment amount awarded (excluding costs) in thousands of dollars. (Value associated with nature o judgment codes 1 and 2.)
    amount_received = {
        "9999": "Coded for amounts greater than $9,999,000",
        "0": "Missing (blank)",
        "-8": "Out-of-range (contains alphas)"
    }

    # Identifies the party favored by the judgment of the court for actions disposed of by the entry of a final judgment.
    judgement_for = {
        "1": "Plaintiff",
        "2": "Defendant",
        "3": "Both",
        "4": "Unknown (or not applicable)",
        "-8": "Out-of-range",
        "-9": "Data not collected (SY70 - SY78)"
    }

    #Level of involvement of the U.S. magistrate. 
    magistrate_involvement = {
        "1": "Consent of parties to magistrate judgment with appeal directly to U.S. court of appeals",
        "2": "Consent of parties to magistrate judgment with appeal to U.S. district court",
        "3": "Special master reference",
        "4": "All pretrial matters, including dispositive motions",
        "5": "Report and recommendation on dispositive motions",
        "6": "All pretrial matters, except dispositive motions",
        "7": "Full pretrial/settlement conferences",
        "8": "Non-dispositive motions",
        "9": "No involvement of magistrate",
        "-8": "Out-of-range",
        "-9": "Data not collected (SY70 - SY80, SY86 - SY87)"
    }

    #Involvement in the case of persons other than judge or magistrate.
    other_involvement = {
        "1": "Arbitrator",
        "2": "Land commissioner",
        "3": "Special master (other than magistrate)",
        "4": "Other",
        "5": "No involvement other than judge or magistrate",
        "-8": "Out-of-range",
        "-9": "Data not collected (SY70 - SY80, SY86 - SY87)"
    }
