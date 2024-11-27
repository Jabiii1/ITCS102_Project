for x in range(1 , 6):
    for a in range(6 , x , -1):
        print(" ", end = " ")
    for b in range(0 , x):
        print("*", end = " ")
    for c in range(0 , x):
        print("*", end = " ")
    print()

for y in range(1 , 6):
    for d in range(0 , y):
        print(" ", end = " ")
    for e in range(6, y , -1):
        print("*", end = " ")
    for f in range(6 , y , -1):
        print("*", end =" ")
    print()