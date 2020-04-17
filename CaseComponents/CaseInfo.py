class CaseInfo:

	def __init__(self, result, initial_settlement_ask, final_settlement, taken_to_trial, start_date,
		end_date, judge_name, judge_description, case_description, num_defendants, num_plaintiffs,
		class_action):

		self.result = result 
		self.initial_settlement_ask = initial_settlement_ask
		self.final_settlement = final_settlement
		self.taken_to_trial = taken_to_trial
		self.start_date = start_date
		self.end_date = end_date
		self.judge_name = judge_name
		self.judge_description = judge_description
		self.case_description = case_description
		self.num_defendants = num_defendants
		self.num_plaintiffs = num_plaintiffs
		self.class_action = class_action


	 ##### CASE INFORMATION ########

	#returns who won -- plaintiff, defendant along with their name, or if it is ongoing or if it was dropped 
	def get_result(self):
		return self.result

	#Settlement ask info 
	def get_initial_settlement_ask(self):
		return self.initial_settlement_ask

	#Settlement ask info 
	def get_final_settlement(self):
		return self.final_settlement

	#trial or not 
	def get_taken_to_trial(self):
		return self.taken_to_trial

	#Start Date 
	def get_start_date(self):
		return self.start_date

	#End date
	def get_end_date(self):
		return self.end_date

	#judge name
	def get_judge_name(self):
		return self.judge_name

	#judge info 
	def get_judge_description(self):
		return self.judge_description

	 #judge info 
	def get_description(self):
		return self.case_description

	#num ddefendants 
	def get_num_defendants(self):
		return self.num_defendants

	#num plaintiffs 
	def get_num_plaintiffs(self):
		return self.num_plaintiffs

	def get_class_action(self):
		return self.class_action

		
