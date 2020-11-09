from unittest import TestCase

from exercise_3.exercise_3 import Exercise3

test_input = """
5
0 5 1 0 0
0 0 1 4 0
0 2 0 0 6
0 0 1 0 1
0 0 0 0 0
""".lstrip().rstrip()

expected_output = """
Max Flow: 4
Cut: 0 1 3
Steps: 5
0 3 1 0 0
0 0 1 2 0
0 0 0 0 3
0 0 1 0 1
0 0 0 0 0
""".lstrip().rstrip()


class TestExercise3(TestCase):

    def test_solution(self):
        self.assertEqual(expected_output, Exercise3(test_input).solution())

