import Move as m
import Bag as b

flag = True

def north():
    print("You are at the reception desk.")
    print("A receptionist, Bob, greets you with a big warm smile.")
    while True:
        print("Hi sir. How can I help you?")
        print("1. get a hotel map")
        print("2. check in")
        choice = int(input("choice (1/2): "))
        if choice == 1:
            pass #create a grid
        elif choice == 2:
            print("Sir, this is your room key. Your room is 103.")
            b.bag.append("Room103 Key")
            break
        else: 
            print("Please choose 1 or 2.")


def south():
    print("This is the entrance. The door is locked. Come back here at the end to unlock it with a key.")

def east():
    print("This is the door to the restaurant. You need a four-digit password to unlock it.")
    while True:
        print("1. enter password")
        print("2. look around in the lobby")
        choice = int(input("choice (1/2): "))
        if choice == 1:
            pw = int(input("password: "))
            # check if it matches the answer to the math question
            break
        elif choice == 2:
            break
        else: 
            print("Please choose 1 or 2.")


def west():
    print("You see a math question: Two nonnegative numbers have a sum of 21. What is the maximum product of ")
    pass

dir = [north, south, east, west]

def lobby():
    while flag:
        direction = m.move()
        dir[direction]()
        
