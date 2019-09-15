
import random
from config import WHITE, BLACK, EMPTY
from copy import deepcopy

class BotPlayer:

    """ Your custom player code goes here, but should implement
    	all of these functions. You are welcome to implement
    	additional helper functions. You may wish to look at board.py
    	to see what functions are available to you.
    """

    def __init__(self, gui, color=WHITE):
        self.color = color
        if self.color == WHITE:
            self.antiColor = BLACK
        else:
            self.antiColor = WHITE
        self.gui = gui

    def get_current_board(self, board):
        self.current_board = board

    def get_move(self):
        print('moving...')
        move = self.strategy()
        self.current_board.apply_move(move, self.color)
        print(self.evaluate(self.current_board, self.color, self.antiColor))
        return 0, self.current_board

    def strategy(self):
        eval, move = self.minimax(self.current_board, 5, True)
        print(move)
        return move

    def minimax(self, board, depth, maximizingPlayer):
        if depth == 0 or board.game_ended():
            #return self.evaluateBoard(board), None
            return self.evaluate(board, self.color, self.antiColor), (0, 2)
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

    def evaluateBoard(self, b):
        score = 0
        for row in range(0,8):
            for col in range(0,8):
                if b.__getitem__(row, col) == self.color:
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
            if b.__getitem__(0,0) == self.color:
                if b.__getitem__(x,0) == self.color and topLeftDown:
                    score += 2
                else:
                    topLeftDown = False
                if b.__getitem__(0,x) == self.color and topLeftRight:
                    score += 2
                else:
                    topLeftRight = False
            if b.__getitem__(0,7) == self.color:
                if b.__getitem__(x,7) == self.color and topRightDown:
                    score += 2
                else:
                    topRightDown = False
                if b.__getitem__(0,7-x) == self.color and topRightLeft:
                    score += 2
                else:
                    topRightLeft = False
            if b.__getitem__(7,0) == self.color:
                if b.__getitem__(7-x,0) == self.color and botLeftUp:
                    score += 2
                else:
                    botLeftUp = False
                if b.__getitem__(7,x) == self.color and botLeftRight:
                    score += 2
                else:
                    botLeftRight = False
            if b.__getitem__(7,7) == self.color:
                if b.__getitem__(7-x,7) == self.color and botRightUp:
                    score += 2
                else:
                    botRightUp = False
                if b.__getitem__(7,7-x) == self.color and botRightLeft:
                    score += 2
                else:
                    botRightLeft = False
        return score

    def evaluate(self, board, fColor, fAntiColor):
        score = 0
        score += self.generalPosition(board, fColor, fAntiColor)
        score += self.stableSides(board, fColor, fAntiColor)
        return score

    def generalPosition(self, board, fColor, fAntiColor):
        score = 0

        for row in range(0,8):
            for col in range(0,8):
                if board.__getitem__(row, col) == fColor:
                    if (row == 0 or row == 7) and (col == 0 or col == 7):
                        score += 5
                    else:
                        score += 1
                if board.__getitem__(row, col) == fAntiColor:
                    if (row == 0 or row == 7) and (col == 0 or col == 7):
                        score -= 5
                    else:
                        score -= 1
        return score

    def stableSides(self, board, fColor, fAntiColor):
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
                    score += 2
                else:
                    topLeftDown = False
                if board.__getitem__(0,x) == fColor and topLeftRight:
                    score += 2
                else:
                    topLeftRight = False
            elif pos00 == fAntiColor:
                if board.__getitem__(x,0) == fAntiColor and topLeftDown:
                    score -= 2
                else:
                    topLeftDown = False
                if board.__getitem__(0,x) == fAntiColor and topLeftRight:
                    score -= 2
                else:
                    topLeftRight = False

            if pos07 == fColor:
                if board.__getitem__(x,7) == fColor and topRightDown:
                    score += 2
                else:
                    topRightDown = False
                if board.__getitem__(0,7-x) == fColor and topRightLeft:
                    score += 2
                else:
                    topRightLeft = False
            elif pos07 == fAntiColor:
                if board.__getitem__(x,7) == fAntiColor and topRightDown:
                    score -= 2
                else:
                    topRightDown = False
                if board.__getitem__(0,7-x) == fAntiColor and topRightLeft:
                    score -= 2
                else:
                    topRightLeft = False

            if pos70 == fColor:
                if board.__getitem__(7-x,0) == fColor and botLeftUp:
                    score += 2
                else:
                    botLeftUp = False
                if board.__getitem__(7,x) == fColor and botLeftRight:
                    score += 2
                else:
                    botLeftRight = False
            elif pos70 == fAntiColor:
                if board.__getitem__(7-x,0) == fAntiColor and botLeftUp:
                    score -= 2
                else:
                    botLeftUp = False
                if board.__getitem__(7,x) == fAntiColor and botLeftRight:
                    score -= 2
                else:
                    botLeftRight = False

            if pos77 == fColor:
                if board.__getitem__(7-x,7) == fColor and botRightUp:
                    score += 2
                else:
                    botRightUp = False
                if board.__getitem__(7,7-x) == fColor and botRightLeft:
                    score += 2
                else:
                    botRightLeft = False
            elif pos77 == fAntiColor:
                if board.__getitem__(7-x,7) == fAntiColor and botRightUp:
                    score -= 2
                else:
                    botRightUp = False
                if board.__getitem__(7,7-x) == fAntiColor and botRightLeft:
                    score -= 2
                else:
                    botRightLeft = False
        return score
