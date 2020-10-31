from functools import reduce
from math import floor
from typing import List


def manhattan(n, board: List[int]):
    null_i = board.index(0)
    board[null_i] = len(board)
    correct_board = sorted(board)
    score = 0
    for i in range(1, len(board) + 1):
        r = board.index(i)
        c = correct_board.index(i)
        score += abs(r % n - c % n) + abs(r//n - c//n)
    return score


