from engine import Board
from opponent import random_bot, monte_carlo
import time

# future only have one function to play the game
# allows inputs of player / bot to input 1 / 2


def dynamic_print(text: str, speed=50):
    """
    Print text dynamically with a specific speed.

    Parameters:
    text (str): The text to be printed dynamically.
    speed (int, optional): The speed of the printing. Defaults to 50.
    """
    for i in range(len(text)):
        print(text[: i + 1], end="\r")
        time.sleep(1 / speed)

    print(text)


def ask_which_bot():
    """
    Asks the user to choose the difficulty of the bot.

    Returns:
    function: A function representing the chosen bot.
    """
    dynamic_print("Choose a difficulty of bot (0-9)")
    difficulty = ask_user(list(range(10)), int)

    if difficulty == 0:
        return random_bot
    else:
        return lambda board: monte_carlo(board, 2 ** int(difficulty))


def player_vs_player(x_start=True):
    """
    Simulates a game of Tic Tac Toe between two human players.

    Parameters:
    x_start (bool, optional): Determines if 'X' starts the game. Defaults to True.
    """
    game = Board()
    game.turn = x_start
    game.print_indexes()
    while not game.game_end:
        move_made = False
        if game.turn:  # x move
            string = "Index of move for X: "
        else:
            string = "Index of move for O: "

        while not move_made:
            try:
                index = int(input((string)))
                game.make_move(index, True)
                move_made = True
            except Exception as e:
                print(f"Invalid Input: {e}")

    game.update(True)


def player_vs_bot(bot, player_start=True):
    """
    Simulates a game of Tic Tac Toe between a human player and a bot.

    Parameters:
    bot (function): The function representing the bot's move.
    player_start (bool, optional): Determines if the player starts the game. Defaults to True.
    """
    if player_start:
        print("You are playing as X")
    else:
        print("You are playing as O")
    game = Board()
    game.print_indexes()
    while not game.game_end:
        if game.turn == player_start:
            move_made = False
            if game.turn:  # x move
                string = "Index of move for X: "
            else:
                string = "Index of move for O: "

            while not move_made:
                try:
                    index = int(input((string)))
                    game.make_move(index, True)
                    move_made = True
                except Exception as e:
                    print(f"Invalid Input: {e}")

        else:
            bot_index = bot(game)
            print(f"Bot played: {bot_index}")
            game.make_move(bot_index, True)

    game.update(True)


def ask_user(condition: list, dtype=str):
    """
    Prompts the user for input and validates it against a given condition.

    Parameters:
    condition (list): The list of valid inputs.
    dtype (type, optional): The type of the input data. Defaults to str.

    Returns:
    The validated user input.
    """
    out = None
    while out not in condition:
        try:
            out = dtype(input(":"))
        except ValueError as e:
            pass
    return out


if __name__ == "__main__":
    dynamic_print("Welcome to TicTacToe")
    dynamic_print("Please select from the following options: ")
    dynamic_print("- (1) - Player vs Player")
    dynamic_print("- (2) - Player vs Agent")
    game_type = ask_user([1, 2, 3], int)

    if game_type == 1:  # PvP
        player_vs_player()
    elif game_type == 2:  # PvE
        dynamic_print("Do you want to go 1st (1) or 2nd? (2)")

        if ask_user([1, 2], int) == 1:
            turn = True
        else:
            turn = False

        player_vs_bot(ask_which_bot(), turn)
