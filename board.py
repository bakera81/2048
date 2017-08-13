import random
import numpy as np
import copy

class Board(object):

    # TODO: Implement deep copy (new object)
    def __init__(self, board=None):
        if board is None:
            self.board = np.array([[0,0,0,0],
                                   [0,0,0,0],
                                   [0,0,0,0],
                                   [0,0,0,0]])
        else:
            self.board = copy.copy(board.board)


    def zeros(self):
        output = []
        for y, row in enumerate(self.board):
            for x, col in enumerate(row):
                if col == 0:
                    output.append((x, y))
        if len(output) == 0:
            print('GAME OVER')
        return output


    def next(self):
        val = random.choice([2,4])
        loc = random.choice(self.zeros())
        self.board[loc[1], loc[0]] = val

# TODO: handle mutlidigit numbers better
# TODO: use curses (for better terminal printing)
    def show(self):
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
        self.board[0] = self.shift(self.board[0])
        self.board[1] = self.shift(self.board[1])
        self.board[2] = self.shift(self.board[2])
        self.board[3] = self.shift(self.board[3])


    def up(self):
        self.board[:,0] = self.shift(self.board[:,0])
        self.board[:,1] = self.shift(self.board[:,1])
        self.board[:,2] = self.shift(self.board[:,2])
        self.board[:,3] = self.shift(self.board[:,3])


    def right(self):
        self.board[0] = self.inverse_shift(self.board[0])
        self.board[1] = self.inverse_shift(self.board[1])
        self.board[2] = self.inverse_shift(self.board[2])
        self.board[3] = self.inverse_shift(self.board[3])


    def down(self):
        self.board[:,0] = self.inverse_shift(self.board[:,0])
        self.board[:,1] = self.inverse_shift(self.board[:,1])
        self.board[:,2] = self.inverse_shift(self.board[:,2])
        self.board[:,3] = self.inverse_shift(self.board[:,3])


    def equals(self, other):
        return np.array_equal(self.board, other.board)

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
