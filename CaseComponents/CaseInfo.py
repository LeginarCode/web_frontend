class CaseInfo:

    def __init__(self, result, initial_settlement_ask, final_settlement, taken_to_trial, start_date,
    	end_date, judge_name, judge_description, case_description, multiple_defendants, multiple_plaintiffs,
    	class_action):

    	self.result = result 
    	self.initial_settlement_ask = initial_settlement_ask
    	self.final_settlement = final_settlement
    	self.taken_to_trial = taken_to_trial
    	self.start_date = start_date
    	self.end_date = end_date
    	self.judge_name = judge_name
    	self.judge_description = judge_description
    	self.case_get_description = case_description
    	self.multiple_defendants = multiple_defendants
    	self.multiple_plaintiffs = multiple_plaintiffs
    	self.class_action = class_action


     ##### CASE INFORMATION ########

    #returns who won -- plaintiff, defendant along with their name, or if it is ongoing or if it was dropped 
    def get_result():
    	return result

    #Settlement ask info 
    def get_initial_settlement_ask():
    	return initial_settlement_ask

    #Settlement ask info 
    def get_final_settlement():
    	return final_settlement

    #trial or not 
    def get_taken_to_trial():
    	return taken_to_trial

    #Start Date 
    def get_start_date():
    	return start_date

    #End date
    def get_end_date():
    	return end_date

    #judge name
    def get_judge_name():
    	return judge_name

    #judge info 
    def get_judge_description():
    	return judge_description

     #judge info 
    def get_description():
    	return case_description

    #num ddefendants 
    def get_multiple_defendants():
    	return multiple_defendants

    #num plaintiffs 
    def get_multiple_plaintiffs():
    	return multiple_plaintiffs

    def get_class_action():
    	return class_action

    	
