####################################################################################
#Module Name: Bag
'''
Description: the bag list allows the player to store the items that he/she collects
along the way and the check method is called everytime the player needs to use an
item from the bag. 
'''
####################################################################################

bag = []

# allow the player to go over all the items in the bag
def check():
    for idx in range(0, len(bag)):
        print(f"{idx+1}. {bag[idx]}")
