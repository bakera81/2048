import random
import numpy as np
import copy

class Board(object):

    def __init__(self, board=None):
        if board is None:
            self.board = np.array([[0,0,0,0],
                                   [0,0,0,0],
                                   [0,0,0,0],
                                   [0,0,0,0]])
        else:
            self.board = copy.copy(board.board)


    def zeros(self):
        """
            Returns an array of tuples of the x,y coordinates of zeros on the board.
        """
        output = []
        for y, row in enumerate(self.board):
            for x, col in enumerate(row):
                if col == 0:
                    output.append((x, y))
        if len(output) == 0:
            print('GAME OVER')
            raise
        return output


    def next(self):
        """
            Adds a 2 or a 4 to open spaces on the board at random.
        """
        val = random.choice([2,4])
        loc = random.choice(self.zeros())
        self.board[loc[1], loc[0]] = val

# TODO: handle mutlidigit numbers better
# TODO: use curses (for better terminal printing)
    def show(self):
        """
            Prints the board to the console.
        """
        # +---------------+
        # | x | x | x | x |
        # | x | x | x | x |
        # | x | x | x | x |
        # | x | x | x | x |
        # +---------------+
        output = '+---------------+\n'
        for row in self.board:
            output += '| {0} | {1} | {2} | {3} |\n'.format(*row)
        output += '+---------------+\n'
        print(output)

    # TODO: Use numpy to do all rows at once
    def shift(self, row):
        """
            Returns an array representing a row or column that has been shifted.
            It will join all numbers that are equal (and eligible to be joined) and will move all numbers to the beginning of the array.
            To shift in the opposite direction, see inverse_shift().
        """
        non_zero_row = [val for val in row if val != 0] # Drop all zeros
        for i in range(len(non_zero_row) - 1): # Combine adjacent if possible
            if non_zero_row[i] == non_zero_row[i + 1]:
                non_zero_row[i] = non_zero_row[i] * 2
                non_zero_row[i + 1] = 0
        # To shift all elements, drop zeros and repad.
        non_zero_row = [val for val in non_zero_row if val != 0] # Drop all zeros
        row = non_zero_row + [0] * (4 - len(non_zero_row)) # Re-pad with zeros
        return row


    def inverse_shift(self, row):
        """
            Returns an array representing a row or column that has been shifted.
            It will join all numbers that are equal (and eligible to be joined) and will move all numbers to the end of the array.
            To shift in the opposite direction, see shift().
        """
        non_zero_row = [val for val in row if val != 0] # Drop all zeros
        for i in reversed(range(1, len(non_zero_row))): # Combine adjacent if possible
            if non_zero_row[i] == non_zero_row[i - 1]:
                non_zero_row[i] = non_zero_row[i] * 2
                non_zero_row[i - 1] = 0
        # To shift all elements, drop zeros and repad.
        non_zero_row = [val for val in non_zero_row if val != 0] # Drop all zeros
        row = [0] * (4 - len(non_zero_row)) + non_zero_row  # Re-pad with zeros
        return row


    def left(self):
        """
            Shift all rows to the left.
        """
        self.board[0] = self.shift(self.board[0])
        self.board[1] = self.shift(self.board[1])
        self.board[2] = self.shift(self.board[2])
        self.board[3] = self.shift(self.board[3])


    def up(self):
        """
            Shift all columns up.
        """
        self.board[:,0] = self.shift(self.board[:,0])
        self.board[:,1] = self.shift(self.board[:,1])
        self.board[:,2] = self.shift(self.board[:,2])
        self.board[:,3] = self.shift(self.board[:,3])


    def right(self):
        """
            Shift all rows to the right.
        """
        self.board[0] = self.inverse_shift(self.board[0])
        self.board[1] = self.inverse_shift(self.board[1])
        self.board[2] = self.inverse_shift(self.board[2])
        self.board[3] = self.inverse_shift(self.board[3])


    def down(self):
        """
            Shift all columns down.
        """
        self.board[:,0] = self.inverse_shift(self.board[:,0])
        self.board[:,1] = self.inverse_shift(self.board[:,1])
        self.board[:,2] = self.inverse_shift(self.board[:,2])
        self.board[:,3] = self.inverse_shift(self.board[:,3])


    def equals(self, other):
        """
            Returns True if the boards are equal, False otherwise.
        """
        return np.array_equal(self.board, other.board)

    # TODO: Just look at the row/col and compute. No need to create a new board.
    def can_combine(self, direction, x, y):
        """
            @param direction the direction to test combining. Possible values are 'up', 'down', 'left', 'right'.
            @param x the x coordinate of the location to test. The origin is top left.
            @param y the y coordinate of the location to test. The origin is top left.
            Returns True if the value at x, y would be greater if the board was shifted in direction.
        """
        original_val = self.board[y, x]
        test_board = Board(self)

        if direction == 'down' or direction == 'd':
            test_board.down()
        elif direction == 'right' or direction == 'r':
            test_board.right()
        elif direction == 'left' or direction == 'l':
            test_board.left()
        elif direction == 'up' or direction == 'u':
            test_board.up()
        else:
            print("Error: invalid string for direction.")
            raise

        test_val = test_board.board[y, x]

        if test_val > original_val:
            return True
        else:
            return False



# TODO: create property for board
    # @property
    # def board(self):
    #     return self.board

    # def getboard(self):
    #     return self.board
    # def setboard(self, value):
    #     self.board = value
    # def delboard(self):
    #     del self.board
    # board = property(getboard, setboard, delboard, "I'm the 'board' property.")
