from unittest import TestCase

from exercise_3.Graph import Graph


class TestGraph(TestCase):

    def test_init(self):
        Graph([
            [0, 5, 2, 0],
            [0, 0, 0, 3],
            [0, 0, 0, 5]])

    def test_number_of_nodes(self):
        g = Graph([
            [0, 5, 2, 0],
            [0, 0, 0, 3],
            [0, 0, 0, 5],
            [0, 0, 0, 0]])
        self.assertEqual(4, len(g))

    def test_max_flow(self):
        g = Graph([
            [0, 10, 5, 0],
            [0, 0, 0, 10],
            [0, 0, 0, 5],
            [0, 0, 0, 0]])
        self.assertEqual(15, g.max_flow())
