from activity2 import act2
from activity3 import act3
from activity4 import act4
from activity5 import act5
from activity6 import act6
from activity7 import act7
from activity8 import act8
from activity9 import act9
from activity10 import act10
from activity11 import act11
from activity12 import act12
from activity13 import act13
from activity14 import act14
from activity15 import act15
from activity16 import act16
from activity17 import act17
from activity18 import act18
from activity19 import act19
from activity20 import act20
from activity21 import act21
from activity22 import act22
from activity23 import act23
from activity24 import act24
from activity25 import act25
from code_challenge1 import cc1
from code_challenge2 import cc2
from code_challenge4 import cc4
from code_challenge5 import cc5
from code_challenge6 import cc6
from code_challenge7 import cc7
from code_challenge8 import cc8
from code_challenge8another import cc8a         #this is the other code_challenge 8
from code_challenge9 import cc9 
from code_challenge10 import cc10
from code_challenge11 import cc11
from code_challenge12 import cc12
from code_challenge13 import cc13
from code_challenge14 import cc14
from code_challenge15 import cc15
from code_challenge16 import cc16
import os             #para sa cls
import time           #para sa heart
import webbrowser     #para sa pag visit ng github acc

def definitions():
    os.system('cls')
    print("Definitioins!")
    df = [
        "1 --- Print Statements",
        "2 --- Variables",
        "3 --- Operators",
        "4 --- Conditional",
        "5 --- Loops",
        "6 --- List",
        "7 --- Functions",
    ]
    
    for dfline in df:
        print(dfline)
        time.sleep(0.3)
    
    pickdef= input("Select one Definitons (type 'back' to return): ")
    
    if pickdef == "1":
        os.system('cls')
        print("Print Statements: Print statements are used to display output to the user. \n\nFor Example: \nprint('Your code')\n\nOutput:\nYour code")
        while True:
            back = input("\nDo you want to go back? (yes/no): ")
            if back.lower() == "yes":
                return definitions()
                break
            elif back.lower() == "no":
                print("Reviewing Definitions...")
                continue
            else:
                print("Invalid input. Please enter 'yes' or 'no'")
                continue
    
    elif pickdef == "2":
        os.system('cls')
        print("Variables: Variables are used to store data in the memory. \n\nFor Example:\n\nx = 26\ny = 'Jayvee'\n\nprint(x)\nprint(y) \n\nOutput:\n\n26\nJayvee")
        while True:
            back = input("\nDo you want to go back? (yes/no): ")
            if back.lower() == "yes":
                return definitions()
                break
            elif back.lower() == "no":
                print("Reviewing Definitions...")
                continue
            else:
                print("Invalid input. Please enter 'yes' or 'no'")
                continue
    
    elif pickdef == "3":
        os.system('cls')
        print("Operators: Operators are used to perform operations on variables.")
        print("\nFor Example: \n\n+	Addition	x + y	\n-	Subtraction	x - y	\n*	Multiplication	x * y	\n/	Division	x / y	\n%	Modulus         x % y	\n**	Exponentiation	x ** y	\n//	Floor division	x // y")
        while True:
            back = input("\nDo you want to go back? (yes/no): ")
            if back.lower() == "yes":
                return definitions()
                break
            elif back.lower() == "no":
                print("Reviewing Definitions...")
                continue
            else:
                print("Invalid input. Please enter 'yes' or 'no'")
                continue
    
    elif pickdef == "4":
        os.system('cls')
        print("Conditional: Conditional statements are used to control the flow of a program.\n")
        print("An -if- statement is written by using the if keyword.\nThe -elif- keyword is Python's way of saying 'if the previous conditions were not true, then try this condition'.\nThe -else- keyword catches anything which isn't caught by the preceding conditions.")
        print("\nFor Example:\nx = 5\ny = 2\nif x > y:\n  print('x is greater than y')\nelif:\n  print('x is less than y')\nelse:  print('both of them are equal')\n\n\nOutput:\nx is greater than y")
        while True:
            back = input("\nDo you want to go back? (yes/no): ")
            if back.lower() == "yes":
                return definitions()
                break
            elif back.lower() == "no":
                print("Reviewing Definitions...")
                continue
            else:
                print("Invalid input. Please enter 'yes' or 'no'")
                continue
    
    elif pickdef == "5":
        os.system('cls')
        print("Loops: Loops are used to repeat a block of code a specified number of times.")
        print("-for loop- is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).")
        print("-while loop- we can execute a set of statements as long as a condition is true.")
        print("\n-continue- statement we can stop the current iteration, and continue with the next")
        print("-break- statement we can stop the loop even if the while condition is true:")
        print("For Example:\n     for x in range(1, 6):\n\tprint('  ' * x , end =' ')\n     for y in range(x, 6):\n\tprint('*', end = ' ')\n     print()")
        print("\nOutput:\n* * * * *\n  * * * *\n    * * *\n      * *\n        * ")
        while True:
            back = input("\nDo you want to go back? (yes/no): ")
            if back.lower() == "yes":
                return definitions()
                break
            elif back.lower() == "no":
                print("Reviewing Definitions...")
                continue
            else:
                print("Invalid input. Please enter 'yes' or 'no'")
                continue
    
    elif pickdef == "6":
        os.system('cls')
        print("List: Lists are used to store multiple items in a single variable.\nThe -list- is changeable, meaning that we can change,add, and remove items after it has been created.")
        print("The -insert()- method inserts an item at the specified index.\nUse the -append()- method to add an item to the end of the list.\n\nLists are created using square brackets:")
        print("\nFor Example:\nmylist = ['Garcia', 'Jayvee', 'Cargando']\nmylist.insert(3,'BSIT')\nmylist.append('1A')\nprint(mylist)")
        print("\nOutput:\n['Garcia', 'Jayvee', 'Cargando', 'BSIT', '1A']\n")
        while True:
            back = input("Do you want to go back? (yes/no): ")
            if back.lower() == "yes":
                return definitions()
                break
            elif back.lower() == "no":
                print("Reviewing Definitions...")
                continue
            else:
                print("Invalid input. Please enter 'yes' or 'no'")
                continue
    
    elif pickdef == "7":
        os.system('cls')
        print("Functions: Functions are used to group a set of related statements together that only runs when it is called.\nA function is defined using the -def- keyword\nTo call a function, use the function name followed by parenthesis")
        print("\nFor Example:\ndef myFunction():\n   print('Jayvee')\nmyFunction()")
        print("\nOutput:\nJayvee")
        while True:
            back = input("\nDo you want to go back? (yes/no): ")
            if back.lower() == "yes":
                return definitions()
                break
            elif back.lower() == "no":
                print("Reviewing Definitions...")
                continue
            else:
                print("Invalid input. Please enter 'yes' or 'no'")
                continue
    
    elif pickdef.lower() == "back":
        return main()
    else:
        return definitions()
