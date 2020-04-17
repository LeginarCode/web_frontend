class Defendant:
	def __init__(self, name, description, education, race, age, location, law_firm,  job, net_worth,
		size, previous_lawsuits, is_corporation, industry_field, num_employees, incorportation_date):

		self.name = name
		self.description = description
		self.education = education
		self.race = race
		self.age = age
		self.location = location
		self.law_firm = law_firm
		self.job = job
		self.net_worth = net_worth
		self.size = size
		self.previous_lawsuits = previous_lawsuits
		self.is_corporation = is_corporation
		self.industry_field = industry_field
		self.num_employees = num_employees
		self.incorportation_date = incorportation_date

	##### DFENDANT INFORMATION ########

	# Returns the name of the defendant. If single defendant, returns a single
	# valuee else a list of names
	def get_name(self):
		return self.name
	# Returns information about defendant
	def get_description(self):
		return self.description

	# Returns defendant education background.  If single defendant, returns a single 
	# valuee else a list of education backgrounds
	def get_education(self):
		return self.education

	# Returns defendant race. If single defendant, returns a single 
	# valuee else a list of races
	def get_race(self):
		return self.race

	# Returns defendant age. If single defendant, returns a single 
	# valuee else a list of ages
	def get_age(self):
		return self.age

	# Returns defendant location. If single defendant, returns a single 
	# valuee else a list of locations
	def get_location(self):
		return self.location

	# Returns defendant's law firm used
	def get_law_firm(self):
		return self.law_firm

	# Returns defendant's job. If single defendant, returns a single 
	# valuee else a list of jobs
	def get_job(self):
		return self.job

	# Returns defendant's net worth. If single defendant, returns a single 
	# valuee else a list of net worths
	def get_net_worth(self):
		return self.net_worth

	# SIze of the group -- for more than one defendant
	def get_size(self):
		return self.size

	# Returns if there have been cases before. Returns a list of Case objects. A bit trippy but essentially 
	# if this is the 3rd case, it returns a list of 2 cases and on the second case on the list this method returns a list with one 
	# and if it is the first one, there will be an empty list
	def get_previous_lawsuits(self):
		return self.previous_lawsuits

	# Is the defendant a large corporation or an individual entity
	def get_is_corporation(self):
		return self.is_corporation

	# This is onyl for companies
	def get_industry_field(self):
		return self.industry_field
	# Returns number of emplpyees in the commpany if a company
	def get_employees(self):
		return self.emplpyees

	# Returns whhen the company was made 
	def get_incorportation_date(self):
		return self.incorportation_date
