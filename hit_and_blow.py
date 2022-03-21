#show board
#play game
#check win
    #boardAi = board
#reset

import random

nugget = ["Red", "Blue", "Yellow", "Green", "Pink", "White"]
board_ai = ["-", "-", "-", "-"]
board = ["-", "-", "-", "-"]

game_still_going = True
tries = 5
hit, blow, guess_number, serial = 0, 0, 0, 0

def generator():

    board_ai[0] = nugget[random.randrange(0, 6)]
    board_ai[1] = nugget[random.randrange(0, 6)]
    board_ai[2] = nugget[random.randrange(0, 6)]
    board_ai[3] = nugget[random.randrange(0, 6)]

    #Color Wont Repeat

    while board_ai[1] == board_ai[0]:
        board_ai[1] = nugget[random.randrange(0, 6)]

    while board_ai[2] == board_ai[0] or board_ai[2] == board_ai[1]:
        board_ai[2] = nugget[random.randrange(0, 6)]

    while board_ai[3] == board_ai[0] or board_ai[3] == board_ai[1] or board_ai[3] == board_ai[2]:
        board_ai[3] = nugget[random.randrange(0, 6)]

def showboard():

    print(f"[ '{board[0]}' , '{board[1]}' , '{board[2]}' , '{board[3]}' ]     ||     [Red, Green, Blue, Yellow, Pink, White]")

def player_turn():

    global guess_number
    global game_still_going
    global tries
        
    if tries > 0: 
        print(f"Lives: {tries} left")
        for slot in board:
            while slot == "-":
                slot = input(f"Say Color Number {guess_number + 1}: ").capitalize()
                if slot in nugget:
                    board[guess_number] = slot
                    nugget.remove(slot)
                    pass 
                else:
                    slot = "-"
            guess_number += 1

        hits()          ##
        blows()         ##
        print(f"\n{board}    <-- Your Guess\n") 
        print(f"{hit} Hit(s)")      
        print(f"{blow} Blow(s)\n")  
        
    elif tries < 0:
        game_still_going = False

def hits():

    global hit

    if board_ai[0] == board[0]:
        hit += 1
    if board_ai[1] == board[1]:
        hit += 1
    if board_ai[2] == board[2]:
        hit += 1
    if board_ai[3] == board[3]:
        hit += 1
    return hit

def blows():
    
    global blow

    if board[0] == board_ai[1] or board[0] == board_ai[2] or board[0] == board_ai[3]:
        blow += 1
    if board[1] == board_ai[0] or board[1] == board_ai[2] or board[1] == board_ai[3]:
        blow += 1
    if board[2] == board_ai[0] or board[2] == board_ai[1] or board[2] == board_ai[3]:
        blow += 1
    if board[3] == board_ai[0] or board[3] == board_ai[1] or board[3] == board_ai[2]:
        blow += 1
    return blow

def win_loss():

    global game_still_going

    if board_ai[0] == board[0] and board_ai[1] == board[1] and board_ai[2] == board[2] and board_ai[3] == board[3]:
        print("You Won!\n")
        print(f"{board_ai}   <-- Answer")
        print("\nThanks For Playing!")
        game_still_going = False

    if tries == 0:
        print("You Lost!\n")
        print(f"{board_ai}   <-- Answer")
        print("\nThanks For Playing!")
        game_still_going = False

def reset():

    # Dont delete any of these, dumbass (Note to self)

    global guess_number
    global hit
    global blow
    global tries
    global board
    global nugget

    tries -= 1
    if hit != 4:
        hit = 0
    blow, guess_number = 0, 0
    board = ["-", "-", "-", "-"]
    nugget = ["Red", "Blue", "Yellow", "Green", "Pink", "White"]

def playgame():

    global tries
    global hit
    global blow

    generator()         ##
    
    print("Welcome To Hit & Blow!\n")

    print("How To Play: A pattern of four color combination has been generated. Try and guess all the colors (out of the six) in the right order. \n             Hit = The Color is in the Correct Spot\n             Blow = The color is in the pattern but in the wrong spot.\n")

    while game_still_going:

        showboard()     ##

        player_turn()   ##

        win_loss()      ##

        reset()         ##

playgame()              ##