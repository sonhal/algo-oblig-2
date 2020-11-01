


class Puzzle:
    """Understands a number grid puzzle"""

    def __init__(self, n, board_nodes):
        self._boards = self._init_board(n, board_nodes)

    def _init_board(self, n, board_nodes):
        for i in range(0, n):
            for j in range(0, n):
                pass
