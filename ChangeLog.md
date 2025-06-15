# Development Work

## Initial Plan
1. Create main and room modules (lobby, restaurant, pool, elevator, room1, room2, gym)
2. Write settings and room descriptions in the main module
3. Create a room method and 4 directions methods for each room module
4. Create a separate bag module, which contains all the items collected along the way.
5. Create a separate move module, which contains a move method that returns which direction the player chooses to go.
6. Import move module in every room module, and call the move method in every room method, so that the player can walk in all directions in the room.
7. Connect the move method with the 4 direction methods using a direction list: [north, south, west, east], so that each direction method can be called with the index returned by the move method.
8. Call lobby method in main so that the player starts the game in the lobby.
9. Once the player enters a room, he/she can't leave the room without finding all the hidden items, nor return to the previous room. \
   (e.g. if not visited pool or key1 not in bag: print("Please look around in this room."); else: print("You may leave the room").)
10. In the lobby, we will have a reception desk, which gives player the key to room1, and a calculus question, which gives player the password to open the door to the restuarant.
11. In the restuarant, we will have two word puzzles and the player will find a UV Torch under a table. The two word puzzles lead to the pool and the elevator respectively.
12. In the pool, the player will collect Key Fragment1 and solve a word puzzle to return to the restuarant.
13. The player will take the elevator to move the second floor.
14. The player will use the room1 key stored in the bag to enter room1.
15. In room1, we will have a sudoku, which gives player the password to open a locked box to get Key Fragment2 and room2 key.
16. They player will use the room2 key to enter room2, which is the last room we have.
17. In room2, the player will use the UV Torch stored in the bag to find a hidden password to open a locked box. The player will collect the last piece of Key Fragment and escape the hotel.


## Checklist
- [ ] Create modules and the basic structure in each room module (1 room method + 4 direction methods) (Iris)
- [ ] Code the move method that returns which direction the player chooses to go. (Iris)
- [ ] Fill in Lobby module. (Iris)
- [ ] Fill in Restaurant module. (Hargun)
- [ ] Fill in Pool Module. (Hargun)
- [ ] Fill in Elevator Module. (Iris)
- [ ] Fill in Room1 Module. (Iris)
- [ ] Fill in Room2 Module. (Iris)
- [ ] Write descriptions for all rooms. (Hargun)
- [ ] Create beta testing survey. (Hargun)
- [ ] Check for errors and modify. (Iris and Hargun)

## Version History


## Timeline
- May 21: Finish writing the proposal
- May 23: Create a basic structure (module, methods ...) and code the move method
- May 26: Finish coding Lobby Module
- May 28: Finish coding Restaurant Module
- May 30: Finish coding Elevator Module
- June 2: Finish coding Room1 and Pool Module
- June 3: Finish coding Room2 Module
- June 4: Write a setting and descriptions in the main module
- June 5-6: Modify - make sure no errors occur while running the project
- June 9: Create a survey for Beta Testing.
- June 10: Beta Testing Day - play others' games and give feedbacks
- June 11-13: Fix errors and improve our code. 
