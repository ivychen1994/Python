def make_pizza(size,*toppings):
	"""打印顧客點的所有配料"""
	print("\nMaking a "+str(size)+
			"-inch pizza with the following tippings:")
	for topping in toppings:
		print("- "+topping)
