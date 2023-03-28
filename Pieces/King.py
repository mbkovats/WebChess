from Pieces.GamePiece import GamePiece


class King(GamePiece):
    def __init__(self, x, y, white) -> None:
        super().__init__(x, y, white, self)
        self.moved = False

    def ifPossible(self, move, board):
        if (move.x <= 1 and move.x >= 8) or (move.y <= 1 and move.y >= 8):
            pass
        elif move.occupied:
            if move.piece.white == self.white:
                return "FAIL"
        # Moving
        if abs(move.y - self.location.y) == 1 and move.x == self.location.x:
            if self.capture(move) != "NVM":
                return self.capture(move)
            return "PASS"
        elif abs(move.x - self.location.x) == 1 and move.y == self.location.y:
            if self.capture(move) != "NVM":
                return self.capture(move)
            return "PASS"
        elif abs(move.y - self.location.y) == 1 and abs(move.x - self.location.x) == 1:
            if self.capture(move) != "NVM":
                return self.capture(move)
            return "PASS"
        elif abs(move.x - self.location.x) == 1 and abs(move.y - self.location.y) == 1:
            if self.capture(move) != "NVM":
                return self.capture(move)
            return "PASS"
        # Castling
        elif not self.moved:
            if move.y == self.location.y and abs(move.x - self.location.x) == 2:
                if move.x > self.location.x:
                    if (
                        not board[move.y - 1][self.location.x].location.occupied
                        and not board[move.y - 1][self.location.x + 1].location.occupied
                    ):
                        if not board[move.y - 1][self.location.x + 2].moved:
                            return "SCASTLE"
                elif move.x < self.location.x:
                    if (
                        not board[move.y - 1][self.location.x - 2].location.occupied
                        and not board[move.y - 1][self.location.x - 3].location.occupied
                        and not board[move.y - 1][self.location.x - 4].location.occupied
                    ):
                        if not board[move.y - 1][self.location.x - 5].moved:
                            return "LCASTLE"
        return "FAIL"
