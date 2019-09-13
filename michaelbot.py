
import random

class BotPlayer:

    """ Your custom player code goes here, but should implement
    	all of these functions. You are welcome to implement
    	additional helper functions. You may wish to look at board.py
    	to see what functions are available to you.
    """


    def __init__(self, gui, color="black"):
        self.color = color
        self.gui = gui

    def get_current_board(self, board):
        self.current_board = board

    def get_move(self):
        score = [[100, -20, 10,  5,  5, 10, -20, 100],\
                 [-20, -50, -2, -2, -2, -2, -50, -20],\
                 [ 10,  -2, -1, -1, -1, -1,  -2,  10],\
                 [  5,  -2, -1, -1, -1, -1,  -2,   5],\
                 [  5,  -2, -1, -1, -1, -1,  -2,   5],\
                 [ 10,  -2, -1, -1, -1, -1,  -2,  10],\
                 [-20, -50, -2, -2, -2, -2, -50, -20],\
                 [100, -20, 10,  5,  5, 10, -20, 100]]
        moves = self.current_board.get_valid_moves(self.color)
        values = [score[move[0]][move[1]] for move in moves]
        self.current_board.apply_move(moves[values.index(max(values))], self.color)
        return 0, self.current_board
