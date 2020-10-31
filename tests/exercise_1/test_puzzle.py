from unittest import TestCase

from exercise_1.puzzle import Puzzle


class TestPuzzle(TestCase):


    def test_first_node_is_start(self):
        puzzle = Puzzle(3, [1, 2, 3, 0, 4, 5, 7, 8, 6])
