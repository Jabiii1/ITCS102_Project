def cc6():
    print("--------Conditional Statements--------")
    name = input("Enter your name: ")
    age = eval(input("Input your age: "))

    if age >= 1 and age < 7:
        print(f"Hello {name}, you are a Toddler!")

    elif age >= 8 and age < 13:
        print(f"Hello {name}, you are a Pre Teen!")

    elif age >= 14 and age < 18:
        print(f"Hello {name}, you are a Teenager!")

    elif age >= 19 and age < 31:
        print(f"Hello {name}, you are a Early Adulthood!")

    elif age >= 32 and age < 45:
        print(f"Hello {name}, you are a Mid Adulthood!")

    elif age >= 46 and age < 59:
        print(f"Hello {name}, you are a Post Adulthood!")

    elif age >= 60 and age <116:
        print(f"Hello {name}, you are a Senior!")

    else:
        print("Invalid Age") 
        print("Please Retype Again")