from Location import Location


class GamePiece:
    def __init__(self, x, y, white, piece) -> None:
        string = ""
        if x == 0:
            string = string + "A"
        elif x == 1:
            string = string + "B"
        elif x == 2:
            string = string + "C"
        elif x == 3:
            string = string + "D"
        elif x == 4:
            string = string + "E"
        elif x == 5:
            string = string + "F"
        elif x == 6:
            string = string + "G"
        elif x == 7:
            string = string + "H"
        string = string + str(y + 1)
        self.location = Location(string, piece)
        self.location.occupied = True
        self.location.piece = piece
        self.white = white
        self.piece = piece

    def capture(self, move):
        if move.occupied:
            if self.white == True:
                return "CAPTURED BLACK"
            elif self.white == False:
                return "CAPTURED WHITE"
        return "NVM"
