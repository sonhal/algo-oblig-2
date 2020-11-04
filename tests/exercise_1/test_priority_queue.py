from dataclasses import dataclass
from typing import Any
from unittest import TestCase

from exercise_1.priority_queue import PriorityQueue

@dataclass
class Node:
    priority: int
    element: Any


class TestPriorityQueue(TestCase):

    def test_init(self):
        pq = PriorityQueue()

    def test_enqueue(self):
        pq = PriorityQueue()
        pq.enqueue(10, "task 1")
        pq.enqueue(1, "task 2")
        pq.enqueue(1, "task 2")
        pq.enqueue(1, "task 2")
        pq.enqueue(1, "task 2")
        pq.enqueue(1, "task 2")
        self.assertEqual("task 2", pq.dequeue())

    def test_dequeue(self):
        pq = PriorityQueue()
        pq.enqueue(10, "task 1")
        pq.enqueue(1, "task 2")
        pq.dequeue()
        self.assertEqual("task 1", pq._pq[0].element)

    def test_contains(self):
        pq = PriorityQueue()
        pq.enqueue(10, "task 1")
        pq.enqueue(1, "task 2")
        pq.dequeue()
        self.assertFalse("task 2" in pq)
        self.assertTrue("task 1" in pq)
