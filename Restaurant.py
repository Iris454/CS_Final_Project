####################################################################################
#Module Name: Restaurant
'''
Description: In the restaurant, the player will see an elevator door, several tables,
a locked door to the swimming pool, and a door to the lobby, located at the north, 
south, east, and west side of the restaurant respectively. A UV Torch can be collected
under the tables. The player is not allowed to return to the lobby. The player needs 
to solve riddles to take the elevator or go to the pool.
'''
####################################################################################

import Move as m
import Elevator as e
import Pool as p
import Bag as b
import Countdown as c

swim = False
flag = True


'''
Here is the elevator. The player needs to solve a riddle to take the elevator.
In addition, the player is not allowed to take the elevator and leave the 
restaurant until he/she collects the items(UV Torch) and has visited the pool.
'''
def north():
    global flag
    print("That way is the elevator.")
    if not swim or "UV Torch" not in b.bag: 
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


'''
Collect UV Torch and place it in the bag.
The player is not allowed to collect it twice.
'''
def south():
    # if already collected the UV Torch, we don't let the player collect it again.
    if "UV Torch" in b.bag: 
        print("You've collected the UV Torch.")
        return
    
    # Collect UV Torch and place it in the bag
    print("Under a table, you find a purple UV Torch. You collect it.")
    b.bag.append("UV Torch")


'''
Here is the door to the swimming pool. The player needs to solve a ridule to enter
the swimming pool. The player is not allowed to visit the pool twice.
'''
def east():
    global swim

    # if already visited the pool, we don't let the player collect it again.
    if swim:
        print("You have visited the pool. You don't need to go there again.")
        return
    
    # solve a riddle to enter the pool
    print("That's the pool, to go there you have to solve this tricky riddle!")
    while True:
        print("Tim's mom has 4 sons, Red, Orange, and Yellow.")
        answer = input("What is the fourth son's name?: ")
        if answer == "Tim":
            #walk to the pool from the restaurant
            print("Yes, you're clever. Now you can go into the pool.")
            print("Walking ...")
            c.countdown(3)

            swim = True # meaning that the player has visited the pool
            p.pool()
            
            #return to the restaurant from the pool
            print("Walking ...")
            c.countdown(3)
            print("You are back at the restuarant.")
            break
        else:
            print("Wrong.")


'''
Here is the door to the lobby, which is also where the player comes into the restaurant. 
The player is not allowed to return to the lobby.
'''
def west():
    print("You've already collected everything from the lobby, you don't need to go that way.")


dir = [north, south, east, west]

'''
Main restaurant function that gives a description of the restaurant and leads the player
to different directions by calling the 4 direction methods above.
'''
def restaurant():

    # room description of the restaurant
    print()
    print("Now you are in the restuarant ------")
    print("The lights are dim, shadows across the open space where tables are neatly arranged. \n" 
            " Each set with folded napkins, polished dishes, and cutlery, prepared, but untouched.\n" 
            " A crystal chandelier sways gently in a draft that seems to come from nowhere,\n" 
            " though not a single window is open. The room is silent.")
    print()
    
    # a while loop that keeps asking the player which direction they want to go 
    # until the player enters the elevator and leaves the restaurant
    while flag:
        direction = m.move()
        dir[direction]()
