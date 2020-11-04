from copy import copy
from enum import Enum
from typing import List, Tuple, Dict

BLANK_TILE_SYMBOL = 0


class Board:
    """Understands a specific instance in a puzzle"""

    class Move(Enum):
        LEFT = 1
        RIGHT = 2
        UP = 3
        DOWN = 4

        def __str__(self):
            return str(self.name[0:1])

    def __init__(self, n, tiles: List[int]):
        validate_board(n, tiles)
        self._n = n
        self._tiles = tiles
        self._blank_index = tiles.index(BLANK_TILE_SYMBOL)
        self._neighbors: Dict = None
        self._parent = None

    @property
    def neighbors(self) -> List[Tuple["Move", "Board"]]:
        if self._neighbors is None:
            self._gen_neighbors()
        return [(k, v) for k, v in self._neighbors.items() if v is not None]

    def _gen_neighbors(self):
        self._neighbors = {
            Board.Move.LEFT: self.move_left(),
            Board.Move.RIGHT: self.move_right(),
            Board.Move.UP: self.move_up(),
            Board.Move.DOWN: self.move_down(),
        }

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, parent):
        self._parent = parent

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

    def heuristic(self, h):
        return h(self._n, self._tiles)

    def __hash__(self) -> int:
        board_hash =  hash(self._n) + 31
        for tile in self._tiles:
            board_hash = board_hash * hash(tile) + 31
        return board_hash

    def __eq__(self, o: object) -> bool:
        if self is o:
            return True
        if isinstance(o, self.__class__) and self._n == o._n and compare_list_ordered(self._tiles, o._tiles):
            return True
        return False

    def __len__(self):
        return len(self._tiles)

    # def __str__(self):
    #     return "".join(str(row) + "\n" for row in self._tiles)

    def __repr__(self):
        return f"Board(n={self._n}, tiles={self._tiles})"


def switch(board, a, b):
    board = copy(board)
    tmp = board[a]
    board[a] = board[b]
    board[b] = tmp
    return board


def compare_list_ordered(a, b):
    if len(a) != len(b):
        return False
    return len(a) == len([i for i, j in zip(a, b) if i == j])


def validate_board(n, tiles):
    if sum(range(n * n)) != sum(tiles) or n != (len(tiles) // n):
        raise ValueError(f"invalid board n={n}, tiles={tiles}")
