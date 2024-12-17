def act8():
	print("--------Conditional Statements--------")
	password = input("Enter your Password: ")

	if password.lower() == "secret":
		print("Access Granted")
		print("Enjoy using the System")

	elif password.lower() == "jabi":
		print("***Jabi Logged In***")

	else:
		print("Wrong Password please try again")
		print("Access Denied")