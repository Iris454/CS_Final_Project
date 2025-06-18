####################################################################################
#Module Name: Pool
'''
Description: In the pool, the player will find Key Fragment1, a towel basket, and a
puzzle located at the north, south, and west side of the lobby respectively. 
Key Fragment1 can be collected in the north. The towel basket is not a mandatory
collection item. The player needs to solve the puzzle to return to the restaurant.
'''
####################################################################################

import Move as m
import Bag as b
from tabulate import tabulate

password = "042"
flag = True


'''
Collect Key Fragment1 and place it in the bag, which is one of the three pieces of the key
that can open the hotel front door and lead to a successful escape.
The player is not allowed to collect it twice.
'''
def north():
    # if already collected the Key Fragment1, we don't let the player collect it again.
    if "Key Fragment1" in b.bag:
        print("You've collected the first piece of key fragment. You don't need to collect again.")
        return 
    
    # Collect Key Fragment1 and place it in the bag
    print("You collect the first piece of key fragment. It's the key to escape.")
    b.bag.append("Key Fragment1")


'''
Located at the south of the the pool is a towel basket.
It is not a mandatory collection item, as it will not affect the game later on.
'''
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
        

'''A slippery area'''
def east():
     print("Be carefull, if you go that way you're going to fall in the pool. Get out of here")


'''
Here we have a puzzle that the player needs to solve to return to the restaurant.
The player is not allowed to solve the puzzle and leave the pool until he/she has found
all the items in the pool.
'''
def west():
    global flag

    # we don't let the player return to the restaurant if they have items unfound
    if "Key Fragment1" not in b.bag:
        print("Sorry, don't return to the restaurant yet. You have something unfound.")
        return
    
    while True:
        # use tabulate to print the puzzle
        print("To enter you have to solve this puzzle.")
        print("You see a locked box. The password is three-digit.")
        print("On a piece of paper next to the box, you see:")
        grid = [[6, 8, 2, "One number is correct and well placed"],
                [6, 1, 4, "One number is correct but wrong placed"],
                [2, 0, 6, "Two numbers are correct but wrong placed"],
                [7, 3, 8, "Nothing is correct"],
                [7, 8, 0, "One number is correct but wrong placed"]]
        print(tabulate(grid, tablefmt = "fancy_grid"))

        #ask players to enter their answer and check if it matches the password
        ans = input("Password (type three numbers in the correct order without spaces): ")
        if ans == password:
            print("Correct password! You may return to the restaurant.")
            flag = False
            break
        else:
            print("Wrong password. Please try again.") 


dir = [north, south, east, west]


'''
Main pool function that gives a description of the pool and leads the player
to different directions by calling the 4 direction methods above.
'''
def pool():
    # room description of the pool
    print()
    print("Now you are in the pool ------")
    print("A dull and dark pool area, with beach chairs set along the edge. The stack of unused towels in the corner, "\
            "gives the sense that somthings wrong. When was the last time this pool was used?")
    print()

    # a while loop that keeps asking the player which direction they want to go 
    # until the player leaves the swimming pool
    while flag:
        direction = m.move()
        dir[direction]()
    
