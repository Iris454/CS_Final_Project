import Move as m
import Bag as b
import Restaurant as r
import Map as ma
import Countdown as c

flag = True
answer = 0
pw = 1372

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
            


def south():
    print("This is the entrance. The door is locked. Come back here at the end to unlock it with a key.")

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
                        flag = False
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


def west():
    global answer
    print("You see a math question: \n" 
    "Two nonnegative numbers have a sum of 21. If the product of one of the numbers \n" 
    "with the square of the other is to be a maximum, what is this maximum product?")
    while True:
        try:
            answer = int(input("answer: "))
            break
        except:
            print("Please type a number.")


dir = [north, south, east, west]

def lobby():

    print()
    print("You are in the lobby ------")
    print("A big room with a grand red carpet leading down to the reception desk. \n" 
            " Classy and sopisticated. It seems perfect at first glance, but with a closer look somthing seems off.")
    print()
    while flag:
        direction = m.move()
        dir[direction]()
        
