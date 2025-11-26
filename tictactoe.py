# tictactoe app with command line interface
# kelompok uRAH
import os

PLAYER_FIRST_ROUND = "none"
PLAYER_ONE = "O"
PLAYER_TWO = "X"
#this dict will be modified later, hence not UPPER_SNAKE_CASE
tictactoe_space = {
    "block_one": "1", #top left
    "block_two": "2", #top center
    "block_three": "3", #top right
    "block_four": "4", #middle left
    "block_five": "5", #middle center
    "block_six": "6", #middle right
    "block_seven": "7", #bottom left
    "block_eight": "8", #bottom center
    "block_nine": "9" #bottom right
}
current_player_turn = PLAYER_FIRST_ROUND


def clear_output():
    """
    Clears the command line output on use
    """
    os.system('cls')


def tictactoe_visual():
    """
    Displays the tictactoe board
    """
    display_one = tictactoe_space["block_one"] #workaround of fstring not liking multiple brackets
    display_two = tictactoe_space["block_two"]
    display_three = tictactoe_space["block_three"]
    display_four = tictactoe_space["block_four"]
    display_five = tictactoe_space["block_five"]
    display_six = tictactoe_space["block_six"]
    display_seven = tictactoe_space["block_seven"]
    display_eight = tictactoe_space["block_eight"]
    display_nine = tictactoe_space["block_nine"]
    print(f"=============\n-------------\n| {display_one} | {display_two} | {display_three} |\n-------------\n| {display_four} | {display_five} | {display_six} |\n-------------\n| {display_seven} | {display_eight} | {display_nine} |\n-------------\n=============")


def tictactoe_player_control():
    global current_player_turn
    #first round and alternating player logic
    if current_player_turn == PLAYER_FIRST_ROUND:
        current_player_turn = PLAYER_ONE
        player_name = "1"
    elif current_player_turn == PLAYER_ONE:
        current_player_turn = PLAYER_TWO
        player_name = "2"
    elif current_player_turn == PLAYER_TWO:
        current_player_turn = PLAYER_ONE
        player_name  = "1"
    print(f"Current player's turn = Player {player_name} ({current_player_turn})")


def tictactoe_win_detection():
    """
    Checks if either Player 1 or Player 2 won or a draw is decided. 
    """
    #Player 1 check
    #horizontal
    if tictactoe_space["block_one"] == PLAYER_ONE and tictactoe_space["block_two"] == PLAYER_ONE and tictactoe_space["block_three"] == PLAYER_ONE:
        return PLAYER_ONE
    elif tictactoe_space["block_four"] == PLAYER_ONE and tictactoe_space["block_five"] == PLAYER_ONE and tictactoe_space["block_six"] == PLAYER_ONE:
        return PLAYER_ONE
    elif tictactoe_space["block_seven"] == PLAYER_ONE and tictactoe_space["block_eight"] == PLAYER_ONE and tictactoe_space["block_nine"] == PLAYER_ONE:
        return PLAYER_ONE
    #vertical
    elif tictactoe_space["block_one"] == PLAYER_ONE and tictactoe_space["block_four"] == PLAYER_ONE and tictactoe_space["block_seven"] == PLAYER_ONE:
        return PLAYER_ONE
    elif tictactoe_space["block_two"] == PLAYER_ONE and tictactoe_space["block_five"] == PLAYER_ONE and tictactoe_space["block_eight"] == PLAYER_ONE:
        return PLAYER_ONE
    elif tictactoe_space["block_three"] == PLAYER_ONE and tictactoe_space["block_six"] == PLAYER_ONE and tictactoe_space["block_nine"] == PLAYER_ONE:
        return PLAYER_ONE
    #diagonal
    elif tictactoe_space["block_one"] == PLAYER_ONE and tictactoe_space["block_five"] == PLAYER_ONE and tictactoe_space["block_nine"] == PLAYER_ONE:
        return PLAYER_ONE
    elif tictactoe_space["block_three"] == PLAYER_ONE and tictactoe_space["block_five"] == PLAYER_ONE and tictactoe_space["block_seven"] == PLAYER_ONE:
        return PLAYER_ONE

    #player 2 check
    elif tictactoe_space["block_one"] == PLAYER_TWO and tictactoe_space["block_two"] == PLAYER_TWO and tictactoe_space["block_three"] == PLAYER_TWO:
        return PLAYER_TWO
    elif tictactoe_space["block_four"] == PLAYER_TWO and tictactoe_space["block_five"] == PLAYER_TWO and tictactoe_space["block_six"] == PLAYER_TWO:
        return PLAYER_TWO
    elif tictactoe_space["block_seven"] == PLAYER_TWO and tictactoe_space["block_eight"] == PLAYER_TWO and tictactoe_space["block_nine"] == PLAYER_TWO:
        return PLAYER_TWO
    #vertical
    elif tictactoe_space["block_one"] == PLAYER_TWO and tictactoe_space["block_four"] == PLAYER_TWO and tictactoe_space["block_seven"] == PLAYER_TWO:
        return PLAYER_TWO
    elif tictactoe_space["block_two"] == PLAYER_TWO and tictactoe_space["block_five"] == PLAYER_TWO and tictactoe_space["block_eight"] == PLAYER_TWO:
        return PLAYER_TWO
    elif tictactoe_space["block_three"] == PLAYER_TWO and tictactoe_space["block_six"] == PLAYER_TWO and tictactoe_space["block_nine"] == PLAYER_TWO:
        return PLAYER_TWO
    #diagonal
    elif tictactoe_space["block_one"] == PLAYER_TWO and tictactoe_space["block_five"] == PLAYER_TWO and tictactoe_space["block_nine"] == PLAYER_TWO:
        return PLAYER_TWO
    elif tictactoe_space["block_three"] == PLAYER_TWO and tictactoe_space["block_five"] == PLAYER_TWO and tictactoe_space["block_seven"] == PLAYER_TWO:
        return PLAYER_TWO

    #Draw Check
    elif tictactoe_space["block_one"] != "1" and tictactoe_space["block_two"] != "2" and tictactoe_space["block_three"] != "3" and tictactoe_space["block_four"] != "4" and tictactoe_space["block_five"] != "5" and tictactoe_space["block_six"] != "6" and tictactoe_space["block_seven"] != "7" and tictactoe_space["block_eight"] != "8" and tictactoe_space["block_nine"] != "9":
        return "DRAW"
    
    #Continue Check (aka game continues)
    else:
        return "ONGOING"


