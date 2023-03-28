from Pieces.GamePiece import GamePiece


class Queen(GamePiece):
    def __init__(self, x, y, white) -> None:
        super().__init__(x, y, white, self)

    def ifPossible(self, move, board):
        if (move.x <= 1 and move.x >= 8) or (move.y <= 1 and move.y >= 8):
            pass
        if move.occupied:
            if move.piece.white == self.white:
                return "FAIL"
        if move.x == self.location.x or move.y == self.location.y:
            if move.x > self.location.x:
                for i in range(self.location.x + 1, move.x):
                    if board[self.location.y - 1][i - 1].location.occupied:
                        return "FAIL"
            elif move.x < self.location.x:
                for i in range(move.x + 1, self.location.x - 1):
                    if board[self.location.y - 1][i - 1].location.occupied:
                        return "FAIL"
            elif move.y < self.location.y:
                for i in range(move.y + 1, self.location.y):
                    if board[i - 1][self.location.x - 1].location.occupied:
                        return "FAIL"
            elif move.y > self.location.y:
                for i in range(self.location.y + 1, move.y):
                    if board[i - 1][self.location.x - 1].location.occupied:
                        return "FAIL"
            if self.capture(move) != "NVM":
                return self.capture(move)
            return "PASS"
        elif abs(move.x - self.location.x) == abs(move.y - self.location.y):
            if move.x >= self.location.x and move.y >= self.location.y:
                for i in range(self.location.x + 1, move.x):
                    for j in range(self.location.y + 1, move.y):
                        if i - self.location.x == j - self.location.y:
                            if board[j - 1][i - 1].location.occupied:
                                return "FAIL"
            elif move.x <= self.location.x and move.y >= self.location.y:
                for i in range(move.x + 1, self.location.x):
                    for j in range(self.location.y + 1, move.y):
                        if self.location.x - i == j - self.location.y:
                            if board[j - 1][i - 1].location.occupied:
                                return "FAIL"
            elif move.x >= self.location.x and move.y <= self.location.y:
                for i in range(self.location.x + 1, move.x):
                    for j in range(move.y + 1, self.location.y):
                        if i - self.location.x == self.location.y - j:
                            if board[j - 1][i - 1].location.occupied:
                                return "FAIL"
            elif move.x <= self.location.x and move.y <= self.location.y:
                for i in range(move.x + 1, self.location.x):
                    for j in range(move.y + 1, self.location.y):
                        if self.location.x - i == self.location.y - j:
                            if board[j - 1][i - 1].location.occupied:
                                return "FAIL"
            if self.capture(move) != "NVM":
                return self.capture(move)
            return "PASS"
        return "FAIL"
