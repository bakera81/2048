from .board import Board, GameOver
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
            print(self.board)
            self.previous_board = Board(self.board)
            moved = False
            resp = input("Next Command: ")
            if resp == 'q' or resp == 'Q':
                self.show_sequence()
                break
            elif resp == 's':
                self.sequence.append({'move': 'down', 'board': Board(self.board)})
                moved = self.down()
            elif resp == 'd':
                self.sequence.append({'move': 'right', 'board': Board(self.board)})
                moved = self.right()
            elif resp == 'w':
                self.sequence.append({'move': 'up', 'board': Board(self.board)})
                moved = self.up()
            elif resp == 'a':
                self.sequence.append({'move': 'left', 'board': Board(self.board)})
                moved = self.left()
            elif resp == 'seq':
                self.show_sequence()
            else:
                print("Unrecognized command '{0}'. 'q' to quit.".format(resp))

            print("moved: {}".format(moved))
            if self.is_over():
                raise GameOver
                break


    def right(self):
        self.sequence.append({'move': 'right', 'board': Board(self.board)})

        if self.board.can_move_in_direction('right'):
            self.board.right()
            self.board.next()
            combined = True
        else:
            combined = False

        return combined


    def down(self):
        self.sequence.append({'move': 'down', 'board': Board(self.board)})

        if self.board.can_move_in_direction('down'):
            self.board.down()
            self.board.next()
            combined = True
        else:
            combined = False

        return combined


    def left(self):
        self.sequence.append({'move': 'left', 'board': Board(self.board)})
        if self.board.can_move_in_direction('left'):
            self.board.left()
            self.board.next()
            combined = True
        else:
            combined = False

        return combined


    def up(self):
        self.sequence.append({'move': 'up', 'board': Board(self.board)})

        if self.board.can_move_in_direction('up'):
            self.board.up()
            self.board.next()
            combined = True
        else:
            combined = False

        return combined


    def show_sequence(self):
        for turn in self.sequence:
            print('#######################')
            print(turn['move'])
            print(turn['board'])


    def is_over(self):
        possible_move = [self.board.can_move_in_direction('up'),
                         self.board.can_move_in_direction('down'),
                         self.board.can_move_in_direction('left'),
                         self.board.can_move_in_direction('right')]

        return not any(possible_move)
