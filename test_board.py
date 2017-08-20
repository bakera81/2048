import unittest
from board import Board
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


    def test_move_towards(self):
        b1 = Board()
        b1.board = np.array([[0,0,0,2],
                             [0,0,0,0],
                             [0,0,0,0],
                             [0,0,0,0]])
        b2 = Board()
        b2.board = np.array([[0,0,0,2],
                             [0,0,0,0],
                             [0,0,0,0],
                             [2,0,0,2]])
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

        self.assertTrue(b1.move_towards(3, 3))
        self.assertTrue(b1.equals(r1))

        self.assertTrue(b2.move_towards(3, 3))
        self.assertTrue(b2.equals(r2))


    def test_attempt_to_collapse_row(self):
        b1 = Board()
        b1.board = np.array([[0,0,0,2],
                             [0,0,0,0],
                             [0,0,0,0],
                             [0,0,0,0]])
        b2 = Board()
        b2.board = np.array([[0,0,0,2],
                             [0,0,0,0],
                             [0,0,0,0],
                             [2,4,4,8]])
        b3 = Board()
        b3.board = np.array([[0,0,0,2],
                             [0,0,0,0],
                             [0,0,0,0],
                             [2,4,8,16]])
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

        self.assertFalse(b1.attempt_to_collapse_row(3, 'right'))
        self.assertTrue(b1.equals(r1))

        self.assertTrue(b2.attempt_to_collapse_row(3, 'right'))
        self.assertTrue(b2.equals(r2))

        self.assertFalse(b3.attempt_to_collapse_row(3, 'right'))
        self.assertTrue(b3.equals(r3))


    def test_move_towards_row(self):
        b1 = Board()
        b1.board = np.array([[0,2,0,2],
                             [0,2,0,2],
                             [0,2,0,2],
                             [0,0,0,0]])
        b2 = Board(b1)
        r1 = Board()
        r1.board = np.array([[0,0,0,0],
                             [0,0,0,0],
                             [0,2,0,2],
                             [0,4,0,4]])

        self.assertTrue(b1.move_towards_row(3))
        self.assertTrue(b1.equals(r1))

        self.assertTrue(b2.move_towards_row(2))
        self.assertTrue(b2.equals(r1))



    def test_move_towards_col(self):
        b1 = Board()
        b1.board = np.array([[0,2,0,2],
                             [0,2,0,2],
                             [0,2,0,2],
                             [0,0,0,0]])
        b2 = Board(b1)
        b3 = Board(b1)
        b4 = Board(b1)
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

        self.assertTrue(b1.move_towards_col(3, 'right'))
        self.assertTrue(b1.equals(r1))
        self.assertFalse(b2.move_towards_col(2, 'right'))

        self.assertTrue(b3.move_towards_col(0, 'left'))
        self.assertTrue(b3.equals(r2))
        self.assertFalse(b4.move_towards_col(1, 'left'))



if __name__ == '__main__':
    unittest.main()
