def act17():    
    
    column = eval(input("Please enter the number of Columns:"))
    for z in range(1,11):
        for x in range(1,column + 1):
            print(f"{z} x {x} = {z*x}", end= "\t")
        print()