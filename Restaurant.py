import Move as m
import Elevator as e
import Pool as p
import Bag as b
import Countdown as c

eat = True
flag = True


def north():
    global flag
    print("That way is the elevator.")
    if eat or "UV Torch" not in b.bag:
        print("Please visit other places first before leaving the restuarant in elevator.")
    else:
        while True:
            print("To go into the elevator you have to solve this easy riddle!")
            print("I have keys, but no locks, I have a space, but no room. You can enter, but can't go outside.")
            answer = input("What am I?: ")
            if answer == "keyboard" or "Keyboard": 
                print("Congratulations, you have solved it, very intelligent.")
                flag = False
                e.elevator()
                break
            else:
                print("No, that is wrong.")


def south():
    if "UV Torch" in b.bag:
        print("You've collected the UV Torch.")
        return
    
    print("Under a table, you find a purple UV Torch. You collect it.")
    b.bag.append("UV Torch")

def east():
    global eat

    if not eat:
        print("You have visited the pool. You don't need to go there again.")
        return
    
    print("That's the pool, to go there you have to solve this tricky riddle!")
    while True:
        print("Tim's mom has 4 sons, Red, Orange, and Yellow.")
        answer = input("What is the fourth son's name?: ")
        if answer == "Tim":
            print("Yes, you're clever. Now you can go into the pool.")
            print("Walking ...")
            c.countdown(3)

            eat = False
            p.pool()
            
            print("Walking ...")
            c.countdown(3)
            print("You are back at the restuarant.")
            break
        else:
            print("Wrong.")


def west():
    print("You've already collected everything from the lobby, you don't need to go that way.")

dir = [north, south, east, west]

def restaurant():
    print()
    print("Now you are in the restuarant ------")
    while flag:
        direction = m.move()
        dir[direction]()
