from typing import List

from exercise_1.a_star_search import AStar
from exercise_1.board import Board
from exercise_1.heuristic import manhattan


class Exercise1:

    def __init__(self, input_text):
        self._n = self._parse_n(input_text)
        self._root = self._parse_root(input_text)

    def solution(self):
        astar = AStar(lambda x, y: 1, lambda x, y: 1, Board(self._n, self._root), Board.goal(self._n))
        moves_str = "".join(str(move) for move in astar.moves())
        return rapport_tiles(self._n, self._root) + \
               f"Solution: {len(astar.moves())}, " + moves_str + "\n" + \
               f"States seen: {astar.unique_states_seen()}"

    def _parse_n(self, input_text):
        return int(input_text.split()[0])

    def _parse_root(self, input_text) -> List:
        return [int(tile) for tile in input_text.split()[1:]]


def rapport_tiles(n, tiles) -> str:
    tiles_str = ""
    for i in range(n):
        tiles_str += "".join(str(tile) + " " for tile in tiles[:n]) + "\n"
        tiles = tiles[n:]
    return tiles_str
