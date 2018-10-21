shop_list = ['apple', 'pear', 'bananna']


def is_in_list(myShop):
	

	for item in shop_list:
		stripShop = myShop.strip()
		if item == stripShop:
			return True

	return False








