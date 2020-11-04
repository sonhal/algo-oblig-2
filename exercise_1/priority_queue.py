import itertools
from collections import Set
from dataclasses import dataclass, field
from heapq import heappush, heappop
from typing import Any, Dict


@dataclass(order=True)
class Prioritized:
    priority: int
    seq_nr: int
    element: Any = field(compare=False)


class PriorityQueue:
    """
    Understands Prioritising elements
    Also keeps a hash map for fast lookup
    inspired from: https://docs.python.org/3/library/heapq.html
    """
    REMOVED = '<removed-task>'  # placeholder for a removed task

    def __init__(self):
        self._pq = []  # list of entries arranged in a heap
        self._node_finder: Dict[Prioritized] = {}  # mapping of tasks to entries
        self._counter = itertools.count()  # unique sequence count

    def enqueue(self, priority, element):
        if element in self._node_finder:
            self._remove_element(element)
        count = next(self._counter)
        node = Prioritized(priority, count, element)
        self._node_finder[element] = node
        heappush(self._pq, node)

    def _remove_element(self, element):
        node = self._node_finder.pop(element)
        node.element = self.REMOVED

    def dequeue(self):
        while self._pq:
            node = heappop(self._pq)
            if node.element is not self.REMOVED:
                del self._node_finder[node.element]
                return node.element
        raise KeyError(f"pop from empty {self.__class__}")

    def priority(self, element):
        return self._node_finder[element].priority

    def __len__(self):
        return len(self._pq)

    def __contains__(self, element):
        return element in self._node_finder