def schoolworks():
    os.system('cls')
    pick1 = input("Schoolworks!\n1 --- Activity\n2 --- Code challenge\n3 --- Back \nChoose between the Schoolworks: ")
    while True:
        if pick1 == "1":
            os.system('cls')
            act()
            break
            
        elif pick1 == "2":
            os.system('cls')
            cc()
            break
            
        elif pick1 == "3":
            os.system('cls')
            return main()
            break
        else:
            return schoolworks()
def act():            #All Acitivities
    os.system('cls')
    Activities = [
        "                                               Garcia's Activities!!!\n",
            "2 --- Activity 2       6 --- Activity 6       11 --- Activity 11      16 --- Activity 16      21 --- Activity 21",
            "3 --- Activity 3       7 --- Activity 7       12 --- Activity 12      17 --- Activity 17      22 --- Activity 22",
            "4 --- Activity 4       8 --- Activity 8       13 --- Activity 13      18 --- Activity 18      23 --- Activity 23",
            "5 --- Activity 5       9 --- Activity 9       14 --- Activity 14      19 --- Activity 19      24 --- Activity 24",
            "                      10 --- Activity 10      15 --- Activity 15      20 --- Activity 20      25 --- Activity 25\n"]

    for line in Activities:
        print(line)
        time.sleep(0.3)
    
    pickact= input("Select one Activity (type 'back' to return): ")
    
    if pickact == "1":
        os.system('cls')
        return act()
    
    elif pickact == "2":
        os.system('cls')
        act2()
        while True:
            back = input("Do you want to go back? (yes/no): ")
            if back.lower() == "yes":
                return act()
                break
                act2() == False
            elif back.lower() == "no":
                print("Reviewing Schoolwork...")
                continue
            else:
                print("Invalid input. Please enter 'yes' or 'no'")
                continue
    
    elif pickact == "3":
        os.system('cls')
        act3()
        while True:
            back = input("Do you want to go back? (yes/no): ")
            if back.lower() == "yes":
                return act()
                break
                act3() == False
            elif back.lower() == "no":
                print("Reviewing Schoolwork...")
                continue
            else:
                print("Invalid input. Please enter 'yes' or 'no'")
                continue
    
    elif pickact == "4":
        os.system('cls')
        act4()
        while True:
            back = input("Do you want to go back? (yes/no): ")
            if back.lower() == "yes":
                return act()
                break
                act4() == False
            elif back.lower() == "no":
                print("Reviewing Schoolwork...")
                continue
            else:
                print("Invalid input. Please enter 'yes' or 'no'")
                continue
    
    elif pickact == "5":
        os.system('cls')
        act5()
        while True:
            back = input("Do you want to go back? (yes/no): ")
            if back.lower() == "yes":
                return act()
                break
                act5() == False
            elif back.lower() == "no":
                print("Reviewing Schoolwork...")
                continue
            else:
                print("Invalid input. Please enter 'yes' or 'no'")
                continue
    
    elif pickact == "6":
        os.system('cls')
        act6()
        while True:
            back = input("Do you want to go back? (yes/no): ")
            if back.lower() == "yes":
                return act()
                break
                act6() == False
            elif back.lower() == "no":
                print("Reviewing Schoolwork...")
                continue
            else:
                print("Invalid input. Please enter 'yes' or 'no'")
                continue
    
    elif pickact == "7":
        os.system('cls')
        act7()
        while True:
            back = input("Do you want to go back? (yes/no): ")
            if back.lower() == "yes":
                return act()
                break
                act7() == False
            elif back.lower() == "no":
                print("Reviewing Schoolwork...")
                continue
            else:
                print("Invalid input. Please enter 'yes' or 'no'")
                continue
    
    elif pickact == "8":
        os.system('cls')
        act8()
        while True:
            back = input("Do you want to go back? (yes/no): ")
            if back.lower() == "yes":
                return act()
                break
                act8() == False
            elif back.lower() == "no":
                print("Reviewing Schoolwork...")
                continue
            else:
                print("Invalid input. Please enter 'yes' or 'no'")
                continue
    
    elif pickact == "9":
        os.system('cls')
        act9()
        while True:
            back = input("Do you want to go back? (yes/no): ")
            if back.lower() == "yes":
                return act()
                break
                act9() == False
            elif back.lower() == "no":
                print("Reviewing Schoolwork...")
                continue
            else:
                print("Invalid input. Please enter 'yes' or 'no'")
                continue
    
    elif pickact == "10":
        os.system('cls')
        act10()
        while True:
            back = input("Do you want to go back? (yes/no): ")
            if back.lower() == "yes":
                return act()
                break
                act10() == False
            elif back.lower() == "no":
                print("Reviewing Schoolwork...")
                continue
            else:
                print("Invalid input. Please enter 'yes' or 'no'")
                continue
    
    elif pickact == "11":
        os.system('cls')
        act11()
        while True:
            back = input("Do you want to go back? (yes/no): ")
            if back.lower() == "yes":
                return act()
                break
                act11() == False
            elif back.lower() == "no":
                print("Reviewing Schoolwork...")
                continue
            else:
                print("Invalid input. Please enter 'yes' or 'no'")
                continue
    
    elif pickact == "12":
        os.system('cls')
        act12()
        while True:
            back = input("Do you want to go back? (yes/no): ")
            if back.lower() == "yes":
                return act()
                break
                act12() == False
            elif back.lower() == "no":
                print("Reviewing Schoolwork...")
                continue
            else:
                print("Invalid input. Please enter 'yes' or 'no'")
                continue
    
    elif pickact == "13":
        os.system('cls')
        act13()
        while True:
            back = input("Do you want to go back? (yes/no): ")
            if back.lower() == "yes":
                return act()
                break
                act13() == False
            elif back.lower() == "no":
                print("Reviewing Schoolwork...")
                continue
            else:
                print("Invalid input. Please enter 'yes' or 'no'")
                continue
    
    elif pickact == "14":
        os.system('cls')
        act14()
        while True:
            back = input("Do you want to go back? (yes/no): ")
            if back.lower() == "yes":
                return act()
                break
                act14() == False
            elif back.lower() == "no":
                print("Reviewing Schoolwork...")
                continue
            else:
                print("Invalid input. Please enter 'yes' or 'no'")
                continue
    
    elif pickact == "15":
        os.system('cls')
        act15()
        while True:
            back = input("Do you want to go back? (yes/no): ")
            if back.lower() == "yes":
                return act()
                break
                act15() == False
            elif back.lower() == "no":
                print("Reviewing Schoolwork...")
                continue
            else:
                print("Invalid input. Please enter 'yes' or 'no'")
                continue
    
    elif pickact == "16":
        os.system('cls')
        act16()
        while True:
            back = input("Do you want to go back? (yes/no): ")
            if back.lower() == "yes":
                return act()
                break
                act16() == False
            elif back.lower() == "no":
                print("Reviewing Schoolwork...")
                continue
            else:
                print("Invalid input. Please enter 'yes' or 'no'")
                continue
    
    elif pickact == "17":
        os.system('cls')
        act17()
        while True:
            back = input("Do you want to go back? (yes/no): ")
            if back.lower() == "yes":
                return act()
                break
                act17() == False
            elif back.lower() == "no":
                print("Reviewing Schoolwork...")
                continue
            else:
                print("Invalid input. Please enter 'yes' or 'no'")
                continue
    
    elif pickact == "18":
        os.system('cls')
        act18()
        while True:
            back = input("Do you want to go back? (yes/no): ")
            if back.lower() == "yes":
                return act()
                break
                act18() == False
            elif back.lower() == "no":
                print("Reviewing Schoolwork...")
                continue
            else:
                print("Invalid input. Please enter 'yes' or 'no'")
                continue
    
    elif pickact == "19":
        os.system('cls')
        act19()
        while True:
            back = input("Do you want to go back? (yes/no): ")
            if back.lower() == "yes":
                return act()
                break
                act19() == False
            elif back.lower() == "no":
                print("Reviewing Schoolwork...")
                continue
            else:
                print("Invalid input. Please enter 'yes' or 'no'")
                continue
    
    elif pickact == "20":
        os.system('cls')
        act20()
        while True:
            back = input("Do you want to go back? (yes/no): ")
            if back.lower() == "yes":
                return act()
                break
                act20() == False
            elif back.lower() == "no":
                print("Reviewing Schoolwork...")
                continue
            else:
                print("Invalid input. Please enter 'yes' or 'no'")
                continue
    
    elif pickact == "21":
        os.system('cls')
        act21()
        while True:
            back = input("Do you want to go back? (yes/no): ")
            if back.lower() == "yes":
                return act()
                break
                act21() == False
            elif back.lower() == "no":
                print("Reviewing Schoolwork...")
                continue
            else:
                print("Invalid input. Please enter 'yes' or 'no'")
                continue
            
    elif pickact == "22":
        os.system('cls')
        act22()
        while True:
            back = input("Do you want to go back? (yes/no): ")
            if back.lower() == "yes":
                return act()
                break
                act22() == False
            elif back.lower() == "no":
                print("Reviewing Schoolwork...")
                continue
            else:
                print("Invalid input. Please enter 'yes' or 'no'")
                continue
    
    elif pickact == "23":
        os.system('cls')
        act23()
        while True:
            back = input("Do you want to go back? (yes/no): ")
            if back.lower() == "yes":
                return act()
                break
                act23() == False
            elif back.lower() == "no":
                print("Reviewing Schoolwork...")
                continue
            else:
                print("Invalid input. Please enter 'yes' or 'no'")
                continue
    
    elif pickact == "24":
        os.system('cls')
        act24()
        while True:
            back = input("Do you want to go back? (yes/no): ")
            if back.lower() == "yes":
                return act()
                break
                act24() == False
            elif back.lower() == "no":
                print("Reviewing Schoolwork...")
                continue
            else:
                print("Invalid input. Please enter 'yes' or 'no'")
                continue
    
    elif pickact == "25":
        os.system('cls')
        act25()
        while True:
            back = input("Do you want to go back? (yes/no): ")
            if back.lower() == "yes":
                return act()
                break
                act25() == False
            elif back.lower() == "no":
                print("Reviewing Schoolwork...")
                continue
            else:
                print("Invalid input. Please enter 'yes' or 'no'")
                continue
    elif pickact.lower() == "back":
        return schoolworks()
    else:
        return act()
