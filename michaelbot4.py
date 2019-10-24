
import random
import math
from config import WHITE, BLACK, EMPTY
class BotPlayer:

    """ Your custom player code goes here, but should implement
    	all of these functions. You are welcome to implement
    	additional helper functions. You may wish to look at board.py
    	to see what functions are available to you.
    """

    global score
    score = [[150, -20, 20, 15, 15, 20, -20, 150],\
             [-20, -40, -8, -6, -6, -8, -40, -20],\
             [ 20,  -8,  6,  4,  4,  6,  -8,  20],\
             [ 15,  -6,  4,  2,  2,  4,  -6,  15],\
             [ 15,  -6,  4,  2,  2,  4,  -6,  15],\
             [ 20,  -8,  6,  4,  4,  6,  -8,  20],\
             [-20, -40, -8, -6, -6, -8, -40, -20],\
             [150, -20, 20, 15, 15, 20, -20, 150]]

    def __init__(self, gui, color=WHITE):
        self.color = color
        self.gui = gui
        self.moveCount = 0
        if self.color == WHITE:
            self.anticolor = BLACK
        else:
            self.anticolor = WHITE

    def get_current_board(self, board):
        self.current_board = board

    def evaluator(self, board):

        x, y, z = board.count_stones()
        if board.game_ended():
            if self.color == WHITE:
                return (x-y) * 1000000
            else:
                return (y-x) * 1000000
        score = [[150, -20, 20, 15, 15, 20, -20, 150],\
                 [-20, -40, -4, -3, -3, -4, -40, -20],\
                 [ 20,  -4,  6,  4,  4,  6,  -4,  20],\
                 [ 15,  -3,  4,  2,  2,  4,  -3,  15],\
                 [ 15,  -3,  4,  2,  2,  4,  -3,  15],\
                 [ 20,  -4,  6,  4,  4,  6,  -4,  20],\
                 [-20, -40, -4, -3, -3, -4, -40, -20],\
                 [150, -20, 20, 15, 15, 20, -20, 150]]
        self.alterScore(board)
        moveNum = len(board.get_valid_moves(self.color))
        antiMoveNum = len(board.get_valid_moves(self.anticolor))
        frontier = board.get_adjacent_count(self.color)
        antiFrontier = board.get_adjacent_count(self.anticolor)

        s = sum([score[i][j] if board.board[i][j] == self.color else -score[i][j] if board.board[i][j] == self.anticolor else 0 for i in range(8) for j in range(8)])
        s += 5*(moveNum - antiMoveNum)
        s += 5*(antiFrontier - frontier)


        return s

    def alterScore(self, board):
        if board.__getitem__(0,0) == self.color :
            score[1][0] = 50
            score[0][1] = 50
        if board.__getitem__(0,7) == self.color :
            score[1][7] = 50
            score[0][6] = 50
        if board.__getitem__(7,0) == self.color :
            score[7][1] = 50
            score[6][0] = 50
        if board.__getitem__(7,7) == self.color :
            score[6][7] = 50
            score[7][6] = 50

    def get_move(self):
        scores = []
        if self.moveCount < 26:

            for state in self.current_board.next_states(self.color) :
                scores.append(-self.negamax(state, 4, -1000000, 1000000, self.anticolor, -1))
                moves = self.current_board.get_valid_moves(self.color)
            self.current_board.apply_move(moves[scores.index(max(scores))], self.color)
        else:
            for state in self.current_board.next_states(self.color) :
                scores.append(-self.negamax(state, 10, -1000000, 1000000, self.anticolor, -1))
                moves = self.current_board.get_valid_moves(self.color)
            self.current_board.apply_move(moves[scores.index(max(scores))], self.color)
        self.moveCount+=1
        return 0, self.current_board


    def negamax(self, node, depth, a, b, color, c) :
        newColor = color
        if color == BLACK:
            newColor = WHITE
        else:
            newColor = BLACK
        if depth == 0 or node.game_ended():
            return c * self.evaluator(node)
        value = -1000000
        for state in node.next_states(color):
            value = max(value, -self.negamax(state, depth - 1, -b, -a, newColor, -c))
            a = max(a, value)
            if a >= b :
                break
        return value
