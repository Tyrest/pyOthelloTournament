def evaluate(board, fColor, fAntiColor):
    def evaluateBoard(self, b):
        score = 0
        score += generalPosition(board, fColor, fAntiColor)
        score += stableSides(board, fColor, fAntiColor)
        return score

def generalPosition(board, fColor, fAntiColor):
    score = 0

    for row in range(0,8):
        for col in range(0,8):
            if b.__getitem__(row, col) == fColor:
                if (row == 0 or row == 7) and (col == 0 or col == 7):
                    score += 5
                else:
                    score += 1
            if b.__getitem__(row, col) == fAntiColor:
                if (row == 0 or row == 7) and (col == 0 or col == 7):
                    score -= 5
                else:
                    score -= 1
    return score

def stableSides(board, fColor, fAntiColor):
    score = 0

    topLeftDown = True
    topLeftRight = True
    topRightDown = True
    topRightLeft = True
    botLeftUp = True
    botLeftRight = True
    botRightUp = True
    botRightLeft = True

    pos00 = b.__getitem__(0,0)
    pos07 = b.__getitem__(0,7)
    pos70 = b.__getitem__(7,0)
    pos77 = b.__getitem__(7,7)

    for x in range(1,7):
        if pos00 == fColor:
            if b.__getitem__(x,0) == fColor and topLeftDown:
                score += 2
            else:
                topLeftDown = False
            if b.__getitem__(0,x) == fColor and topLeftRight:
                score += 2
            else:
                topLeftRight = False
        elif pos00 == fAntiColor:
            if b.__getitem__(x,0) == fAntiColor and topLeftDown:
                score -= 2
            else:
                topLeftDown = False
            if b.__getitem__(0,x) == fAntiColor and topLeftRight:
                score -= 2
            else:
                topLeftRight = False

        if pos07 == fColor:
            if b.__getitem__(x,7) == fColor and topRightDown:
                score += 2
            else:
                topRightDown = False
            if b.__getitem__(0,7-x) == fColor and topRightLeft:
                score += 2
            else:
                topRightLeft = False
        elif pos07 == fAntiColor:
            if b.__getitem__(x,7) == fAntiColor and topRightDown:
                score -= 2
            else:
                topRightDown = False
            if b.__getitem__(0,7-x) == fAntiColor and topRightLeft:
                score -= 2
            else:
                topRightLeft = False

        if pos70 == fColor:
            if b.__getitem__(7-x,0) == fColor and botLeftUp:
                score += 2
            else:
                botLeftUp = False
            if b.__getitem__(7,x) == fColor and botLeftRight:
                score += 2
            else:
                botLeftRight = False
        elif pos70 == fAntiColor:
            if b.__getitem__(7-x,0) == fAntiColor and botLeftUp:
                score -= 2
            else:
                botLeftUp = False
            if b.__getitem__(7,x) == fAntiColor and botLeftRight:
                score -= 2
            else:
                botLeftRight = False

        if pos77 == fColor:
            if b.__getitem__(7-x,7) == fColor and botRightUp:
                score += 2
            else:
                botRightUp = False
            if b.__getitem__(7,7-x) == fColor and botRightLeft:
                score += 2
            else:
                botRightLeft = False
        elif pos77 == fAntiColor:
            if b.__getitem__(7-x,7) == fAntiColor and botRightUp:
                score -= 2
            else:
                botRightUp = False
            if b.__getitem__(7,7-x) == fAntiColor and botRightLeft:
                score -= 2
            else:
                botRightLeft = False
    return score
