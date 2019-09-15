
import random
import time
import multiprocessing
from multiprocessing import Array
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
        self.antiColor = WHITE
        if self.color == WHITE:
            self.anticolor = BLACK
        self.gui = gui

    def get_current_board(self, board):
        self.current_board = board

    def get_move(self):
        starttime = time.time()
        nextMoves = Array('d', len(self.current_board.get_valid_moves(self.color)))
        processes = []
        i = 0

        for nextBoard in self.current_board.next_states(self.color):
            p = multiprocessing.Process(target=self.multiHelper, args=(i, nextBoard, nextMoves,))
            i += 1
            processes.append(p)
            p.start()
        for process in processes:
            process.join()

        validMoves = self.current_board.get_valid_moves(self.color)
        nextMoves = list(nextMoves)
        move = validMoves[nextMoves.index(max(nextMoves))]
        self.current_board.apply_move(move, self.color)
        print(str(move) + ' in: {} seconds'.format(time.time() - starttime))
        return 0, self.current_board

    def multiHelper(self, i, nextBoard, nextMoves):
        nextMoves[i] = -self.negamax(nextBoard, 4, -999999, 999999, self.antiColor)
        pass

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
        whiteNum, blackNum, emptyNum = board.count_stones()
        if emptyNum < 2:
            if self.color == WHITE:
                score += 10 * whiteNum - blackNum
            else:
                score += 10 * blackNum - whiteNum
        score += self.generalPosition(board, self.color)
        score -= 0.5 * self.generalPosition(board, self.antiColor)
        score += 5 * self.stableSides(board, self.color)
        score -= 2.5 * self.stableSides(board, self.antiColor)
        if emptyNum > 48:
            score += len(board.get_valid_moves(self.color))
            score -= board.get_adjacent_count(self.color)
        return score

    def generalPosition(self, board, fColor):
        score = 0
        posValues = [[50,-10, 5, 3, 3, 5,-15,50],
                     [-10,-30,-2,-2,-2,-2,-30,-15],\
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
