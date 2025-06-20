####################################################################################
#Module Name: Room2
'''
Description: Room2 refers to Room104, which requires the Room104 Key to enter.
After entering, the player will only see a locked box. The player needs to use the 
UV Torch from the bag to see the hidden password inside the room.
Using the password, the player opens the box, finds the last piece of key fragment,
and successfully escapes the hotel. 
'''
####################################################################################

import Bag as b
import Countdown as c

'''
After entering Room104, first step we have a room description. Then the player will be asked to get the bag
and grab the UV Torch from the bag to see the hidden password in the room. Then he/she will be able to open
a locked box, find the last piece of key fragment, and escape the hotel.
'''
def room2():
    # room description
    print("The room smells of smoke. A rusted ceiling fan turns slowly above, barely moving the air."\
            " Yellowed lace curtains hang over a single, cracked window, filtering the dim light from the street outside."\
            " An old rotary phone sits on the nightstand beside a chipped lamp. The bed is lumpy and uneven, its sheets faded.")
    print()
    print("In this room, you only see a locked box with a four-digit password.")
    while True:
        choice = input("What do you do now?: ")
        if "bag" in choice.lower().split():
            while True:
                b.check()
                print("Which item do you want to use now?")
                ans = int(input("choose a number: "))
                if ans > 0 and ans <= len(b.bag):
                    if b.bag[ans-1] == "UV Torch":
                        print("Using the UV Torch, you see the hidden password: 3421.")
                        print("Hooray, you get the last piece of key fragment! You escape the hotel!") # win!!!
                        print("Thank you for playing my game!")
                        break
                    else:
                        print("This item is not useful now. Please pick again.")
                else:
                    print("Pleae pick a number labeled in front of the items.")
            break
        else:
            print("Hint: type out the thing that you have along the way.")



'''a function that requires the player to use Room104 Key in the bag to open the Room104 door'''
def entering():
    print("Walking ...")
    c.countdown(2)
    print()
    print("You walk up to the door of Room 104. What do you do now?")
    while True:
        try:
            print("1. go over the items in your bag")
            print("2. keep walking")
            choice = int(input("choice (1/2): "))
            if choice == 1:
                while True:
                    b.check() # go over the items in the bag
                    print("Which item do you want to use now?")
                    ans = int(input("choose a number: "))
                    if ans > 0 and ans <= len(b.bag):
                        if b.bag[ans-1] == "Room104 Key":
                            print("You use the key to unlock the door. You enter Room 104")
                            room2()
                            break
                        else:
                            print("This item is not useful now. Please pick again.")
                    else:
                        print("Pleae pick a number labeled in front of the items.")
                break
            elif choice == 2:
                print("All the doors are locked. You can't go anywhere. Please choose again.")
            else:
                print("Please choose 1 or 2.")
        except:
            print("Please type a single digit.")
