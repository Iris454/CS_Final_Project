####################################################################################
#Module Name: Elevator
'''
Description: The player takes the elevator to go up to the second floor, and he/she
will see Room103. The player needs to get Room103 Key from the bag to enter the room.
'''
####################################################################################

import Bag as b
import Room1 as r
import Countdown as c

'''
An elevator function that tells the player that he/she moves up to the second floor
and lets he/she use Room103 Key in the bag to enter the room.
'''
def elevator():
    # the player takes the elevator to go up to the second floor
    print()
    c.countdown(2)
    print("Ding! The elevator is here. \n"
          "The floor creeks of the old elevator, there are only 2 buttons, \n"
          "1 and 2. Be carefull, it might break down.")
    print()
    print("You move up to the second floor")
    print()
    print("The door is open. You walk out of the elevator.  \n" 
        "Room103 is right in front of you, but it's locked.  \n"
        "What do you do now?")


    while True:
        try:
            # the player needs to choose 1 to get Room103 Key from the bag to enter the room
            print("1. go over the items in your bag")
            print("2. keep walking")
            choice = int(input("choice (1/2): "))
            if choice == 1:
                while True:
                    try:
                        b.check() # a function in the bag module that go over all the items in the bag
                        print("Which item do you want to use now?")
                        ans = int(input("choose a number: "))
                        if ans > 0 and ans <= len(b.bag):
                            if b.bag[ans-1] == "Room103 Key":
                                print("You use the key to unlock the door.")
                                r.room1() # enter Room103
                                break
                            else:
                                print("This item is not useful now. Please pick again.")
                        else:
                            print("Pleae pick a number labeled in front of the items.")
                    except: #catch the error if the player input is not an integer
                        print("Please type a number.")
                break
            elif choice == 2:
                print("All the doors are locked. You can't go anywhere. Please choose again.")
            else:
                print("Please choose 1 or 2.")
        except: #catch the error if the player input is not an integer
            print("Please type a number.")

    
