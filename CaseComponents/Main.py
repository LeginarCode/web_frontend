from CaseInfo import CaseInfo
from Defendant import Defendant
from Plaintiff import Plaintiff
from CaseObject import CaseObject
import datetime


#Sample Case Object made below. Data can be parsed this way with a loop and can keep all information in this.

#CONSTRUCTOR INFO
#def __init__(name, description, education, race, age, location, law_firm,  job, net_worth,
#		size, previous_lawsuits, is_corporation, industry_field, num_employees, incorportation_date):


#while (data): 
# populate objects and create 

#
# 
# 
# find websites to scrape data and pass it into these fields in a loop
# 
# 
#  
PlaintiffTest = Plaintiff("Gary", "Stout young man", "Yale Educated", "Black", 25, "New York", 
	"Jake and Jake", "teacher", 800000, None, None, False, None, None, None)
DefendantTest = Defendant("John", "Tall middle aged man", "Harvard Educated", "white", 35, "Chicago", 
	"Litt and Litt", "teacher", 1200000, None, None, False, None, None, None)

#CONSTRUCTOR INFO
# def __init__(result, initial_settlement_ask, final_settlement, taken_to_trial, start_date,
#   	end_date, judge_name, judge_description, case_description, num_defendants, num_plaintiffs,
#    	class_action):
CaseInfoTest = CaseInfo("Gary Win", 200000, 200000, True, datetime.datetime(2020, 5, 17), datetime.datetime.now(), 
	"Smith", "Old white judge, Georgetown educated liberal judge", "Intellectual Property theft", 1, 1, False)



CaseObjectTest = CaseObject(PlaintiffTest, DefendantTest, CaseInfoTest)


print(PlaintiffTest.get_name())
