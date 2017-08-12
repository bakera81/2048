import random
import numpy as np
board = np.array([[0,0,0,0],
                  [0,0,0,0],
                  [0,0,0,0],
                  [0,0,0,0]])

def print_board(board):
    # +---------------+
    # | x | x | x | x |
    # | x | x | x | x |
    # | x | x | x | x |
    # | x | x | x | x |
    # +---------------+
    output = '+---------------+\n'
    for row in board:
        output += '| {0} | {1} | {2} | {3} |\n'.format(*row)
    output += '+---------------+\n'
    print(output)


def zeros(board):
    output = []
    for y, row in enumerate(board):
        for x, col in enumerate(row):
            if col == 0:
                output.append((x, y))
    if len(output) == 0:
        print('GAME OVER')
    return output


def next(board):
    val = random.choice([2,4])
    loc = random.choice(zeros(board))
    board[loc[1], loc[0]] = val
    return board


def shift(row):
    non_zero_row = [val for val in row if val != 0] # Drop all zeros
    for i in range(len(non_zero_row) - 1): # Combine adjacent if possible
        if non_zero_row[i] == non_zero_row[i + 1]:
            non_zero_row[i] = non_zero_row[i] * 2
            non_zero_row[i + 1] = 0
    # To shift all elements, drop zeros and repad.
    non_zero_row = [val for val in non_zero_row if val != 0] # Drop all zeros
    row = non_zero_row + [0] * (4 - len(non_zero_row)) # Re-pad with zeros
    return row


def inverse_shift(row):
    non_zero_row = [val for val in row if val != 0] # Drop all zeros
    for i in reversed(range(1, len(non_zero_row))): # Combine adjacent if possible
        if non_zero_row[i] == non_zero_row[i - 1]:
            non_zero_row[i] = non_zero_row[i] * 2
            non_zero_row[i - 1] = 0
    # To shift all elements, drop zeros and repad.
    non_zero_row = [val for val in non_zero_row if val != 0] # Drop all zeros
    row = [0] * (4 - len(non_zero_row)) + non_zero_row  # Re-pad with zeros
    return row

def left(board):
    board[0] = shift(board[0])
    board[1] = shift(board[1])
    board[2] = shift(board[2])
    board[3] = shift(board[3])
    return board


def up(board):
    board[:,0] = shift(board[:,0])
    board[:,1] = shift(board[:,1])
    board[:,2] = shift(board[:,2])
    board[:,3] = shift(board[:,3])
    return board


def right(board):
    board[0] = inverse_shift(board[0])
    board[1] = inverse_shift(board[1])
    board[2] = inverse_shift(board[2])
    board[3] = inverse_shift(board[3])
    return board


def down(board):
    board[:,0] = inverse_shift(board[:,0])
    board[:,1] = inverse_shift(board[:,1])
    board[:,2] = inverse_shift(board[:,2])
    board[:,3] = inverse_shift(board[:,3])
    return board


def run():
    board = np.array([[0,0,0,0],
                      [0,0,0,0],
                      [0,0,0,0],
                      [0,0,0,0]])
    board = next(board)
    board = next(board)
    while 1:
        print_board(board)
        resp = input("Next Command: ")
        if resp == 'q' or resp == 'Q':
            break
        elif resp == 's':
            board = down(board)
        elif resp == 'd':
            board = right(board)
        elif resp == 'w':
            board = up(board)
        elif resp == 'a':
            board = left(board)
        else:
            print("Unrecognized command '{0}'. 'q' to quit.".format(resp))
        board = next(board)
