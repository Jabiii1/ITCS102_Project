for w in range(1,6):
    for x in range(6, w , -1):
        print(" ", end= " ")
    for y in range(1, w ,1):
        print("*", end= " ")
    for z in range(2, w, 1):
        print("*", end= " ")
    print()

for a in range(1,5):
    for b in range(-1, a , 1):
        print(" ", end= " ")
    for c in range(a, 4 ):
        print("*", end= " ")
    for d in range(a, 3):
        print("*", end= " ")
    print()