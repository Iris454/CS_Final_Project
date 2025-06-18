###############################################################################
#Title: Hotel Escape Room Game
#Assignment: Final Project
#Class: CS30
#Date: 6/17/2025
#Name: Iris and Hargun
###############################################################################
'''
In this game, the player will try to escape from the hotel by solving
puzzles and finding items along the way. The puzzles we have include sudoku,
ridules, and calculus problems etc.
The player will start at the lobby, and he/she will enters the restaurant, 
the pool, and take an elevator to go up to the second floor, where he/she will 
see Room103 and Room104. The player will find the last piece of key fragment 
to the main door in Room104, then he/she will successfully escape the hotel.
'''
###############################################################################
import Lobby as l


name = input("Hi, what's your name! ")
print(f"Hi {name}! Thank you for playing my Escpae Room Game!")

# Background Story
print("The year is 1957. A storm brews over the Atlantic, and the wind "
      + "howls like a warning through the pines. \n"
        "You have arrived at the junction of the city and the mountains to visit a friend. \n" 
        "Suddenly, a building resembling an ancient castle catches your attention. \n"
        "Coming closer, you see the name —— Cliffside Hotel, \n"
        "a once-grand retreat for the wealthy elite, now left to decay at the edge of the world. \n" 
        "Out of curiosity, you walk in. \n" 
        "The storm slams the door shut behind you with a thunderous crack. \n" 
        "You try to open the door, but it's locked. \n"
        "Find a way to escape the Cliffside Hotel. Good luck! \n")

# Call lobby method from Lobby module
l.lobby()

