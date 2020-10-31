import numpy as np


class Board:
    """Understands a specific instance in a puzzle"""

    def __init__(self, n, config):
        self._board = self._init_board(n, config)

    def _init_board(self, n, config):
        data = np.array(config)
        return data.reshape((n, n)).tolist()

    def __str__(self):
        return "".join(str(row) + "\n" for row in self._board)


class Puzzle:
    """Understands a number grid puzzle"""

    def __init__(self, n, board_nodes):
        self._boards = self._init_board(n, board_nodes)

    def _init_board(self, n, board_nodes):
        for i in range(0, n):
            for j in range(0, n):
                pass
