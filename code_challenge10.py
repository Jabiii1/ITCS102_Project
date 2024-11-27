
for x in range(1, 6):
    for a in range(6,x, -1):
        print(" " ,end= " ")
    for s in range(0, x ):
        print("*" , end= " ")
    for d in range(0, x):
        print("*" , end= " ")
    print() 

for y in range(1, 6):
    for f in range(0,y):
        print(" " ,end= " ")
    for g in range(y,6 , 1):
        print("*" , end= " ")
    for h in range(y, 6, 1):
        print("*" , end= " ")
    print()
