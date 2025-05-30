import Move as m
import Elevator as e
import Pool as p
import Lobby as l

def north():
    print("That way is the elevator.")
    print("To go into the elevator you have to solve this easy riddle!")
    print("I have keys, but no locks, I have a space, but no room. You can enter, but can't go outside.")
    answer = input("What am I?: ")
    if answer == "keyboard" or "Keyboard": 
        print("Congratulations, you have solved it, very intelligent.")
        e.elevator()
    else:
        print("No, that is wrong.")


def south():
    print("Sorry there's nothing that way, pick another direction.")
    pass

def east():
    print("That's the pool, to go there you have to solve this tricky riddle!")
    print("Tim's mom has 4 sons, Red, Orange, and Yellow.")
    answer = input("What is the fourth son's name?: ")
    if answer == "Tim":
        print("Yes, you're clever. Now you can go into the pool.")
        p.Pool()
    else:
        print("Wrong.")


def west():
    print("You're back in the lobby")
    l.Lobby()


dir = [north, south, east, west]