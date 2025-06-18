####################################################################################
#Module Name: Map
'''
Description: Maps of the first floor and the second floor of the hotel.
We used tabulate for formatting.
'''
####################################################################################

from tabulate import tabulate

first_floor = [[None, "elevator", None], ["lobby", "restuarant", "pool"]]
second_floor = [["elevator", "Room103"], [None, "Room104"]]


'''Use tabulate to print out first-floor and second-floor maps'''
def map():
    print("first floor:")
    print(tabulate(first_floor, tablefmt = "fancy_grid"))
    print("second floor:")
    print(tabulate(second_floor, tablefmt = "fancy_grid"))