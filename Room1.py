####################################################################################
#Module Name: Room1
'''
Description: Room1 refers to Room103, in which the player will find Key Fragment2,
a locked box, a sudoku, and an exit door, located at the north, south, east, and west 
side of the Room103 respectively. Key Fragment2 and Room104 Key can be collected 
in this room. The product of the answer to the sudoku and the room number, 103 is 
the password to the locked box. After collecting the items and entering the password, 
the player will be able to leave the room.
'''
####################################################################################

import Move as m
import Bag as b
import Room2 as r
from tabulate import tabulate

answer = 0
pw = 8
password = 8*103
flag = True


'''
Collect Key Fragment2 and place it in the bag.
The player is not allowed to collect it twice.
'''
def north():
    if "Key Fragment2" in b.bag:
        print("Sorry, you have already collected the second key fragment here. Please visit other places.")
    else:
        print("You collect the second key fragment. You are one step closer to escape.")
        b.bag.append("Key Fragment2")


'''
Located at the south side of Room103 is a locked box. 
The player needs to solve the sudoku in the east first before being able to open the box 
to collect Room104 Key. The player is not allowed to collect it twice.
'''
def south():
    if "Room104 Key" in b.bag:
        print("You've opened the box and collected Room104 Key. You don't need to do it again.")
        return
    
    print("You see a locked box. The password is three-digit. \n"
          "Hint: calculate the product of the two positive integers in this room.")
    if answer == 0: # don't let the player enter password without solving the puzzle first
        print("Sorry, you can't open the box without solving the puzzle. Please do it first.")
        return
    
    #player enters the password
    while True:
        try:
            ans = int(input("Password: "))

            if ans == password:
                print("Corrent password. You open the box and collect Room104 Key.")
                b.bag.append("Room104 Key")
                break
            else:
                print("Wrong password. Please try again.")
                print("Hint: multiply the number you get from solving the puzzle \n"
                    "and the first three-digit number you see when entering the room.")
                
        except:
            print("Please type a number.")


'''A sudoku game, the player needs to find which number "X" represents'''
def east():
    global answer

    #sudoku, using tabulate for formatting
    print("You see a sudoku: ")
    sudoku = [[None, 2, None, None, 8, None, None, 7, None],
                [4, 7, None, None, None, 9, None, None, None],
                [None, None, None, None, None, 5, 5, 2, None],
                [None, 9, 2, 3, None, None, 1, None, None],
                ["X", 1, None, None, 7, None, None, 3, 5],
                [None, None, 7, 9, None, 5, 6, None, None],
                [7, None, 4, None, None, None, 2, None, 6],
                [None, None, None, 6, 3, 4, None, None, None],
                [6, None, None, None, 9, None, None, 5, 3]]
    print(tabulate(sudoku, tablefmt = "fancy_grid"))

    #player answers "What number does X represent?: "
    while True:
        try:
            answer = int(input("What number does X represent?: "))
            if answer == pw:
                print("Hooray! You nailed it. You are clever.")
                break
            else:
                print("Sorry, your answer isn't correct. Please do it again.")
        except: 
            print("Please type a single digit.")


'''
The door to leave Room103. The player is not allowed to leave without 
collecting all the items in the room.
'''
def west():
    global flag
    print("This is the door to leave Room103.")
    if "Room104 Key" in b.bag and "Key Fragment2" in b.bag:
        print("You've found all the items in this room. You may leave the room now.")
        flag = False
        r.entering()
    else:
        print("Sir, please don't leave the room now. You still have items unfound.")


dir = [north, south, east, west]


'''
Main room1 function that gives a description of the Room103 and leads the player
to different directions by calling the 4 direction methods above.
'''
def room1():
    #room description of Room103
    print()
    print("Now you are in Room 103.")
    print("A faded scent of dust lingers in the air. The wallpaper peels revealing stained walls.\n"
    " A flickering ceiling light casts long shadows across the room's furniture. \n"
    "An unmade bed, a cracked vanity mirror, and a creaky armoire half-open.")
    print()

    # a while loop that keeps asking the player which direction they want to go 
    # until the player leaves the room.
    while flag:
        direction = m.move()
        dir[direction]()
        