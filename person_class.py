class person(object):


	#The "self" has to be first parameter
	def __init__(self, lastname_arg, firstname_arg,age_arg=None):

		self.lastname = lastname_arg
		self.firstname = firstname_arg
		self.age = age_arg

	def output_fullname(self):
		fullName = self.lastname + " " + self.lastname