from board import Board

class Game(object):

    def __init__(self):
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
                print(self.sequence)
            else:
                print("Unrecognized command '{0}'. 'q' to quit.".format(resp))
            if not self.board.equals(self.previous_board): # Don't add new numbers if no move was made
                self.board.next()

    def show_sequence(self):
        for turn in self.sequence:
            print('#######################')
            print(turn['move'])
            turn['board'].show()
