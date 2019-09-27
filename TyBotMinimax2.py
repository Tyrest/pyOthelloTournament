
import random
import time
from config import WHITE, BLACK, EMPTY
from copy import deepcopy

class BotPlayer:

    """ Your custom player code goes here, but should implement
    	all of these functions. You are welcome to implement
    	additional helper functions. You may wish to look at board.py
    	to see what functions are available to you.
    """

    def __init__(self, gui, color=BLACK):
        self.color = color
        if self.color == WHITE:
            self.antiColor = BLACK
        else:
            self.antiColor = WHITE
        self.gui = gui

    def get_current_board(self, board):
        self.current_board = board

    def get_move(self):
        starttime = time.time()
        moves = []
        for nextBoard in self.current_board.next_states(self.color):
            moves.append(-self.negamax(nextBoard, 4, -999999, 999999, self.antiColor))
        validMoves = self.current_board.get_valid_moves(self.color)
        self.current_board.apply_move(validMoves[moves.index(max(moves))], self.color)
        print(str(self.evaluate(self.current_board)) + ' in: {} seconds'.format(time.time() - starttime))
        return 0, self.current_board

    def negamax(self, board, depth, alpha, beta, color):
        newColor = WHITE
        reverse = 1
        if color == WHITE:
            newColor = BLACK
            reverse = -1
        if depth == 0 or board.game_ended():
            return reverse * self.evaluate(board)
        value = -999999
        for nextBoard in board.next_states(color):
            value = max(value, -self.negamax(nextBoard, depth - 1, alpha, beta, newColor))
            beta = min(beta, value)
            if alpha >= beta:
                break
        return value

    def evaluate(self, board):
        score = 0
        score += self.generalPosition(board, self.color)
        score += self.stableSides(board, self.color)
        score -= 0.5 * self.stableSides(board, self.antiColor)
        if board.count_stones()[2] > 32:
            score += 4 * len(board.get_valid_moves(self.color))
        return score

    def generalPosition(self, board, fColor):
        score = 0
        posValues = [[50,-10, 5, 3, 3, 5,-15,50],
                     [-10,-25,-2,-2,-2,-2,-30,-15],\
                     [ 5,-2,-1,-1,-1,-1,-2, 5],\
                     [ 3,-2,-1,-1,-1,-1,-2, 3],\
                     [ 3,-2,-1,-1,-1,-1,-2, 3],\
                     [ 5,-2,-1,-1,-1,-1,-2, 5],\
                     [-15,-30,-2,-2,-2,-2,-30,-15],\
                     [50,-15, 5, 3, 3, 5,-15,50]]
        score = sum([posValues[x][y] for x in range(8) for y in range(8)\
        if board.__getitem__(x,y) == fColor])
        return score

    def stableSides(self, board, fColor):
        score = 0

        topLeftDown = True
        topLeftRight = True
        topRightDown = True
        topRightLeft = True
        botLeftUp = True
        botLeftRight = True
        botRightUp = True
        botRightLeft = True

        pos00 = board.__getitem__(0,0)
        pos07 = board.__getitem__(0,7)
        pos70 = board.__getitem__(7,0)
        pos77 = board.__getitem__(7,7)

        for x in range(1,7):
            if pos00 == fColor:
                if board.__getitem__(x,0) == fColor and topLeftDown:
                    score += 5
                else:
                    topLeftDown = False
                if board.__getitem__(0,x) == fColor and topLeftRight:
                    score += 5
                else:
                    topLeftRight = False

            if pos07 == fColor:
                if board.__getitem__(x,7) == fColor and topRightDown:
                    score += 5
                else:
                    topRightDown = False
                if board.__getitem__(0,7-x) == fColor and topRightLeft:
                    score += 5
                else:
                    topRightLeft = False

            if pos70 == fColor:
                if board.__getitem__(7-x,0) == fColor and botLeftUp:
                    score += 5
                else:
                    botLeftUp = False
                if board.__getitem__(7,x) == fColor and botLeftRight:
                    score += 5
                else:
                    botLeftRight = False

            if pos77 == fColor:
                if board.__getitem__(7-x,7) == fColor and botRightUp:
                    score += 5
                else:
                    botRightUp = False
                if board.__getitem__(7,7-x) == fColor and botRightLeft:
                    score += 5
                else:
                    botRightLeft = False
        return score
