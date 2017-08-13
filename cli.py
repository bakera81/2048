import numpy as np
from copy import copy
from board import Board
b = Board()
b.next()
b.next()
while True:
    b.show()
    previous_board = copy(getattr(b, 'board'))
    resp = input("Next Command: ")
    if resp == 'q' or resp == 'Q':
        break
    elif resp == 's':
        b.down()
    elif resp == 'd':
        b.right()
    elif resp == 'w':
        b.up()
    elif resp == 'a':
        b.left()
    else:
        print("Unrecognized command '{0}'. 'q' to quit.".format(resp))
    if not np.array_equal(getattr(b, 'board'), previous_board): # Don't add new numbers if no move was made
        b.next()
