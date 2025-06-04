from tabulate import tabulate

first_floor = [[None, "elevator", None], ["lobby", "restuarant", "pool"]]
second_floor = [["elevator", "Room103"], [None, "Room104"]]

def map():
    print("first floor:")
    print(tabulate(first_floor, tablefmt = "fancy_grid"))
    print("second floor:")
    print(tabulate(second_floor, tablefmt = "fancy_grid"))