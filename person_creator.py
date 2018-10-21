from person_class import person

def create_person():
	x = person("Smith", "Robert")
	return x

if __name__ == '__main__':
	my_person = create_person()
	print(my_person.lastname)
	print(my_person.output_fullname())
	print(my_person.age)