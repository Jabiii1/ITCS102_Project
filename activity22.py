def activity4():
    
    num1 = eval(input("Enter your first number  -->"))
    num2 = eval(input("Enter your second number -->"))
    sum = num1 + num2
    print("The sum of " , num1 , "+" , num2 , "=" , sum)

def activity6():
    x = 5
    print(x)

    x = x + 10
    print(x)

    x = x + 15 
    print(x)

    x += 10
    print(x)

def activity7():
    #Introduction to Conditional Statements
    gold = 0
    miner = input("Hi, What is your name: ")
    isGold = input("is the mineral gold? ")
    if isGold.lower() == "yes" :
        gold += 1
        print(f"Hi {miner}, Your total number of gold is {gold}")
    else:
        print(f"Hi {miner}, Your total number of gold is {gold}")

def activity8():
    password = input("Enter your Password: ")
    if password.lower() == "secret":
        print("Access Granted")
        print("Enjoy using the System")
    elif password.lower() == "jabi":
        print("***Jabi Logged In***")
    else:
        print("Wrong Password please try again")
        print("Access Denied")

def activity9():
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

def activity10():
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

Continue = True

while Continue == True:
    ask = input("Please select the activity that you want to check: \n 4 = activity4 \n 6 = activity6 \n 7 = activity7 \n 8 = activity8 \n 9 = activity9 \n 10 = activity 10 \n:")

    if ask == "4":
        activity4()

    elif ask == "6":
        activity6()

    elif ask == "7":
        activity7()

    elif ask == "8":
        activity8()
    
    elif ask == "9":
        activity9()
    
    elif ask == "10":
        activity10()
        break
    else:
        print("Invalid Number")
        continue