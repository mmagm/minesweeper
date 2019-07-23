import unittest
from board import *
from view import *
import pdb

class TestBoard(unittest.TestCase):
    def test_board_calculation(self):
        random.seed(10)
        board = Board(rows=4, cols=4, mines=3)

        board.board = [
            '.', '.', '.', 'X',
            '.', '.', '.', 'X',
            '.', '.', '.', '.',
            'X', '.', '.', '.'
        ]

        BoardView(board).render()
        board.calculate()
        BoardView(board).render()

        self.assertEqual(board.board[0:4],   ['.', '.', 2, 'X'], "First row should equal")
        self.assertEqual(board.board[4:8],   ['.', '.', 2, 'X'], "Second row should equal")
        self.assertEqual(board.board[8:12],  [1, 1, 1, 1],       "Third row should equal")
        self.assertEqual(board.board[12:16], ['X', 1, '.', '.'], "Fourth row should equal")

if __name__ == '__main__':
    unittest.main()