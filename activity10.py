name = input("Enter  your name: ")
isStudent = input("Are you a student in DLL (yes/no) :")

if isStudent .lower() == "yes":
	yearlevel = input("What year are you currently enrolled ?\nS - Freshmen \nS - Sophomore \nJ - Junior \nR- Senior \nPlease input your answer here: ")

	if yearlevel.lower() == "f" :
		print(f"Hi {name}, Freshmen, Welcome to DLL! ")
	elif yearlevel.lower() == "s": 
		print(f"Hi {name}, Sophomore, Welcome to DLL! ")
	elif yearlevel.lower() == "j":
		print(f"Hi {name}, Junior, Welcome to DLL!")
	elif yearlevel.lower() == "r" :
		print(f"Hi {name}, Senior, Welcome to DLL!")
else:
	print(f"Hi {name}, Thank you for using our system!")
