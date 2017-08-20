import unittest
from board import Board
from game import Game
import numpy as np


class TestBoardMethods(unittest.TestCase):

    def setUp(self):
        pass

    def test_equals(self):
        b1 = Board()
        b1.board = np.array([[0,0,0,2],
                             [0,0,0,0],
                             [0,0,0,0],
                             [0,0,0,0]])
        b2 = Board(b1)

        self.assertTrue(b1.equals(b2))
        self.assertTrue(b2.equals(b1))

        b2.next()
        self.assertFalse(b1.equals(b2))




# NOTE: Some tests currently fail because Game.down() calls Board.next()
class TestGameMethods(unittest.TestCase):

    def test_move_towards(self):
        b1 = Board()
        b1.board = np.array([[0,0,0,2],
                             [0,0,0,0],
                             [0,0,0,0],
                             [0,0,0,0]])
        g1 = Game()
        g1.board = b1
        b2 = Board()
        b2.board = np.array([[0,0,0,2],
                             [0,0,0,0],
                             [0,0,0,0],
                             [2,0,0,2]])
        g2 = Game()
        g2.board = b2
        r1 = Board()
        r1.board = np.array([[0,0,0,0],
                             [0,0,0,0],
                             [0,0,0,0],
                             [0,0,0,2]])
        r2 = Board()
        r2.board = np.array([[0,0,0,0],
                             [0,0,0,0],
                             [0,0,0,0],
                             [2,0,0,4]])

        self.assertTrue(g1.move_towards(3, 3))
        self.assertTrue(g1.board.equals(r1))

        self.assertTrue(g2.move_towards(3, 3))
        self.assertTrue(g2.board.equals(r2))


    def test_attempt_to_collapse_row(self):
        b1 = Board()
        b1.board = np.array([[0,0,0,2],
                             [0,0,0,0],
                             [0,0,0,0],
                             [0,0,0,0]])
        g1 = Game(board=b1)
        b2 = Board()
        b2.board = np.array([[0,0,0,2],
                             [0,0,0,0],
                             [0,0,0,0],
                             [2,4,4,8]])
        g2 = Game(board=b2)
        b3 = Board()
        b3.board = np.array([[0,0,0,2],
                             [0,0,0,0],
                             [0,0,0,0],
                             [2,4,8,16]])
        g3 = Game(board=b3)
        r1 = Board()
        r1.board = np.array([[0,0,0,2],
                             [0,0,0,0],
                             [0,0,0,0],
                             [0,0,0,0]])
        r2 = Board()
        r2.board = np.array([[0,0,0,2],
                             [0,0,0,0],
                             [0,0,0,0],
                             [0,2,8,8]])
        r3 = Board()
        r3.board = np.array([[0,0,0,2],
                             [0,0,0,0],
                             [0,0,0,0],
                             [2,4,8,16]])

        self.assertFalse(g1.attempt_to_collapse_row(3, 'right'))
        self.assertTrue(g1.board.equals(r1))

        self.assertTrue(g2.attempt_to_collapse_row(3, 'right'))
        self.assertTrue(g2.board.equals(r2))

        self.assertFalse(g3.attempt_to_collapse_row(3, 'right'))
        self.assertTrue(g3.board.equals(r3))


    def test_move_towards_row(self):
        b1 = Board()
        b1.board = np.array([[0,2,0,2],
                             [0,2,0,2],
                             [0,2,0,2],
                             [0,0,0,0]])
        g1 = Game()
        g1.board = b1
        b2 = Board(b1)
        g2 = Game()
        g2.board = b2
        r1 = Board()
        r1.board = np.array([[0,0,0,0],
                             [0,0,0,0],
                             [0,2,0,2],
                             [0,4,0,4]])

        self.assertTrue(g1.move_towards_row(3))
        self.assertTrue(g1.board.equals(r1))

        self.assertTrue(g2.move_towards_row(2))
        self.assertTrue(g2.board.equals(r1))



    def test_move_towards_col(self):
        b1 = Board()
        b1.board = np.array([[0,2,0,2],
                             [0,2,0,2],
                             [0,2,0,2],
                             [0,0,0,0]])
        g1 = Game(board=b1)
        b2 = Board(b1)
        g2 = Game(board=b2)
        b3 = Board(b1)
        g3 = Game(board=b3)
        b4 = Board(b1)
        g4 = Game(board=b4)
        r1 = Board()
        r1.board = np.array([[0,0,0,4],
                             [0,0,0,4],
                             [0,0,0,4],
                             [0,0,0,0]])
        r2 = Board()
        r2.board = np.array([[4,0,0,0],
                             [4,0,0,0],
                             [4,0,0,0],
                             [0,0,0,0]])

        self.assertTrue(g1.move_towards_col(3, 'right'))
        self.assertTrue(g1.board.equals(r1))
        self.assertFalse(g2.move_towards_col(2, 'right'))

        self.assertTrue(g3.move_towards_col(0, 'left'))
        self.assertTrue(g3.board.equals(r2))
        self.assertFalse(g4.move_towards_col(1, 'left'))


if __name__ == '__main__':
    unittest.main()
