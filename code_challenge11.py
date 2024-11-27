for x in range(0,7):
    for y in range(7 - x):
        print(" " , end= " ")
    for z in range(1, x + 1):
        print("  *", end = " ")
    print()

for a in range(1,7):
    for b in range(1, a + 1):
        print("  ", end = " ")
    for c in range( 6, a, -1):
        print("   *", end = " ")
    print()  