def cc():             #All Code Challenge
    os.system('cls')
    codeChallenges = [
    "                                            Garcia's Code Challenges!!!\n",
    
    "1 --- Code Challenge 1       6 --- Code Challenge 6        10 --- Code Challenge 10        15 --- Code Challenge 15",
    "2 --- Code Challenge 2       7 --- Code Challenge 7        11 --- Code Challenge 11        16 --- Code Challenge 16",
    "4 --- Code Challenge 4       8 --- Code Challenge 8        12 --- Code Challenge 12",
    "5 --- Code Challenge 5      8a --- Code Challenge 8(1)     13 --- Code Challenge 13",
    "                             9 --- Code Challenge 9        14 --- Code Challenge 14\n",]

    for line in codeChallenges:
        print(line)
        time.sleep(0.3)
    
    pickcc= input("Select one Code Challenge (type 'back' to return): ")
            
    if pickcc == "1":
        os.system('cls')
        cc1()
        while True:
            back = input("Do you want to go back? (yes/no): ")
            if back.lower() == "yes":
                return cc()
                break
                cc1() == False
            elif back.lower() == "no":
                print("Reviewing Schoolwork...")
                continue
            else:
                print("Invalid input. Please enter 'yes' or 'no'")
                continue
    
    elif pickcc == "2":
        os.system('cls')
        cc2()
        while True:
            back = input("Do you want to go back? (yes/no): ")
            if back.lower() == "yes":
                return cc()
                break
                cc2() == False
            elif back.lower() == "no":
                print("Reviewing Schoolwork...")
                continue
            else:
                print("Invalid input. Please enter 'yes' or 'no'")
                continue
    elif pickcc == "3":
        return cc()
    
    elif pickcc == "4":
        os.system('cls')
        cc4()
        while True:
            back = input("Do you want to go back? (yes/no): ")
            if back.lower() == "yes":
                return cc()
                break
                cc4() == False
            elif back.lower() == "no":
                print("Reviewing Schoolwork...")
                continue
            else:
                print("Invalid input. Please enter 'yes' or 'no'")
                continue
    
    elif pickcc == "5":
        os.system('cls')
        cc5()
        while True:
            back = input("Do you want to go back? (yes/no): ")
            if back.lower() == "yes":
                return cc()
                break
                cc5() == False
            elif back.lower() == "no":
                print("Reviewing Schoolwork...")
                continue
            else:
                print("Invalid input. Please enter 'yes' or 'no'")
                continue
    
    elif pickcc == "6":
        os.system('cls')
        cc6()
        while True:
            back = input("Do you want to go back? (yes/no): ")
            if back.lower() == "yes":
                return cc()
                break
                cc6() == False
            elif back.lower() == "no":
                print("Reviewing Schoolwork...")
                continue
            else:
                print("Invalid input. Please enter 'yes' or 'no'")
                continue
    
    elif pickcc == "7":
        os.system('cls')
        cc7()
        while True:
            back = input("Do you want to go back? (yes/no): ")
            if back.lower() == "yes":
                return cc()
                break
                cc7() == False
            elif back.lower() == "no":
                print("Reviewing Schoolwork...")
                continue
            else:
                print("Invalid input. Please enter 'yes' or 'no'")
                continue
            
    elif pickcc == "8":
        os.system('cls')
        cc8()
        while True:
            back = input("Do you want to go back? (yes/no): ")
            if back.lower() == "yes":
                return cc()
                break
                cc8() == False
            elif back.lower() == "no":
                print("Reviewing Schoolwork...")
                continue
            else:
                print("Invalid input. Please enter 'yes' or 'no'")
                continue
    
    elif pickcc.lower() == "8a":
        os.system('cls')
        cc8a()
        while True:
            back = input("Do you want to go back? (yes/no): ")
            if back.lower() == "yes":
                return cc()
                break
                cc8a() == False
            elif back.lower() == "no":
                print("Reviewing Schoolwork...")
                continue
            else:
                print("Invalid input. Please enter 'yes' or 'no'")
                continue
    
    elif pickcc == "9":
        os.system('cls')
        cc9()
        while True:
            back = input("Do you want to go back? (yes/no): ")
            if back.lower() == "yes":
                return cc()
                break
                cc9() == False
            elif back.lower() == "no":
                print("Reviewing Schoolwork...")
                continue
            else:
                print("Invalid input. Please enter 'yes' or 'no'")
                continue
    
    elif pickcc == "10":
        os.system('cls')
        cc10()
        while True:
            back = input("Do you want to go back? (yes/no): ")
            if back.lower() == "yes":
                return cc()
                break
                cc10() == False
            elif back.lower() == "no":
                print("Reviewing Schoolwork...")
                continue
            else:
                print("Invalid input. Please enter 'yes' or 'no'")
                continue
    
    elif pickcc == "11":
        os.system('cls')
        cc11()
        while True:
            back = input("Do you want to go back? (yes/no): ")
            if back.lower() == "yes":
                return cc()
                break
                cc11() == False
            elif back.lower() == "no":
                print("Reviewing Schoolwork...")
                continue
            else:
                print("Invalid input. Please enter 'yes' or 'no'")
                continue
    
    elif pickcc == "12":
        os.system('cls')
        cc12()
        while True:
            back = input("Do you want to go back? (yes/no): ")
            if back.lower() == "yes":
                return cc()
                break
                cc12() == False
            elif back.lower() == "no":
                print("Reviewing Schoolwork...")
                continue
            else:
                print("Invalid input. Please enter 'yes' or 'no'")
                continue
    
    elif pickcc == "13":
        os.system('cls')
        cc13()
        while True:
            back = input("Do you want to go back? (yes/no): ")
            if back.lower() == "yes":
                return cc()
                break
                cc13() == False
            elif back.lower() == "no":
                print("Reviewing Schoolwork...")
                continue
            else:
                print("Invalid input. Please enter 'yes' or 'no'")
                continue
    
    elif pickcc == "14":
        os.system('cls')
        cc14()
        while True:
            back = input("Do you want to go back? (yes/no): ")
            if back.lower() == "yes":
                return cc()
                break
                cc14() == False
            elif back.lower() == "no":
                print("Reviewing Schoolwork...")
                continue
            else:
                print("Invalid input. Please enter 'yes' or 'no'")
                continue
    
    elif pickcc == "15":
        os.system('cls')
        cc15()
        while True:
            back = input("Do you want to go back? (yes/no): ")
            if back.lower() == "yes":
                return cc()
                break
                cc15() == False
            elif back.lower() == "no":
                print("Reviewing Schoolwork...")
                continue
            else:
                print("Invalid input. Please enter 'yes' or 'no'")
                continue
            
    elif pickcc == "16":
        os.system('cls')
        cc16()
        while True:
            back = input("Do you want to go back? (yes/no): ")
            if back.lower() == "yes":
                return cc()
                break
                cc16() == False
            elif back.lower() == "no":
                print("Reviewing Schoolwork...")
                continue
            else:
                print("Invalid input. Please enter 'yes' or 'no'")
                continue
    elif pickcc.lower() == "back":
        return schoolworks()
    else:
        return cc()

def heart():  #mini effort sa huli
    print("\nThanks for using the program!\n")
    time.sleep(1)

    puso = [
        "     ***     ***  ",
        "    *****   ***** ",
        "   ******* *******",
        "    ************* ",
        "     ***********  ",
        "      *********   ",
        "       *******    ",
        "        *****     ",
        "         ***      ",
        "          *       "]

    for line in puso:
        print(line)
        time.sleep(0.3)  

def link():           #Github Profile
    webbrowser.open("https://github.com/Jabiii1")
def main():           #Main Menu
    os.system('cls')  
    print("Jayvee C. Garcia BSIT-1A First-Sem Project!!!")
    pick = input("\n1 --- Schoolworks\n2 --- Definitions\n3 --- Github Profile\n4 --- Exit\nChoose between the choices: ")

    if pick == "1":
        schoolworks()
        
    elif pick == "2":
        os.system('cls')
        definitions()


    elif pick == "3":
        link()
    
    elif pick == "4":
        os.system('cls')
        print("Program Terminated.")
        heart()
    else:
        return main()
main()