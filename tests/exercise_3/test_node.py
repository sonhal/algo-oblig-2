from unittest import TestCase

from exercise_3.Graph import Node


class TestNode(TestCase):

    def test_is_source(self):
        self.assertTrue(Node(0, [0, 1, 2, 0]).is_source())  # source config

    def test_is_sink(self):
        self.assertTrue(Node(3, [0, 1, 2, 0]).is_sink())  # source config

    def test_update_flow(self):
        n = Node(1, [0, 0, 0, 2])
        s = Node(3, [0, 0, 0, 0])
        n.set_flow(s, 2)
        self.assertEqual(2, n.flow(s))
        self.assertRaises(ValueError, lambda: n.set_flow(s, 3))

    def test_residual(self):
        n = Node(1, [0, 0, 0, 2])
        s = Node(3, [0, 0, 0, 0])
        n.set_flow(s, 1)
        self.assertEqual(1, n.residual(s))
        n.set_flow(s, 2)
        self.assertEqual(0, n.residual(s))
