import math


# Converting binary number to index location
def binary_to_index(b: int):
    """
    Convert a binary number to an index location.

    Parameters:
    b (int): The binary number to be converted.

    Returns:
    int: The converted index location.
    """
    return int(math.log2(b))


class Board:
    """
    Represents a Tic Tac Toe board.

    Attributes:
    x_pos (int): The position of X on the board.
    o_pos (int): The position of O on the board.
    turn (bool): True for X player, False for O player.
    move_stack (list): A list to keep track of the moves made.
    game_end (bool): Indicates whether the game has ended.
    winner (bool): True if X wins, False if O wins.
    print (bool): Flag for printing the board.
    win_masks (list): List of masks for winning positions.

    Methods:
    make_move(index, display): Make a move at the specified index.
    undo_move(display): Undo the last move.
    update(display): Update the game status.
    get_moves(): Get available moves.
    print_indexes(): Print the index locations on the board.
    __str__(): String representation of the board.
    """

    def __init__(self, x_pos=0, o_pos=0):
        """
        Initialize the Board with specified X and O positions.

        Parameters:
        x_pos (int): The position of X on the board.
        o_pos (int): The position of O on the board.
        """
        self.x_pos = x_pos
        self.o_pos = o_pos
        self.turn = True  # true is x player, false is o player
        self.move_stack = []
        self.game_end = False
        self.winner = None
        self.print = False

        self.win_masks = [
            1 << 0 | 1 << 1 | 1 << 2,
            1 << 3 | 1 << 4 | 1 << 5,
            1 << 6 | 1 << 7 | 1 << 8,
            1 << 0 | 1 << 3 | 1 << 6,
            1 << 1 | 1 << 4 | 1 << 7,
            1 << 2 | 1 << 5 | 1 << 8,
            1 << 0 | 1 << 4 | 1 << 8,
            1 << 2 | 1 << 4 | 1 << 6,
        ]

        self.update()

    def make_move(self, index: int, display=False):
        """
        Make a move at the specified index.

        Parameters:
        index (int): The index where the move is made.
        display (bool, optional): Flag for displaying the board. Defaults to False.
        """
        if self.game_end:
            raise Exception("Game is finished, further moves cannot be made")
        if self.taken_pos & 1 << index != 0:
            raise ValueError("Index already taken")
        if index < 0 or index > 8:
            raise ValueError("Index outside of range 0-8")

        if self.turn:  # placing x
            self.x_pos += 1 << index
        else:  # placing o
            self.o_pos += 1 << index

        self.turn = not self.turn

        if display:
            print(self)

        self.update()

        self.move_stack.append(index)

    def undo_move(self, display=False):
        """
        Undo the last move.

        Parameters:
        display (bool, optional): Flag for displaying the board. Defaults to False.
        """
        if self.move_stack == []:
            raise Exception("Cannot Undo when no moves have been made")

        index = self.move_stack[-1]
        self.move_stack.remove(index)

        if self.turn:  # last move was O
            self.o_pos -= 1 << index
        else:  # last move was X
            self.x_pos -= 1 << index

        self.game_end = False
        self.winner = None
        self.turn = not self.turn

        if display:
            print(self)

        self.update()

    def update(self, display=False):
        """
        Update the game status.

        Parameters:
        display (bool, optional): Flag for displaying the board. Defaults to False.
        """
        self.taken_pos = self.x_pos | self.o_pos

        if self.turn:  # o was just placed
            for mask in self.win_masks:
                if mask & self.o_pos == mask:
                    self.game_end = True
                    self.winner = False
                    if display:
                        print("Game Over: O wins")
                    return
        else:  # x was just placed
            for mask in self.win_masks:
                if mask & self.x_pos == mask:
                    self.game_end = True
                    self.winner = True
                    if display:
                        print("Game Over: X wins")
                    return

        if self.taken_pos == 511:  # all positions are left
            if display:
                print("Game Over: Draw")
            self.game_end = True

    def get_moves(self):
        """
        Get available moves on the board.

        Returns:
        list: List of available moves.
        """
        out = []
        if self.game_end:
            return out
        for i in range(9):
            if 1 << i & self.taken_pos == 0:
                out.append(i)

        return out

    def print_indexes(self):
        """Print the index locations on the board."""
        print("Index Locations to Play:")
        print("|0|1|2|")
        print("|3|4|5|")
        print("|6|7|8|")

    def __str__(self):
        """
        Get the string representation of the board.

        Returns:
        str: The string representation of the board.
        """
        con = "{:9b}"
        x_pos = con.format(self.x_pos)
        o_pos = con.format(self.o_pos)

        rows = ["-------"]

        r = ""
        for i in range(9):
            r += "|"
            if x_pos[i] == "1":
                r += "X"
            elif o_pos[i] == "1":
                r += "O"
            else:
                r += " "

            if (i + 1) % 3 == 0:
                r += "|"
                rows.append(r[::-1])
                r = ""

        return "\n".join(rows[::-1])
