
import random
from copy import deepcopy
from config import WHITE, BLACK, EMPTY

class BotPlayer:

    """ Your custom player code goes here, but should implement
    	all of these functions. You are welcome to implement
    	additional helper functions. You may wish to look at board.py
    	to see what functions are available to you.
    """

    def __init__(self, gui, color=BLACK):
        self.color = color
        self.gui = gui
        self.weighted_board = [[10, 4, 5, 5, 5, 5, 4, 10],
                      [4, 0, 0, 0, 0, 0, 0, 4],
                      [5, 0, 3, 3, 3, 3, 0, 5],
                      [5, 0, 3, 0, 0, 3, 0, 5],
                      [5, 0, 3, 0, 0, 3, 0, 5],
                      [5, 0, 3, 3, 3, 3, 0, 5],
                      [4, 0, 0, 0, 0, 0, 0, 4],
                      [10, 4, 5, 5, 5, 5, 4, 10]]

    def get_current_board(self, board):
        self.current_board = board

    def get_move(self):
        moves = self.current_board.get_valid_moves(self.color)
        optimal = -1
        best_move = moves[0]
        stone_index = 1
        if (self.color == 2):
            stone_index = 0
        for i, j in moves:
            potential_board = deepcopy(self.current_board)
            potential_board.apply_move((i, j), self.color)
            checker = self.weighted_board[i][j] + potential_board.count_stones()[stone_index]
            if checker > optimal:
                optimal = checker
                best_move = i, j
        self.current_board.apply_move(best_move, self.color)
        return 0, self.current_board
