from Pieces.GamePiece import GamePiece
class Blank(GamePiece):
    def __init__(self, x, y, white) -> None:
        super().__init__(x, y, white, self)
        self.moved = False
        self.location.occupied = False
    def ifPossible(self, move, board):
        return "FAIL"