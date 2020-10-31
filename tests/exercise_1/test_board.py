from unittest import TestCase

from exercise_1.puzzle import Board


class TestBoard(TestCase):

    def test_create_neighbor(self):
        board = Board(3, [1, 2, 3, 0, 4, 5, 7, 8, 6])
        neighbor = Board(3, [1, 2, 3, 4, 0, 5, 7, 8, 6])
        board.left = neighbor
        self.assertEqual(board, neighbor.right)
