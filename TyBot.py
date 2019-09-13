import random
from config import WHITE, BLACK, EMPTY

class BotPlayer:

    """ Your custom player code goes here, but should implement
    	all of these functions. You are welcome to implement
    	additional helper functions. You may wish to look at board.py
    	to see what functions are available to you.
    """

    def __init__(self, gui, color="white"):
        self.color = color
        self.gui = gui
        self.COLOR = WHITE

    def get_current_board(self, board):
        self.current_board = board

    def get_move(self):
        validMoves = self.current_board.get_valid_moves(self.color)
        move = self.strategy(validMoves)
        self.current_board.apply_move(move[0], self.color)
        print(self.evaluateBoard(self.current_board))
        return 0, self.current_board

    def strategy(self, validMoves):
        print(validMoves)
        bestMoves = []
        bestMoves.append(validMoves[0])
        moveValue = -1

        # Loops through the valid moves
        for move in validMoves:
            # Tests if the move is a corner
            if (move[0] == 0 or move[0] == 7) and (move[1] == 0 or move[1] == 7):
                if moveValue < 3:
                    bestMoves.clear()
                bestMoves.append(move)
                moveValue = 3
            # Tests if the row is in the middle
            elif move[0] > 1 and move[0] < 6 and moveValue < 3:
                # Tests if the move is in the middle 4x4
                if move[1] > 1 and move[1] < 6:
                    if moveValue < 2:
                        bestMoves.clear()
                    bestMoves.append(move)
                    moveValue = 2
                # Tests if the move is on a safe edge
                elif move[1] == 0 or move[1] == 7 and moveValue < 2:
                    if moveValue < 1:
                        bestMoves.clear()
                    bestMoves.append(move)
                    moveValue = 1
            # Tests if the col is in the middle
            elif move[1] > 1 and move[1] < 6 and moveValue < 2:
                #Tests if the move is on a safe edge
                if move[0] == 0 or move[0] == 7:
                    if moveValue < 1:
                        bestMoves.clear()
                    bestMoves.append(move)
                    moveValue = 1

        if moveValue == 3:
            print('Corner')
        if moveValue == 2:
            print('Middle')
        if moveValue == 1:
            print('Safe Edge')
        if moveValue == 0:
            print('Buffer')
        if moveValue == -1:
            print('Bad')
            return random.sample(validMoves, 1)
        return random.sample(bestMoves, 1)

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
