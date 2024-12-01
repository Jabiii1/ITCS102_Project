def act21():
    count = True
    num = 0

    while count == True:
        name = input("Please enter a name ---> ")
        
        if name.lower() == "stop":
            print("The loop has now stopped")
            print(f"You have entered {num} number")
            break
            count = False
        else:
            num += 1