def tictactoe_start():
    """
    Main function, controls the game flow
    """
    #resets the game, cleaning it of leftover stuff as well as defining the stuff used
    print("initializing...")
    tictactoe_running = "ONGOING"
    global current_player_turn
    global tictactoe_space
    current_player_turn = PLAYER_FIRST_ROUND
    tictactoe_space = {
        "block_one": "1", #top left
        "block_two": "2", #top center
        "block_three": "3", #top right
        "block_four": "4", #middle left
        "block_five": "5", #middle center
        "block_six": "6", #middle right
        "block_seven": "7", #bottom left
        "block_eight": "8", #bottom center
        "block_nine": "9" #bottom right
    }

    #actual game start
    while tictactoe_running == "ONGOING":
        #main code
        clear_output()
        tictactoe_visual() #displays board
        #checks if the game has ended
        game_condition = tictactoe_win_detection()
        if game_condition == "ONGOING":
            pass
        elif game_condition == PLAYER_ONE:
            print("Player 1 (O) has won the match!")
            tictactoe_running = "END" #just in case
            break
        elif game_condition == PLAYER_TWO:
            print("Player 2 (X) has won the match!")
            tictactoe_running = "END" #just in case
            break
        elif game_condition == "DRAW":
            print("The game has ended in a draw.")
            tictactoe_running = "END" #just in case
            break

        tictactoe_player_control() #sets who's turn to play
        
        print("insert number of the space which you want to fill:")
        while True: #loop to fix user error
            player_input = input()
            #logic 
            if player_input == "1" and tictactoe_space["block_one"] == "1":
                tictactoe_space["block_one"] = current_player_turn
                break
            elif player_input == "2" and tictactoe_space["block_two"] == "2":
                tictactoe_space["block_two"] = current_player_turn
                break
            elif player_input == "3" and tictactoe_space["block_three"] == "3":
                tictactoe_space["block_three"] = current_player_turn
                break
            elif player_input == "4" and tictactoe_space["block_four"] == "4":
                tictactoe_space["block_four"] = current_player_turn
                break
            elif player_input == "5" and tictactoe_space["block_five"] == "5":
                tictactoe_space["block_five"] = current_player_turn
                break
            elif player_input == "6" and tictactoe_space["block_six"] == "6":
                tictactoe_space["block_six"] = current_player_turn
                break
            elif player_input == "7" and tictactoe_space["block_seven"] == "7":
                tictactoe_space["block_seven"] = current_player_turn
                break
            elif player_input == "8" and tictactoe_space["block_eight"] == "8":
                tictactoe_space["block_eight"] = current_player_turn
                break
            elif player_input == "9" and tictactoe_space["block_nine"] == "9":
                tictactoe_space["block_nine"] = current_player_turn
                break
            else:
                print("Can't accept input. Either the position is already taken or the input is invalid. try inputting again.")

#Loop untuk main lagi atau tidak
while True:
    print("Welcome to TicTacToe\nInsert the number corresponding to the action:\n1 - Play\n2 - Ruleset\n3 - Exit")
    user_input_mode = input()
    if user_input_mode == "1":
        playing = True
        while playing == True:
            tictactoe_start()
            # Setelah permainan selesai, tanya apakah ingin main lagi 
            while True :
                play_again = input ("Do you want to play again?  (y = play again / n = return to menu): ").lower()
                if play_again == 'y' :
                    break #main  lagi
                elif play_again == 'n':
                    playing = False
                    break        
                else:
                    print("Invalid input. Please enter 'y' for yes or 'n' for no." )
    elif user_input_mode == "2":
        clear_output()
        print("=========\n1. Find an opponent and determine who goes first \n2. One player plays X's and the other plays O's\n3. Players take turns marking a space in a 3X3 grid\n4. The player that places 3 of their marks in a horizontal, vertical or diagonal row wins the game\n=========")
    elif user_input_mode == "3":
        clear_output()
        print("Thanks for playing!")
        exit()
    else:
        clear_output()
        print("Invalid input. Please enter the number listed." )
#play the game

#tictactoe_start()
