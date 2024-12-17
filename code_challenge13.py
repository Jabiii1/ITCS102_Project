def cc13():
    print("--------For Loops--------")
    for x in range(1,6):
        for a in range(6, x , -1):
            print(" ", end= " ")
        for b in range(x , 0 , -1):
            print(b, end= " ")
        for c in range(2, x+1):
            print(c, end= " ")
        print()

    for y in range(4,0, -1):
        for d in range(6, y ,-1):
            print(" ", end= " ")
        for e in range(y, 0 , -1):
            print(e, end=" ")
        for f in range(2, y +1):
            print(f, end= " ")
        print()