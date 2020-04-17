from CaseInfo import CaseInfo
from Defendant import Defendant
from Plaintiff import Plaintiff


class CaseObject:

	def __init__(self, plaintiff, defendant, case_info):
		self.case_info = case_info
		self.plaintiff = plaintiff
		self.defendant = defendant
		
	##### CASE INFORMATION ########
	#returns who won -- plaintiff, defendant along with their name, or if it is ongoing or if it was dropped 
	def get_case_info_result(self):
		return self.case_info.get_result()

	#Settlement ask info 
	def get_case_info_initial_settlement_ask(self):
		return self.case_info.get_initial_settlement_ask()

	#Settlement ask info 
	def get_case_info_final_settlement(self):
		return self.case_info.get_final_settlement()

	#trial or not 
	def get_case_info_taken_to_trial(self):
		return self.case_info.get_taken_to_trial()

	#Start Date 
	def get_case_info_start_date(self):
		return self.case_info.get_start_date()

	#End date
	def get_case_info_end_date(self):
		return self.case_info.get_end_date()

	#Settlement ask info 
	def get_case_info_end_date(self):
		return self.case_info.get_end_date()

	#judge name
	def get_case_info_judge_name(self):
		return self.case_info.get_judge_name()

	#judge info 
	def get_case_info_judge_description(self):
		return self.case_info.get_judge_description()

	 #judge info 
	def get_case_info_description(self):
		return self.case_info.get_description()

	#defendantt numser info 
	def get_case_info_multiple_defendants(self):
		return self.case_info.get_multiple_defendants()

	#plaintiff number info 
	def get_case_info_multiple_defendants(self):
		return self.case_info.get_multiple_paintiffs()


	def get_case_info_class_action(self):
		return self.case_info.get_class_action()


	##### PLAINTIFF INFORMATION ########

	#Returns the name of the plaintiff. If single plaintiff, returns a single 
	#valuee else a list of names
	def get_plaintiff_name(self):
		return self.plaintiff.get_name()

	#Returns information about plaintiff
	def get_plaintiff_description(self):
		return self.plaintiff.get_description()

	#Returns plaintiff education background.  If single plaintiff, returns a single 
	#valuee else a list of education backgrounds
	def get_plaintiff_education(self):
		return self.plaintiff.get_education()

	#Returns plaintiff race. If single plaintiff, returns a single 
	#valuee else a list of races
	def get_plaintiff_race(self):
		return self.plaintiff.get_race()

	#Returns plaintiff age. If single plaintiff, returns a single 
	#valuee else a list of ages
	def get_plaintiff_age(self):
		return self.plaintiff.get_age()

	#Returns plaintiff location. If single plaintiff, returns a single 
	#valuee else a list of locations
	def get_plaintiff_location(self):
		return self.plaintiff.get_location()

	#Returns plaintiff's law firm used
	def get_plaintiff_law_firm(self):
		return self.plaintiff.get_law_firm()

	#Returns plaintiff's job. If single plaintiff, returns a single 
	#valuee else a list of jobs
	def get_plaintiff_job(self):
		return self.plaintiff.get_job()

	#Returns plaintiff's net worth. If single plaintiff, returns a single 
	#valuee else a list of net worths
	def get_plaintiff_net_worth(self):
		return self.plaintiff.get_net_worth()

	#SIze of the group -- for more than one plaintiff
	def get_plaintiff_size(self):
		return self.plaintiff.get_size()

	#Returns if there have been cases before. Returns a list of Case objects. A bit trippy but essentially 
	#if this is the 3rd case, it returns a list of 2 cases and on the second case on the list this method returns a list with one 
	#and if it is the first one, there will be an empty list
	def get_plaintiff_previous_lawsuits(self):
		return self.plaintiff.get_previous_lawsuits()

	#Is the plaintiff a large corporation or an individual entity
	def get_plaintiff_is_corporation(self):
		return self.plaintiff.get_is_corporation()

	#This is onyl for companies
	def get_plaintiff_industry_field(self):
		return self.plaintiff.get_industry_field()

	#Returns number of emplpyees in the commpany if a company
	def get_plaintiff_employees(self):
		return self.plaintiff.get_num_employees()

	#Returns whhen the company was made 
	def get_plaintiff_incorportation_date(self):
		return self.plaintiff.get_incorportation_date()



	##### DFENDANT INFORMATION ########

	#Returns the name of the defendant. If single defendant, returns a single 
	#valuee else a list of names
	def get_defendant_name(self):
		return self.defendant.get_name()

	#Returns information about defendant
	def get_defendant_description(self):
		return self.defendant.get_description()

	#Returns defendant education background.  If single defendant, returns a single 
	#valuee else a list of education backgrounds
	def get_defendant_education(self):
		return self.defendant.get_education()

	#Returns defendant race. If single defendant, returns a single 
	#valuee else a list of races
	def get_defendant_race(self):
		return self.defendant.get_race()

	#Returns defendant age. If single defendant, returns a single 
	#valuee else a list of ages
	def get_defendant_age(self):
		return self.defendant.get_age()

	#Returns defendant location. If single defendant, returns a single 
	#valuee else a list of locations
	def get_defendant_location(self):
		return self.defendant.get_location()

	#Returns defendant's law firm used
	def get_defendant_law_firm(self):
		return self.defendant.get_law_firm()

	#Returns defendant's job. If single defendant, returns a single 
	#valuee else a list of jobs
	def get_defendant_job(self):
		return self.defendant.get_job()

	#Returns defendant's net worth. If single defendant, returns a single 
	#valuee else a list of net worths
	def get_defendant_net_worth(self):
		return self.defendant.get_net_worth()

	#SIze of the group -- for more than one defendant
	def get_defendant_size(self):
		return self.defendant.get_size()

	#Returns if there have been cases before. Returns a list of Case objects. A bit trippy but essentially 
	#if this is the 3rd case, it returns a list of 2 cases and on the second case on the list this method returns a list with one 
	#and if it is the first one, there will be an empty list
	def get_defendant_previous_lawsuits(self):
		return self.defendant.get_previous_lawsuits()

	#Is the defendant a large corporation or an individual entity
	def get_defendant_is_corporation(self):
		return self.defendant.get_is_corporation()

	#This is onyl for companies
	def get_defendant_industry_field(self):
		return self.defendant.get_industry_field()

	#Returns number of emplpyees in the commpany if a company
	def get_defendant_employees(self):
		return self.defendant.get_num_employees()

	#Returns whhen the company was made 
	def get_defendant_incorportation_date(self):
		return self.defendant.get_incorportation_date()









