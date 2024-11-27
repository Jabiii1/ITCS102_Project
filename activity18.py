triangle = eval(input("Please input the number of the triangle: "))

for x in range(1,7):
    for a in range(triangle):
        for b in range(1,x+1):
            print("&", end=" ")
        for c in range(7, x, -1):
            print(" ", end=" ")
        print(" ", end=" ")
    print()