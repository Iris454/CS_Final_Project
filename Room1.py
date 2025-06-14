import Move as m
import Bag as b
import Room2 as r
from tabulate import tabulate
answer = 0
pw = 8
password = 8*103
flag = True

def north():
    if "Key Fragment2" in b.bag:
        print("Sorry, you have already collected the second key fragment here. Please visit other places.")
    else:
        print("You collect the second key fragment. You are one step closer to escape.")
        b.bag.append("Key Fragment2")

def south():
    if "Room104 Key" in b.bag:
        print("You've opened the box and collected Room104 Key. You don't need to do it again.")
        return
    
    print("You see a locked box. The password is three-digit. \n"
          "Hint: calculate the product of the two positive integers in this room.")
    if answer == 0:
        print("Sorry, you can't open the box without solving the puzzle. Please do it first.")
        return

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

def east():
    global answer
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

def west():
    global flag
    if "Room104 Key" in b.bag and "Key Fragment2" in b.bag:
        print("You've found all the items in this room. You may leave the room now.")
        flag = False
        r.entering()
    else:
        print("Sir, please don't leave the room now. You still have items unfound.")


dir = [north, south, east, west]

def room1():
    print()
    print("Now you are in Room 103.")
    while flag:
        direction = m.move()
        dir[direction]()
        