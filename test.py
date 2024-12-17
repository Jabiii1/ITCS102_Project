"""Pinag tetestingan ko ng code"""
# def cc():
#     codeChallenges = [
#     "                                            Garcia's Code Challenges!!!\n",
#     "Print Statements/Operators                 Condition/Variable/For Loops                               Functions      ",
#     "  1 --- Code Challenge 1       6 --- Code Challenge 6        10 --- Code Challenge 10        15 --- Code Challenge 15",
#     "  2 --- Code Challenge 2       7 --- Code Challenge 7        11 --- Code Challenge 11        16 --- Code Challenge 16",
#     "  4 --- Code Challenge 4       8 --- Code Challenge 8        12 --- Code Challenge 12",
#     "  5 --- Code Challenge 5      8a --- Code Challenge 8(1)     13 --- Code Challenge 13",
#     "                               9 --- Code Challenge 9        14 --- Code Challenge 14",]

#     for line in codeChallenges:
#         print(line)
#         time.sleep(0.3)
# cc()

# def act():
#     Activities = [
# "                                               Garcia's Activities!!!\n",
# "2 --- Activity 2       6 --- Activity 6       11 --- Activity 11      16 --- Activity 16      21 --- Activity 21",
# "3 --- Activity 3       7 --- Activity 7       12 --- Activity 12      17 --- Activity 17      22 --- Activity 22",
# "4 --- Activity 4       8 --- Activity 8       13 --- Activity 13      18 --- Activity 18      23 --- Activity 23",
# "5 --- Activity 5       9 --- Activity 9       14 --- Activity 14      19 --- Activity 19      24 --- Activity 24",
# "                      10 --- Activity 10      15 --- Activity 15      20 --- Activity 20      25 --- Activity 25"]

#     for line in Activities:
#         print(line)
#         time.sleep(0.3)
# act()





import time
import os

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

def heart():  #mini effort sa huli fully pro max
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

    # smaller version ng puso
    puso_small = [
        "      *     *     ",
        "     ***   ***    ",
        "    ***** *****   ",
        "     *********    ",
        "      *******     ",
        "       *****      ",
        "        ***       ",
        "         *        "]


    for pagtibok in range(10): # Pang Animate the heart para tumibok 10 times
        os.system('cls')  # Para ma clear yung screen at lumabas yung kabilang heart
        for line in puso_small: #smaller heart
            print(line)
        time.sleep(0.5)

        os.system('cls')  # Para ma clear yung screen at lumabas yung kabilang heart
        for line in puso: #Para sa malaking heart
            print(line)
        time.sleep(0.5)
        
    os.system('cls')   # Final display ng heart after tumibok
    for line in puso:
        print(line)
    
    time.sleep(1)  # Pause bago lumabas yung sa command

def cc9():
    print("slkjdldj")
    
    for x in range(1, 11):
        print("  " * x , end =" ")  
        for y in range(x, 11):
            print("*", end = " ")  
        print()    
        
cc9()