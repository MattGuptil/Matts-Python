class person(object):


	#The "self" has to be first parameter
	def __init__(self, lastname_arg, firstname_arg,age_arg=None):

		# two underscores __ will hide it
		self.lastname = lastname_arg
		self.firstname = firstname_arg
		self.age = age_arg

	def output_fullname(self):
		fullName = self.lastname + " " + self.lastname

	def change_lastname(self,new_name):
		pswd = input("Enter Pass: ")
		if pswd == "1":
			self.__lastname = new_name

	@property
	def w(self):
		return self._weight

	# or @w.setter
	def set_weight(self,input):
		self.__weight = input