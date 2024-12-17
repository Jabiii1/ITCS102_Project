def act13():
    print("--------For Loop--------")
    for x in range(1,0, -1):
        num = eval(input("Enter a number: "))
        factor = num * num
        print(f"The factorial of {num} is {factor}")
