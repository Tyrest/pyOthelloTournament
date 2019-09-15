
import random
from config import WHITE, BLACK, EMPTY
class BotPlayer:

    """ Your custom player code goes here, but should implement
    	all of these functions. You are welcome to implement
    	additional helper functions. You may wish to look at board.py
    	to see what functions are available to you.
    """
    global score
    score = [[150, -20, 20, 15, 15, 20, -20, 150],\
             [-20, -40, -4, -3, -3, -4, -40, -20],\
             [ 20,  -4,  6,  4,  4,  6,  -4,  20],\
             [ 15,  -3,  4,  2,  2,  4,  -3,  15],\
             [ 15,  -3,  4,  2,  2,  4,  -3,  15],\
             [ 20,  -4,  6,  4,  4,  6,  -4,  20],\
             [-20, -40, -4, -3, -3, -4, -40, -20],\
             [150, -20, 20, 15, 15, 20, -20, 150]]

    def __init__(self, gui, color=BLACK):
        self.color = color
        self.gui = gui
        if self.color == WHITE:
            self.anticolor = BLACK
        else:
            self.anticolor = WHITE

    def get_current_board(self, board):
        self.current_board = board

    def evaluator(self, board):

        x, y, z = board.count_stones()
        if self.color == WHITE:
            return 10 * (x - y) / (2*z + 1) - board.get_adjacent_count(self.color) + sum([score[i][j] if board.board[i][j] == self.color else 0 if board.board[i][j] == EMPTY else -score[i][j]*2/3 for i in range(8) for j in range(8)])
        else:
            return 10 * (y - x) / (2*z + 1) - board.get_adjacent_count(self.color) + sum([score[i][j] if board.board[i][j] == self.color else 0 if board.board[i][j] == EMPTY else -score[i][j]*2/3 for i in range(8) for j in range(8)])

    def get_move(self):
        scores = []
        for state in self.current_board.next_states(self.color) :
            scores.append(-self.negamax(state, 4, -1000000, 1000000, self.anticolor, -1))
        moves = self.current_board.get_valid_moves(self.color)
        self.current_board.apply_move(moves[scores.index(max(scores))], self.color)
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
