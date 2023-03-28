from Pieces.GamePiece import GamePiece


class Pawn(GamePiece):
    def __init__(self, x, y, white) -> None:
        super().__init__(x, y, white, self)
        self.moved = False

    def ifPossible(self, move, board):
        returnval = "FAIL"
        if (move.x <= 1 and move.x >= 8) or (move.y <= 1 and move.y >= 8):
            pass
        elif move.occupied:
            if move.piece.white == self.white:
                return returnval
            else:
                if (
                    abs(move.x - self.location.x) == 1 and move.y == self.location.y + 1
                ) and self.white == True:
                    self.moved = True
                    returnval = "CAPTURED BLACK"
                elif (
                    abs(move.x - self.location.x) == 1 and move.y == self.location.y - 1
                ) and self.white == False:
                    self.moved = True
                    returnval = "CAPTURED WHITE"
        elif move.x != self.location.x:
            pass
        elif self.white == True:
            if self.moved:
                if move.y == self.location.y + 1:
                    returnval = "PASS"
            else:
                if move.y == self.location.y + 1 or move.y == self.location.y + 2:
                    self.moved = True
                    returnval = "PASS"
        else:
            if self.moved:
                if move.y == self.location.y - 1:
                    returnval = "PASS"
            else:
                if move.y == self.location.y - 1 or move.y == self.location.y - 2:
                    self.moved = True
                    returnval = "PASS"
        if returnval != "FAIL":
            if move.y == 8 or move.y == 1:
                if returnval == "CAPTURED BLACK":
                    return "PROMOTIONB"
                elif returnval == "CAPTURED WHITE":
                    return "PROMOTIONW"
                return "PROMOTION"
        return returnval
