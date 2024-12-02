def act19():
    countinue = True

    while countinue == True:
        name = input("Enter your name: ")

        if name.lower() == "stop":
            print("Loop Terminated")

            break
            countinue = false
