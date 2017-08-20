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


    def increment_position(self, x, y):
        # +---------------+
        # | > | > | > | * |
        # | ^ | < | < | < |
        # | > | > | > | ^ |
        # | ^ | < | < | < |
        # +---------------+
        if y == 3 or y == 1:
            if x == 0:
                return tuple([x, y-1])
            else:
                return tuple([x-1, y])
        elif y == 2:
            if x == 3:
                return tuple([x, y-1])
            else:
                return tuple([x+1, y])
        elif y == 0:
            if x == 3:
                return tuple([None, None])
            else:
                return tuple([x+1, y])
        else:
            print("Error: y is out of bounds.")
            raise

# Note: change direction depending on row!
    def solve_at_position(self, x, y):
        if self.board.can_combine('d', x, y):
            self.board.down()
            return self.solve_at_position(x, y)
        elif self.board.can_combine('r', x, y):
            self.board.right()
            return self.solve_at_position(x, y)
        elif self.board.can_combine('l', x, y):
            self.board.right()
            return self.solve_at_position(x, y)
        elif self.board.can_combine('u', x, y):
            self.board.right()
            return self.solve_at_position(x, y)
        else:
            return self.solve_at_position(self.increment_position(x, y))


    def solve_at_position_2(self, x, y):
        if self.board.can_combine('d', x, y):
            self.board.down()
            return True
        elif self.board.can_combine('r', x, y):
            self.board.right()
            return True
        elif self.board.can_add_to_row(y):
            self.board.down()
            return True
        elif self.board.can_combine('l', x, y):
            self.board.left()
            return True
        elif self.board.can_combine('u', x, y):
            self.board.up()
            return True
        else:
            return False



    # NOTE: The board below will be shifted to the left
    # +---------------+
    # | 0 | 0 | 0 | 0 |
    # | 0 | 0 | 0 | 4 |
    # | 0 | 0 | 0 | 4 |
    # | 0 | 0 | 0 | 2 |
    # +---------------+
    def solve(self):
        x = 3 # start solving at the bottom right
        y = 3
        while True:
            print(str(x) + ', ' + str(y))
            self.board.show()
            action_taken = self.solve_at_position_2(x, y)
            if action_taken == False:
                x, y = self.increment_position(x, y)
            else:
                x, y = (3, 3)
                self.board.next() #It seems like new numbers are being added at the wrong time.
            if x == None or y == None:
                print('Ending.')
                break

# TODO:
# left
# +---------------+
# | 0 | 0 | 0 | 0 |
# | 0 | 0 | 0 | 0 |
# | 0 | 2 | 0 | 4 |
# | 2 | 4 | 2 | 16 |
# +---------------+

# left
# +---------------+
# | 0 | 0 | 2 | 4 |
# | 0 | 4 | 2 | 8 |
# | 4 | 8 | 2 | 4 |
# | 8 | 16 | 4 | 64 |
# +---------------+

    def solve_2(self):
        x, y = (3, 3)
        direction = 'right'
        for _ in range(100):
            if self.move_towards(x, y):
                pass
            elif self.attempt_to_collapse_row(y, direction):
                pass
            elif self.attempt_to_collapse_col(x):
                pass
            elif self.move_towards_row(y):
                pass
            elif self.move_towards_col(x, direction):
                pass
            else:
                if direction == 'right':
                    self.left()
                    self.right()
                else:
                    self.right()
                    self.left()

            # When to increment x, y?


    def right(self):
        self.sequence.append({'move': 'right', 'board': Board(self.board)})
        self.board.right()
        self.board.next()


    def down(self):
        self.sequence.append({'move': 'down', 'board': Board(self.board)})
        self.board.down()
        self.board.next()


    def left(self):
        self.sequence.append({'move': 'left', 'board': Board(self.board)})
        self.board.left()
        self.board.next()


    def up(self):
        self.sequence.append({'move': 'up', 'board': Board(self.board)})
        self.board.up()
        self.board.next()


    def move_towards(self, x, y):
        if self.board.can_combine(x, y, 'down'):
            self.down()
            return True
        elif self.board.can_combine(x, y, 'right'):
            self.right()
            return True
        elif self.board.can_combine(x, y, 'left'):
            self.left()
            return True
        elif self.board.can_combine(x, y, 'up'):
            self.up()
            return True
        else:
            return False


    def attempt_to_collapse_row(self, y, direction):
        test_board = Board(self.board)
        if direction == 'right':
            test_board.right()
        elif direction == 'left':
            test_board.left()
        else:
            print('Error: invalid direction')

        if np.array_equal(self.board.board[y], test_board.board[y]):
            return False
        else:
            if direction == 'right':
                self.right()
            elif direction == 'left':
                self.left()
            else:
                print('Error: invalid direction')
            return True


    def attempt_to_collapse_col(self, x):
        test_board = Board(self.board)
        test_board.down()

        if np.array_equal(self.board.board[:, x], test_board.board[:, x]):
            return False
        else:
            self.down()
            return True


    def move_towards_row(self, y):
        test_board = Board(self.board)
        test_board.down()

        # There is a case where the board has changed but the row is the same
        if not np.array_equal(self.board.board[y], test_board.board[y]):
            self.down()
            return True
        else:
            return False


    def move_towards_col(self, x, direction):
        test_board = Board(self.board)
        if direction == 'right':
            test_board.right()
            if not np.array_equal(self.board.board[:, x], test_board.board[:, x]):
                self.right()
                return True
            else:
                return False
        elif direction == 'left':
            test_board.left()
            if not np.array_equal(self.board.board[:, x], test_board.board[:, x]):
                self.left()
                return True
            else:
                return False
        else:
            print('Invalid direction.')


    def show_sequence(self):
        for turn in self.sequence:
            print('#######################')
            print(turn['move'])
            turn['board'].show()
