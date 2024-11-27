name = input("Introduce your self\n")
parse = name.split(" ")
foundPattern = False
x = 0

for item in parse:
    if foundPattern is True:
        print(f"Hello {item}")
        break
    if item.lower() == "name":
        x += 1
    if item.lower() == "is":
        x += 1 
    if x >= 2:
        foundPattern = True