from unittest import TestCase

from exercise_1.exercise_1 import Exercise1

test_input = """
3
1 2 3
0 4 5
7 8 6
"""

test_output = """
1 2 3
0 4 5
7 8 6
Solution: 3, RRD
States seen: 7
"""

class TestE2E(TestCase):


    def test_oblig_example(self):
        ex1 = Exercise1(test_input)
        self.assertEqual(test_output, ex1.solution())