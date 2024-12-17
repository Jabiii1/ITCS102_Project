def cc8():
	print("--------Conditional Statements--------")
	prelim = eval(input("Please input your pre-lim grade : "))
	midterm = eval(input("Please input your mid-termgrade : "))
	semifinal = eval(input("Please input your semi-final grade : "))
	final = eval(input("Please input your final grade: "))
	quiz = eval(input("Please input your quiz grade : "))
	project = eval(input("Please input your project grade : "))

	total_grade = (prelim*0.15) + (midterm*0.15) + (semifinal*0.15) + (final*0.15) + (quiz*0.25) + (project*0.15)

	if total_grade > 98:
		print("Invalid Grade please try again")

	elif total_grade >= 75:
		print ("\n\nYou Passed!!!")
		print ("Congratulation!!!")

	else:
		print("\n\nYou Failed")
		print("Better Luck next Time!")