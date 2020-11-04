from unittest import TestCase

from exercise_1.a_star_search import AStar
from exercise_1.board import Board
from exercise_1.heuristic import manhattan


class TestAStar(TestCase):

    def test_init(self):
        self.assertIsNotNone(AStar(lambda x: 1, Board(3, [1,2,3,4,5,6,7,8,0]), manhattan, Board(3, [1,2,3,4,5,6,7,8,0])))

    def test_shortest_with_no_move_needed(self):
        astar = AStar(lambda x, y: 1, manhattan, Board(3, [1, 2, 3, 4, 5, 6, 7, 8, 0]), Board(3, [1, 2, 3, 4, 5, 6, 7, 8, 0]))
        self.assertEqual([], astar.moves())

    def test_shortest_with_one_move_needed(self):
        astar = AStar(lambda x, y: 1, manhattan, Board(3, [1, 2, 3, 4, 5, 6, 7, 8, 0]), Board(3, [1, 2, 3, 4, 5, 6, 7, 0, 8]))
        self.assertEqual([Board.Move.LEFT],
                         astar.moves())

    def test_shortest_max_moves_needed(self):
        astar = AStar(lambda x, y: 1, manhattan, Board(3, [1, 2, 3,
                                                           4, 5, 6,
                                                           7, 8, 0]),
                      Board(3, [1, 2, 3,
                                4, 0, 8,
                                7, 6, 5]))
        self.assertEqual([Board.Move.LEFT, Board.Move.UP, Board.Move.RIGHT, Board.Move.DOWN, Board.Move.LEFT, Board.Move.UP], astar.moves())

    def test_shortest_moves(self):
        astar = AStar(lambda x, y: 1, manhattan, Board(3, [1, 2, 3,
                                                           4, 5, 6,
                                                           7, 8, 0]), Board(3, [1, 2, 0,
                                                                                4, 5, 3,
                                                                                7, 8, 6]))
        self.assertEqual([Board.Move.UP, Board.Move.UP], astar.moves())
