def cc14():

    number = True
    totalnumber = 0
    print("--------WHile Loops--------")
    while number == True:
        the_number = eval(input("Please enter a random number: "))
        
        if the_number == 0:
            print("The loop has been terminated.")
            print(f"The sum of all of the numbers that you've input is {totalnumber}")
            break
            number = False
            
        else:
            totalnumber += the_number
            continue
            