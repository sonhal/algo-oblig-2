from dataclasses import dataclass, field
from typing import Callable, List, Any

from exercise_1.board import Board
from exercise_1.priority_queue import PriorityQueue


@dataclass(eq=True, frozen=True)
class Node:
    element: Board
    parent: Any = field(compare=False)
    move: Board.Move = field(compare=False)

    @property
    def neighbors(self):
        return [Node(element, self, move) for move, element in self.element.neighbors]

    def heuristic(self, h):
        return self.element.heuristic(h)


class AStar:

    def __init__(self, cost_function: Callable, heuristic_function: Callable, root, goal):
        self._cost = cost_function
        self._h = heuristic_function
        self._queue = PriorityQueue()
        self._cost_cache = {}
        self._done: List[Node] = []
        self._root = root
        self._goal = goal
        self._computed = False

    def moves(self) -> List:
        if self._computed is False:
            self._compute()
        moves = []
        curr = self._done[-1]
        while curr.element != self._root:
            moves.append(curr.move)
            curr = curr.parent
        return list(reversed(moves))

    def unique_states_seen(self):
        if self._computed is False:
            self._compute()
        return max(self._queue.unique_seen() - 1, 0)  # edge case when r == g

    def _compute(self):
        root_node = Node(self._root, None, None)
        self._queue.enqueue(0, root_node)
        self._cost_cache[root_node] = 0
        while len(self._queue) > 0:
            # deqeue cheapest node(v) where value = f(v)
            v: Node = self._queue.dequeue()
            self._done.append(v)
            if v.element == self._goal:
                self._computed = True
                return
            for w in v.neighbors:
                if w not in self._queue:
                    cost = self._f(v, w)
                    self._queue.enqueue(cost, w)
                    self._cost_cache[w] = cost

                elif self._cost_cache[w] >= self._f(v, w):
                    cost = self._f(v, w)
                    self._queue.enqueue(cost, w)
                    self._cost_cache[w] = cost

        raise ValueError(f"No path to goal={self._goal}")

    def _f(self, parent, node):
        return self._g(parent, node) + node.heuristic(self._h)

    def _g(self, parent, node):
        return self._cost_cache[parent] + self._cost(parent, node)




