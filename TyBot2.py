
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
        move = self.strategy()
        self.current_board.apply_move(move[0], self.color)
        return 0, self.current_board

    def strategy(self):
        #validMoves = self.current_board.get_valid_moves(self.color)
        tempBoard = self.current_board
        validMoves = tempBoard.get_valid_moves(self.color)

        return random.sample(validMoves, 1)

    def minimax(self, board, depth, maximizingPlayer):
        if depth == 0 or board.game_ended():
            return self.evaluateBoard(board)
        if maximizingPlayer:
            value = -1000000
            for move in board.valid_moves():
                tempBoard = deepcopy(board)
                tempBoard.apply_move(move, self.color)
                eval = self.minimax(tempBoard, depth - 1, FALSE)
                if value < eval:
                    value = eval

                #value = max(value, self.minimax(tempBoard, depth - 1, FALSE))
            return value
        else:
            value = 1000000
            for tempBoard in [board.next_states()]
                value = min(value, self.minimax(tempBoard, depth − 1, TRUE))
            return value


    def evaluateBoard(self, b):
        score = 0
        for row in range(0,8):
            for col in range(0,8):
                if b.__getitem__(row, col) == self.COLOR:
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
            if b.__getitem__(0,0) == self.COLOR:
                if b.__getitem__(x,0) == self.COLOR and topLeftDown:
                    score += 2
                else:
                    topLeftDown = False
                if b.__getitem__(0,x) == self.COLOR and topLeftRight:
                    score += 2
                else:
                    topLeftRight = False
            if b.__getitem__(0,7) == self.COLOR:
                if b.__getitem__(x,7) == self.COLOR and topRightDown:
                    score += 2
                else:
                    topRightDown = False
                if b.__getitem__(0,7-x) == self.COLOR and topRightLeft:
                    score += 2
                else:
                    topRightLeft = False
            if b.__getitem__(7,0) == self.COLOR:
                if b.__getitem__(7-x,0) == self.COLOR and botLeftUp:
                    score += 2
                else:
                    botLeftUp = False
                if b.__getitem__(7,x) == self.COLOR and botLeftRight:
                    score += 2
                else:
                    botLeftRight = False
            if b.__getitem__(7,7) == self.COLOR:
                if b.__getitem__(7-x,7) == self.COLOR and botRightUp:
                    score += 2
                else:
                    botRightUp = False
                if b.__getitem__(7,7-x) == self.COLOR and botRightLeft:
                    score += 2
                else:
                    botRightLeft = False
        return score
