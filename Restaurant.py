import Move as m
import Elevator as e
import Pool as p
eat = True

def north():
    print("That way is the elevator.")
    while True:
        print("To go into the elevator you have to solve this easy riddle!")
        print("I have keys, but no locks, I have a space, but no room. You can enter, but can't go outside.")
        answer = input("What am I?: ")
        if answer == "keyboard" or "Keyboard": 
            print("Congratulations, you have solved it, very intelligent.")
            eat = False
            e.elevator()
        else:
            print("No, that is wrong.")


def south():
    print("Sorry there's nothing that way, pick another direction.")
    pass

def east():
    while True:
        print("That's the pool, to go there you have to solve this tricky riddle!")
        print("Tim's mom has 4 sons, Red, Orange, and Yellow.")
        answer = input("What is the fourth son's name?: ")
        if answer == "Tim":
            print("Yes, you're clever. Now you can go into the pool.")
            eat = False
            p.Pool()
        else:
            print("Wrong.")


def west():
    print("You've already collected everything from the lobby, you don't need to go that way.")

def restaurant():
    direction = m.move()
    dir[direction]()

dir = [north, south, east, west]