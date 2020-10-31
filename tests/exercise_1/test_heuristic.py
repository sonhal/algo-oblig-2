from unittest import TestCase

from exercise_1.heuristic import manhattan


class TestManhattan(TestCase):

    def test_perfect_board(self):
        board = [1, 2, 3,
                 4, 5, 6,
                 7, 8, 0]
        self.assertEqual(0, manhattan(3, board))

    def test_back_vert_move_board(self):
        board = [1, 3, 2,
                 4, 5, 6,
                 7, 8, 0]
        self.assertEqual(2, manhattan(3, board))

    def test_vert_move_board(self):
        board = [1, 2, 3,
                 4, 5, 6,
                 7, 0, 8]
        self.assertEqual(2, manhattan(3, board))

    def test_hor_move_board(self):
        board = [1, 2, 3,
                 4, 5, 0,
                 7, 8, 6]
        self.assertEqual(2, manhattan(3, board))

    def test_multi_vert_move_board(self):
        board = [2, 3, 1,
                 4, 5, 6,
                 7, 8, 0]
        self.assertEqual(4, manhattan(3, board))

    def test_multi_hor_move_board(self):
        board = [1, 2, 0,
                 4, 5, 6,
                 7, 8, 3]
        self.assertEqual(4, manhattan(3, board))

    def test_multi_hor_vert_move_board(self):
        board = [1, 0, 2,
                 4, 5, 6,
                 7, 8, 3]
        self.assertEqual(6, manhattan(3, board))

    def test_reversed_board(self):
        board = [0, 8, 7,
                 6, 5, 4,
                 3, 2, 1]
        self.assertEqual(24, manhattan(3, board))
