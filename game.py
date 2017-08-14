from board import Board

class Game(object):

    def __init__(self):
        """
            Initializes the board with two numbers.
        """
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
        elif self.board.can_combine('l', x, y):
            self.board.right()
            return True
        elif self.board.can_combine('u', x, y):
            self.board.right()
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



    def show_sequence(self):
        for turn in self.sequence:
            print('#######################')
            print(turn['move'])
            turn['board'].show()
