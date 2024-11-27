
age = eval(input("Enter your age: "))

if age > 115:
	print("Invalid Age.")
	print("Please Retype your Age.")

elif age >= 1 and age < 7:
	print("You're  age is at Toddler.")

elif age >= 8 and age < 13:
	print("You're age is at Pre Teen.")

elif age >= 14 and age < 18:
	print("You're age is at Teenager")

elif age >= 19 and age < 31:
	print("You're age is at Early Adulthood")

elif age >= 32 and age < 45:
	print("You're age is at Mid Adulthood")

elif age >= 46 and age < 59:
	print ("Your age is at Port Adulthood ")

elif age >= 60 and age < 100:
	print("Your age is at Senior's age")

