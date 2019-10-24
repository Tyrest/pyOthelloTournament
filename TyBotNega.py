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
            moves.append(-self.negamax(nextBoard, 4, -99999999, 99999999, self.antiColor, -1))

        validMoves = self.current_board.get_valid_moves(self.color)
        self.current_board.apply_move(validMoves[moves.index(max(moves))], self.color)
        print('Took {} seconds'.format(time.time() - starttime))
        return 0, self.current_board

    def negamax(self, board, depth, a, b, color, c):
        # if depth = 0 or node is a terminal node then
        #     return color × the heuristic value of node
        # value := −∞
        # for each child of node do
        #     value := max(value, −negamax(child, depth − 1, −color))
        # return value

        newColor = WHITE
        if color == WHITE:
            newColor = BLACK

        if depth == 0 or board.game_ended():
            return c * self.evaluate(board)
        value = -99999999
        for nextBoard in board.next_states(color):
            value = max(value, -self.negamax(nextBoard, depth - 1, -b, -a, newColor, -c))
            a = max(a, value)
            if a >= b :
                break
        return value

    def evaluate(self, board):
        score = 0
        whiteNum, blackNum, emptyNum = board.count_stones()

        if self.color == WHITE:
            if emptyNum < 2:
                if whiteNum - blackNum > 0:
                    return 999999
                else:
                    return -999999
            if whiteNum == 0:
                return -999999
            elif blackNum == 0:
                return 999999
        else:
            if emptyNum < 2:
                if blackNum - whiteNum > 0:
                    return 999999
                else:
                    return -999999
            if blackNum == 0:
                return -999999
            elif whiteNum == 0:
                return 999999

        score += self.generalPosition(board, self.color)
        score -= self.generalPosition(board, self.antiColor)
        score += 5 * self.stableSides(board, self.color)
        score -= 5 * self.stableSides(board, self.antiColor)
        score -= 2 * board.get_adjacent_count(self.color)
        score += 2 * board.get_adjacent_count(self.antiColor)
        # score += 2 * len(board.get_valid_moves(self.color))
        # score -= 2 * len(board.get_valid_moves(self.antiColor))
        return score

    def generalPosition(self, board, fColor):
        score = 0
        posValues = [[ 50,-20,10, 8, 8,10,-20, 50],
                     [-20,-30,-8,-4,-4,-8,-30,-20],\
                     [ 10, -8, 0, 0, 0, 0, -8, 10],\
                     [  8, -4, 0, 3, 3, 0, -4,  8],\
                     [  8, -4, 0, 3, 3, 0, -4,  8],\
                     [ 10, -8, 0, 0, 0, 0, -8, 10],\
                     [-20,-30,-8,-4,-4,-8,-30,-20],\
                     [ 50,-20,10, 8, 8,10,-20, 50]]
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

        for x in range(1,6):
            if pos00 == fColor:
                if board.__getitem__(x,0) == fColor and topLeftDown:
                    score += 1
                else:
                    topLeftDown = False
                if board.__getitem__(0,x) == fColor and topLeftRight:
                    score += 1
                else:
                    topLeftRight = False

            if pos07 == fColor:
                if board.__getitem__(x,7) == fColor and topRightDown:
                    score += 1
                else:
                    topRightDown = False
                if board.__getitem__(0,7-x) == fColor and topRightLeft:
                    score += 1
                else:
                    topRightLeft = False

            if pos70 == fColor:
                if board.__getitem__(7-x,0) == fColor and botLeftUp:
                    score += 1
                else:
                    botLeftUp = False
                if board.__getitem__(7,x) == fColor and botLeftRight:
                    score += 1
                else:
                    botLeftRight = False

            if pos77 == fColor:
                if board.__getitem__(7-x,7) == fColor and botRightUp:
                    score += 1
                else:
                    botRightUp = False
                if board.__getitem__(7,7-x) == fColor and botRightLeft:
                    score += 1
                else:
                    botRightLeft = False
        return score
