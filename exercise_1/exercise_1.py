from typing import List

from exercise_1.a_star_search import AStar
from exercise_1.board import Board
from exercise_1.heuristic import manhattan


class Exercise1:

    GOAL = Board(3, [1, 2, 3,
                     4, 5, 6,
                     7, 8, 0])

    def __init__(self, input_text):

        self._n = self._parse_n(input_text)
        self._root = self._parse_root(input_text)

    def solution(self):
        astar = AStar(lambda x, y: 1, manhattan, Board(self._n, self._root), self.GOAL)
        moves_str = "".join(str(move) for move  in astar.moves())
        return " ".join(str(tile) for tile in self._root) + "\n" + \
               f"Solution: {len(astar.moves())}," + moves_str + "\n" + \
               f"States seen: {astar.unique_states_seen()}"

    def _parse_n(self, input_text):
        return int(input_text.split()[0])

    def _parse_root(self, input_text) -> List:
        return [int(tile) for tile in input_text.split()[1:]]

