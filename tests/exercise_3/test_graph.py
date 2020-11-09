from unittest import TestCase

from exercise_3.Graph import Graph


class TestGraph(TestCase):

    def test_init(self):
        Graph([
            [0, 5, 2, 0],
            [0, 0, 0, 3],
            [0, 0, 0, 5],
            [0, 0, 0, 0]])

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

    def test_steps(self):
        g = Graph([
            [0, 10, 5, 0],
            [0, 0, 0, 10],
            [0, 0, 0, 5],
            [0, 0, 0, 0]])
        self.assertEqual(3, g.steps())

    def test_flow_graph(self):
        g = Graph([
            [0, 10, 5, 0],
            [0, 0, 0, 10],
            [0, 0, 0, 5],
            [0, 0, 0, 0]])
        self.assertEqual([
            [0, 10, 5, 0],
            [0, 0, 0, 10],
            [0, 0, 0, 5],
            [0, 0, 0, 0]], g.flow_graph())

    def test_maxed_cut(self):
        g = Graph([
            [0, 10, 5, 0],
            [0, 0, 0, 10],
            [0, 0, 0, 5],
            [0, 0, 0, 0]])
        self.assertEqual([0, 1, 2], g.min_cut())

        g = Graph([
            [0, 10, 5, 2, 0],
            [0, 0, 0, 0, 10],
            [0, 0, 0, 0, 5],
            [0, 0, 0, 0, 10],
            [0, 0, 0, 0, 0]])
        self.assertEqual([0, 1, 2], g.min_cut())


