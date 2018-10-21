def sumFile():
	fName = input("Enter File Name: ")
	myF = open(fName)
	myVals = myF.readlines()
	a = 0
	for i in myVals:

		try:
			x = int(i)
		except ValueError:
			print("Not an Int")
			break

		i = int(i) 	
	
		a = a+i

	return a

if __name__ == "__main__":
	print(sumFile())
	
