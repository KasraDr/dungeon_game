import os
import random

# the Position on the grid map (x,y)
CELLS = [
    (0,0), (1,0), (2,0), (3,0), (4,0), (5,0), (6,0), (7,0),
    (0,1), (1,1), (2,1), (3,1), (4,1), (5,1), (6,1), (7,1),
    (0,2), (1,2), (2,2), (3,2), (4,2), (5,2), (6,2), (7,2),
    (0,3), (1,3), (2,3), (3,3), (4,3), (5,3), (6,3), (7,3),
    (0,4), (1,4), (2,4), (3,4), (4,4), (5,4), (6,4), (7,4),
    (0,5), (1,5), (2,5), (3,5), (4,5), (5,5), (6,5), (7,5),
    (0,6), (1,6), (2,6), (3,6), (4,6), (5,6), (6,6), (7,6),
    (0,7), (1,7), (2,7), (3,7), (4,7), (5,7), (6,7), (7,7)
]


# automatically clear the screen
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# generate 3 random location for player, monster and exit door
def get_locations():
    return random.sample(CELLS, 3)

# defines the player's moves
def move_player(player, move):
    x, y = player

    if move == "LEFT":
        x -= 1
    
    if move == "RIGHT":
        x += 1
    
    if move == "UP":
        y -= 1

    if move == "DOWN":
        y += 1

    return x, y

# determines the moves available based on the player position
def get_moves(player):
    moves = ["LEFT", "RIGHT", "UP", "DOWN"]

    x, y = player
    if x == 0:
        moves.remove("LEFT")
    if x == 7:
        moves.remove("RIGHT")
    if y == 0:
        moves.remove("UP")
    if y == 7:
        moves.remove("DOWN")

    return moves

#  creates the grid map by outputing patterns of | and _
def draw_map(player):

    print(" _" * 8)
    tile = "|{}"

    for cell in CELLS:
        x, y = cell
        if x < 7:
            line_end = ""
            if cell == player:  
                output = tile.format("X")
            else:
                output = tile.format("_")
        else:
            line_end = "\n"
            if cell == player:
                output = tile.format("X|")
            else:
                output = tile.format("_|")
        print(output, end=line_end)

# playing...
def play():
    monster, player, door = get_locations()
    playing = True

    while playing:

        clear_screen()

        draw_map(player)
        valid_moves = get_moves(player)
        print("\nYou are currently in room {}".format(player)) 
        print("You can move {}".format(", ".join(valid_moves))) 
        print("Type 'Q' to quit.")
        print()

        move = input(">>> ").upper()

        if move == "Q":
            print("\n ** Come back and play soon! ** \n")
            break

        if move in valid_moves:
            player = move_player(player, move)
            if player == monster:
                print("\n ** Game Over! The monster got you! ** \n")
                playing = False
            
            if player == door:
                print ("\n ** Congrats! You escaped! ** \n")
                playing = False
        else:
            input("\n *** Ouch! Watch out for walls! ** \n")
    else:
        if input("Play again? (y/n): ").lower == "y":
            play()
        else:
            print("Good luck!")
        

play()