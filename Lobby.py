####################################################################################
#Module Name: Lobby
'''
Description: In the lobby, the player will find a reception desk, hotel entrance,
a locked door to the restaurant, and a calculus problem, located at the north, 
south, east, and west side of the lobby respectively. Room103 Key and a map can be
collected at the reception desk. The answer to the calculus problem is the password
to the locked door. After collecting the items and enter the password, the player
will be able to enter the restuarant.
'''
####################################################################################

import Move as m
import Bag as b
import Restaurant as r
import Map as ma
import Countdown as c

flag = True
answer = 0
pw = 1372

'''
Located at the north side of the lobby is a reception desk.
The player can get Room103 Key and a map here.
The player can only collect Room103 Key once even if he/she visits this place multiple times.
'''
def north():
    print("You are at the reception desk.")
    print("A receptionist, Bob, greets you with a big warm smile.")
    print("Hi sir. How can I help you?")
    while True:
        try:
            print("1. get a hotel map")
            print("2. check in")
            choice = int(input("choice (1/2): "))
            if choice == 1:
                ma.map()
                break
            elif choice == 2 and len(b.bag) == 0:
                print("Sir, this is your room key. Your room is 103.")
                b.bag.append("Room103 Key")
                break
            elif choice == 2 and len(b.bag) != 0:
                print("Sir, you've already checked in. You don't need to do it again.")
                break
            else:
                print("Please choose 1 or 2.")
        except:
            print("Please type a single digit.")
            


'''Entrance of the hotel'''
def south():
    print("This is the entrance. The door is locked. Come back here at the end to unlock it with a key.")


'''
Located at the east side of the lobby is the door to the restuarant. It is locked.
The password is the answer to the Calculus question in the west.
If you have not collected the Room103 Key at the reception deak, a message will show
up telling you to collect it first before you can enter the restaurant. 
'''
def east():
    global flag
    print("This is the door to the restaurant. You need a four-digit password to unlock it.")
    while True:
        try:
            print("1. enter password")
            print("2. look around in the lobby")
            choice = int(input("choice (1/2): "))
            if choice == 1:
                if answer == 0:
                    print("You haven't found the password. Please walk around in the lobby to find it.")
                elif answer == pw:
                    print("The password is correct! You've mastered the knowledge of CALCULUS!")
                    print()
                    c.countdown(2)
                    if len(b.bag) == 0:
                        print("Sorry, please check in at the reception desk first before entering the restuarant.")
                    else:
                        print("You may visit the restuarant!")
                        flag = False  # breaks the while loop in the lobby method
                        r.restaurant()
                else:
                    print("Incorrect password. Please solve the math question again.")
                
                break
            elif choice == 2:
                break
            else:
                print("Please choose 1 or 2.")

        except:
            print("Please type a single digit.") 


'''
Here, the player has a Calculus question to solve.
The answer will be the password to open the restaurant door. 
'''
def west():
    global answer
    print("You see a math question: \n" 
    "Two nonnegative numbers have a sum of 21. If the product of one of the numbers \n" 
    "with the square of the other is to be a maximum, what is this maximum product?")
    while True:
        try:
            answer = int(input("answer: "))
            break
        except:  # Catch the error in case the player input is not an integer
            print("Please type a number.")


dir = [north, south, east, west]


'''
Main lobby function that gives a description of the lobby and leads the player
to different directions by calling the 4 direction methods above.
'''
def lobby():

    # room description of the lobby
    print()
    print("You are in the lobby ------")
    print("A big room with a grand red carpet leading down to the reception desk. \n" 
            " Classy and sopisticated. It seems perfect at first glance, but with a closer look somthing seems off.")
    print()

    # a while loop that keeps asking the player which direction they want to go 
    # until the player enters another room
    while flag: 
        direction = m.move()
        dir[direction]()
        
