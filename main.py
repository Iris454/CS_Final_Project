
descriptions = {"lobby": "",   
                "pool": "", 
                "restaurant": "", 
                "gym": "", 
                "elevator": "", 
                "room1": "", 
                "room2": ""}

import Lobby as l

name = input("Hi, what's your name! ")
print(f"Hi {name}! Thank you for playing my Escpae Room Game!")
print("The year is 1957. A storm brews over the Atlantic, and the wind howls like a warning through the pines." \
        "You have arrived at the junction of the city and the mountains to visit a friend." \
        "Suddenly, a building resembling an ancient castle catches your attention." \
        "Coming closer, you see the name —— Cliffside Hotel," \
        "a once-grand retreat for the wealthy elite, now left to decay at the edge of the world." \
        "Out of curiosity, you walk in." \
        "The storm slams the door shut behind you with a thunderous crack." \
        "You try to open the door, but it's locked." \
        "Find a way to escape the Cliffside Hotel. Good luck!")
print(descriptions["lobby"])
l.lobby()


