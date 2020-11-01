from copy import copy
from enum import Enum
from typing import List, Tuple

BLANK_TILE_SYMBOL = 0


class Board:
    """Understands a specific instance in a puzzle"""

    class Move(Enum):
        LEFT = 1
        RIGHT = 2
        UP = 3
        DOWN = 4

    def __init__(self, n, tiles: List[int]):
        self._n = n
        self._tiles = tiles
        self._blank_index = tiles.index(BLANK_TILE_SYMBOL)
        self._neighbors = None

    @property
    def neighbors(self):
        if self._neighbors is None:
            self._gen_neighbors()
        return self._neighbors

    def _gen_neighbors(self):
        self._neighbors = {
            Board.Move.LEFT: self.move_left(),
            Board.Move.RIGHT: self.move_right(),
            Board.Move.UP: self.move_up(),
            Board.Move.DOWN: self.move_down(),
        }

    def move_left(self):
        if self._blank_x() == 0:
            return None
        return Board(self._n, switch(self._tiles, self._blank_index, self._blank_index - 1))

    def move_right(self):
        if self._blank_x() == self._n - 1:
            return None
        return Board(self._n, switch(self._tiles, self._blank_index, self._blank_index + 1))

    def move_up(self):
        if self._blank_y() == 0:
            return None
        return Board(self._n, switch(self._tiles, self._blank_index, self._blank_index - 3))

    def move_down(self):
        if self._blank_y() == self._n - 1:
            return None
        return Board(self._n, switch(self._tiles, self._blank_index, self._blank_index + 3))

    def _blank_x(self):
        return self._blank_index % self._n

    def _blank_y(self):
        return self._blank_index // self._n

    def __hash__(self) -> int:
        return hash(self._n) + 31 * hash(self._tiles)

    def __eq__(self, o: object) -> bool:
        if self is o:
            return True
        if isinstance(o, self.__class__) and self._n == o._n and self._tiles == o._tiles:
            return True
        return False

    def __str__(self):
        return "".join(str(row) + "\n" for row in self._tiles)

    def __repr__(self):
        return f"Board(n={self._n}, tiles={self._tiles})"


def switch(board, a, b):
    board = copy(board)
    tmp = board[a]
    board[a] = board[b]
    board[b] = tmp
    return board
