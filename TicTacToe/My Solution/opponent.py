from engine import Board
import random


def random_bot(board: Board):
    """
    Generates a random move for the bot based on the available moves.

    Parameters:
    board (Board): The current state of the board.

    Returns:
    int: The randomly chosen move.
    """
    return random.choice(board.get_moves())


def monte_carlo(board: Board, n: int):
    """
    Uses the Monte Carlo method to make an informed move based on multiple simulated games.

    Parameters:
    board (Board): The current state of the board.
    n (int): The number of simulations to run.

    Returns:
    int: The move chosen based on the Monte Carlo simulations.
    """
    moves = board.get_moves()
    wins = []
    for move in moves:
        board.make_move(move)
        win = 0
        for i in range(n):
            moves_made = 0
            while board.game_end == False:
                board.make_move(random_bot(board))
                moves_made += 1

            if board.winner:  # X wins
                win += 1
            elif board.winner == False:
                win += -1

            # reset board
            for _ in range(moves_made):
                board.undo_move()

        board.undo_move()
        wins.append(win)

    if board.turn:
        best_index = wins.index(max(wins))
    else:
        best_index = wins.index(min(wins))
    return moves[best_index]
