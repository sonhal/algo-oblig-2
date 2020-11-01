from unittest import TestCase

from exercise_1.board import Board


class TestBoard(TestCase):

    def test_move_right(self):
        board = Board(3, [1, 2, 3, 0, 4, 5, 7, 8, 6])
        self.assertEqual(Board(3, [1, 2, 3,
                                   4, 0, 5,
                                   7, 8, 6]), board.move_right())

        board = Board(3, [1, 2, 0, 3, 4, 5, 7, 8, 6])
        self.assertEqual(None, board.move_right())

    def test_move_left(self):
        board = Board(3, [1, 2, 0, 3, 4, 5, 7, 8, 6])
        self.assertEqual(Board(3, [1, 0, 2,
                                   3, 4, 5,
                                   7, 8, 6]), board.move_left())

        board = Board(3, [0, 2, 1, 3, 4, 5, 7, 8, 6])
        self.assertEqual(None, board.move_left())

    def test_move_up(self):
        board = Board(3, [1, 2, 3, 0, 4, 5, 7, 8, 6])
        self.assertEqual(Board(3, [0, 2, 3,
                                   1, 4, 5,
                                   7, 8, 6]), board.move_up())
        board = Board(3, [0, 2, 3, 1, 4, 5, 7, 8, 6])
        self.assertEqual(None, board.move_up())

    def test_move_down(self):
        board = Board(3, [1, 2, 3, 0, 4, 5, 7, 8, 6])
        self.assertEqual(Board(3, [1, 2, 3,
                                   7, 4, 5,
                                   0, 8, 6]), board.move_down())

        board = Board(3, [1, 2, 3, 7, 4, 5, 0, 8, 6])
        self.assertEqual(None, board.move_down())

    def test_neighbors(self):
        board = Board(3, [1, 2, 3,
                          0, 4, 5,
                          7, 8, 6])
        self.assertEqual(Board(3, [0, 2, 3, 1, 4, 5, 7, 8, 6]), board.neighbors[Board.Move.UP])
        self.assertEqual(None, board.neighbors[Board.Move.LEFT])