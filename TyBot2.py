
import random
from config import WHITE, BLACK, EMPTY
from copy import deepcopy

class BotPlayer:

    """ Your custom player code goes here, but should implement
    	all of these functions. You are welcome to implement
    	additional helper functions. You may wish to look at board.py
    	to see what functions are available to you.
    """

    def __init__(self, gui, color=WHITE, antiColor=BLACK):
        self.color = color
        self.antiColor = antiColor
        self.gui = gui

    def get_current_board(self, board):
        self.current_board = board

    def get_move(self):
        move = self.strategy()
        self.current_board.apply_move(move, self.color)
        return 0, self.current_board

    def strategy(self):
        eval, move = self.minimax(self.current_board, 5, True)
        print(move)
        return move

    def minimax(self, board, depth, maximizingPlayer):
        if depth == 0 or board.game_ended():
            return self.evaluateBoard(board, self.color), None
        if maximizingPlayer:
            value = -1000000
            validMoves = board.get_valid_moves(self.color)
            bestMove = None
            for move in validMoves:
                tempBoard = deepcopy(board)
                tempBoard.apply_move(move, self.color)
                eval, dontMatter = self.minimax(tempBoard, depth - 1, False)
                if value < eval:
                    value = eval
                    bestMove = move
            return value, bestMove
        else:
            value = 1000000
            validMoves = board.get_valid_moves(self.antiColor)
            bestMove = None
            for move in validMoves:
                tempBoard = deepcopy(board)
                tempBoard.apply_move(move, self.antiColor)
                eval, dontMatter = self.minimax(tempBoard, depth - 1, True)
                if value > eval:
                    value = eval
                    bestMove = move
            return value, bestMove

    def evaluateBoard(self, b, c):
        score = 0
        for row in range(0,8):
            for col in range(0,8):
                if b.__getitem__(row, col) == c:
                    if (row == 0 or row == 7) and (col == 0 or col == 7):
                        score += 5
                    else:
                        score += 1
        topLeftDown = True
        topLeftRight = True
        topRightDown = True
        topRightLeft = True
        botLeftUp = True
        botLeftRight = True
        botRightUp = True
        botRightLeft = True
        for x in range(1,7):
            if b.__getitem__(0,0) == c:
                if b.__getitem__(x,0) == c and topLeftDown:
                    score += 2
                else:
                    topLeftDown = False
                if b.__getitem__(0,x) == c and topLeftRight:
                    score += 2
                else:
                    topLeftRight = False
            if b.__getitem__(0,7) == c:
                if b.__getitem__(x,7) == c and topRightDown:
                    score += 2
                else:
                    topRightDown = False
                if b.__getitem__(0,7-x) == c and topRightLeft:
                    score += 2
                else:
                    topRightLeft = False
            if b.__getitem__(7,0) == c:
                if b.__getitem__(7-x,0) == c and botLeftUp:
                    score += 2
                else:
                    botLeftUp = False
                if b.__getitem__(7,x) == c and botLeftRight:
                    score += 2
                else:
                    botLeftRight = False
            if b.__getitem__(7,7) == c:
                if b.__getitem__(7-x,7) == c and botRightUp:
                    score += 2
                else:
                    botRightUp = False
                if b.__getitem__(7,7-x) == c and botRightLeft:
                    score += 2
                else:
                    botRightLeft = False
        return score
