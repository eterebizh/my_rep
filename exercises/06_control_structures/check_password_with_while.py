

username = input ("Please enter a username: ")
password = input ("Please enter a password: ")

password_correct = False

while not password_correct:
	if len(password) < 8:
		print ("Password length should be at least 8 characters")
		password_correct = False
		password = input ("Please enter a password: ")
	elif username in password: 
		print ("Password can't contain a username")
		password_correct = False
		password = input ("Please enter a password: ")
	else:
		print ("Username/Password has been set")
		password_correct = True