def add_ints(a,b):
	if type(a) is not int or type(b) is not int:
		raise TypeError("add_ints can't take non-integer args")
	return a + b


if __name__ == "__main__":
	print(add_ints(1,2))
	try:
		print(add_ints("hello",2))
	except TypeError:
		print("Please Enter int")

