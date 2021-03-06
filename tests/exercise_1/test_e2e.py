from unittest import TestCase

from exercise_1.exercise_1 import Exercise1

test_input = """
3
1 2 3
0 4 5
7 8 6
"""

test_output = """1 2 3
0 4 5
7 8 6
Solution: 3, RRD
States seen: 24
"""

test_input_8p = """
4
1 2 0 4
5 6 3 7
9 10 11 8
13 14 15 12
"""

test_output_8p = """1 2 0 4
5 6 3 7
9 10 11 8
13 14 15 12
Solution: 4, DRDD
States seen: 129
"""


class TestE2E(TestCase):

    def test_oblig_example(self):
        ex1 = Exercise1(test_input)
        self.assertEqual(test_output, ex1.solution())

    def test_oblig_example_8_puzzle(self):
        ex1 = Exercise1(test_input_8p)
        self.assertEqual(test_output_8p, ex1.solution())