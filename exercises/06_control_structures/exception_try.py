
while True: 
		a = input ("Enter first number: ")
		b = input ("Enter second number: ")

		if a.isdigit() and b.isdigit(): 
			if int(b) == 0:
				print ("Can't divide by zero")
			else: 
				print ("Result is ", int(a)/int(b))
				break
		else:
			print ("Only numbers are allowed, please try again")