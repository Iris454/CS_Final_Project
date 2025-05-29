import Move as m
import Bag as b
import Room2 as r
from tabulate import tabulate
answer = 0
pw = 8
password = 8*103

def north():
    pass

def south():
    print("You see a locked box. The password is three-digit." \
          "Hint, calculate the product of the two positive integers in this room.")
    ans = int(input("Password: "))
    if answer == 0:
        print("Sorry, you can't open the box without solving the puzzle. Please do it first.")
    elif ans == password:
        print("Corrent password. You open the box and collect Room104 Key.")
        b.bag.append("Room104 Key")
    else:
        print("Wrong password. Please try again.")

def east():
    global answer
    print("You see a sudoku: ")
    while True:
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
        answer = int(input("What number does X represent?: "))
        if answer == pw:
            print("Hooray! You nailed it.")
            break
        else:
            print("Sorry, your answer isn't correct. Please do it again.")

def west():
    if "Room104 Key" in b.bag and "Key Fragment3" in b.bag:
        print("You've found all the items in this room. You may leave the room now.")
        r.room2()
    else:
        print("Sir, please don't leave the room now. You still have items unfound.")


dir = [north, south, east, west]

def room1():
    direction = m.move()
    dir[direction]()
    