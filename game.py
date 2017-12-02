from board import Board
import numpy as np
import copy

class Game(object):

    def __init__(self, board=None):
        """
            Initializes the board with two numbers.
        """
        if board is not None:
            self.board = copy.copy(board)
        else:
            self.board = Board()
            self.board.next()
            self.board.next()

        self.previous_board = None
        self.sequence = [{'move': None, 'board': Board(self.board)}]


    def play(self):
        while True:
            self.board.show()
            self.previous_board = Board(self.board)
            resp = input("Next Command: ")
            if resp == 'q' or resp == 'Q':
                print(self.sequence)
                break
            elif resp == 's':
                self.sequence.append({'move': 'down', 'board': Board(self.board)})
                self.board.down()
            elif resp == 'd':
                self.sequence.append({'move': 'right', 'board': Board(self.board)})
                self.board.right()
            elif resp == 'w':
                self.sequence.append({'move': 'up', 'board': Board(self.board)})
                self.board.up()
            elif resp == 'a':
                self.sequence.append({'move': 'left', 'board': Board(self.board)})
                self.board.left()
            elif resp == 'seq':
                self.show_sequence()
            else:
                print("Unrecognized command '{0}'. 'q' to quit.".format(resp))
            if not self.board.equals(self.previous_board): # Don't add new numbers if no move was made
                self.board.next()


    def right(self):
        self.sequence.append({'move': 'right', 'board': Board(self.board)})

        if self.board.can_combine_in_direction('right'):
            combined = 1.0
        else:
            combined = 0.0

        self.board.right()
        self.board.next()

        return combined


    def down(self):
        self.sequence.append({'move': 'down', 'board': Board(self.board)})

        if self.board.can_combine_in_direction('down'):
            combined = 1.0
        else:
            combined = 0.0

        self.board.down()
        self.board.next()

        return combined


    def left(self):
        self.sequence.append({'move': 'left', 'board': Board(self.board)})
        if self.board.can_combine_in_direction('left'):
            combined = 1.0
        else:
            combined = 0.0

        self.board.left()
        self.board.next()

        return combined


    def up(self):
        self.sequence.append({'move': 'up', 'board': Board(self.board)})

        if self.board.can_combine_in_direction('up'):
            combined = 1.0
        else:
            combined = 0.0

        self.board.up()
        self.board.next()

        return combined


    def show_sequence(self):
        for turn in self.sequence:
            print('#######################')
            print(turn['move'])
            turn['board'].show()


    def is_over():
        pass
