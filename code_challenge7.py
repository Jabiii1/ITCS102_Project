def cc7():
    
    #Grocery
    name = input("Good Day Costumer!! Please enter your name: ")
    buy = input(f"\nHi {name}, do you want to buy a grocery? (yes/no) ")

    if buy.lower() == "yes":
        item = input("\nWhat do you want to buy: ")
        itemPrice = eval(input(f"Price of the {item}: "))
        cusmoney = eval(input("Amount Given : "))
        age = eval(input("Please enter your age: "))
        discount = round((itemPrice * 0.052), 2)
        discountPrice = round((itemPrice - discount), 2)
        tax = round((itemPrice * 0.123),2)
        taxPrice = round((itemPrice + tax),2)
        
        if age >= 60:
            print(f"\nHi {name}, you purchased a {item} with a price of (₱{itemPrice}) plus a 5.2% discount (₱{discount}) to your total purchase. ")
            print(f"\nMoney Given: {cusmoney}")
            print(f"Total Purchased: {round((itemPrice - discount), 2)}")
            print(f"Change: {round((cusmoney - discountPrice), 2)}")
            print(f"\nThank you {name} for shopping with us. Please come by again next time!")
    
        elif age >= 18:
            print(f"\nHi {name}, you purchased a {item} with a price of (₱{itemPrice}) plus a 12.5% tax (₱{tax}) to your total purchase. ")
            print(f"\nMoney Given: {cusmoney}")
            print(f"Total Purchased: {round((itemPrice + tax), 2)}")
            print(f"Change: {round((cusmoney - taxPrice), 2)}")
            print(f"\nThank you {name} for shopping with us. Please come by again next time!")
            
        elif age >= 1:
            print(f"\nHi {name}, you purchased a {item} with a total price of (₱{itemPrice}). ")
            print(f"\nMoney Given: {cusmoney}")
            print(f"Total Purchased: {itemPrice}")
            print(f"Change: {round(cusmoney - itemPrice)}")
            print(f"\nThank you {name} for shopping with us. Please come by again next time!")
            
        else:
            print(f"\nThank you {name} for stopping by!")