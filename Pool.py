# import modules and libraries
import Move as m
import Bag as b
from tabulate import tabulate

password = "042"
flag = True

def north():
    if "Key Fragment1" in b.bag:
        print("You've collected the first piece of key fragment. You don't need to collect again.")
        return 
    
    print("You collect the first piece of key fragment. It's the key to escape.")
    b.bag.append("Key Fragment1")

def south():
    while True:
        print("Here's a towel basket. Do you want to put one in your bag?")
        choice = input("choice (y/n): ")
        if choice == "y":
            b.bag.append("Pool Towel")
            break
        elif choice == "n":
            print("Ok thats fine.")
            break
        else:
            print("Sorry, only pick y or n")
        

def east():
     print("Be carefull, if you go that way you're going to fall in the pool. Get out of here")


def west():
    global flag

    if "Key Fragment1" not in b.bag:
        print("Sorry, don't return to the restaurant yet. You have something unfound.")
    while True:
        print("To enter you have to pass this puzzle.")
        print("You see a locked box. The password is three-digit.")
        print("On a piece of paper next to the box, you see:")
        grid = [[6, 8, 2, "One number is correct and well placed"],
                [6, 1, 4, "One number is correct but wrong placed"],
                [2, 0, 6, "Two numbers are correct but wrong placed"],
                [7, 3, 8, "Nothing is correct"],
                [7, 8, 0, "One number is correct but wrong placed"]]
        print(tabulate(grid, tablefmt = "fancy_grid"))

        ans = input("Password (type three numbers in the correct order without spaces): ")
        if ans == password:
            print("Correct password! You may return to the restaurant.")
            flag = False
            break
        else:
            print("Wrong password. Please try again.") 


dir = [north, south, east, west]

def pool():
    print()
    print("Now you are in the pool ------")
    print("A dull and dark pool area, with beach chairs set along the edge. The stack of unused towels in the corner, "\
            "gives the sense that somthings wrong. When was the last time this pool was used?")
    print()
    
    while flag:
        direction = m.move()
        dir[direction]()
    
