
descriptions = {"lobby": "A big room with a grand red carpet leading down to the reception desk." \
                " Classy and sopisticated. It seems perfect at first glance, but with a closer look somthing seems off.",   
                "pool": "A dull and dark pool area, with beach chairs set along the edge. The stack of unused towels in the corner, "/
                "gives the sense that somthings wrong. When was the last time this pool was used? ", 
                "restaurant": "The lights are dim, long shadows across the open space where tables are neatly arranged." \
                        " Each set with folded napkins, polished dishes, and gleaming cutlery, prepared, but untouched." \
                        " A crystal chandelier sways gently in a draft that seems to come from nowhere," \
                        " though not a single window is open. The room is silent, as if time itself  is paused.", 
                "elevator": "The floor creeks of the old elevator, there are only 2 buttons, 1 and 2. Be carefull, it might break down.", 
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


