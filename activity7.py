#Introduction to Conditional Statements
gold = 0
miner = input("Hi, What is your name: ")

isGold = input("is the mineral gold? ")

if isGold.lower() == "yes" :
	gold += 1
	print(f"Hi {miner}, Your total number of gold is {gold}")
else:
	print(f"Hi {miner}, Your total number of gold is {gold}")