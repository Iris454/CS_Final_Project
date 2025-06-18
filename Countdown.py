####################################################################################
#Module Name: Countdown
'''
Description: the countdown timer creates a time interval before the next code segment 
appears, which works with the code "print("walking...")" to simulate the feeling of 
the player walking.
'''
####################################################################################

import time

'''create a time interval of t seconds before the next code segment appears'''
def countdown(t):
    while t:
        time.sleep(1)
        t -= 1