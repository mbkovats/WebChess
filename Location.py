class Location():
    def __init__(self, square, piece) -> None:
        if square[0] == "A":
            self.x = 1
        if square[0] == "B":
            self.x = 2
        if square[0] == "C":
            self.x = 3
        if square[0] == "D":
            self.x = 4
        if square[0] == "E":
            self.x = 5
        if square[0] == "F":
            self.x = 6
        if square[0] == "G":
            self.x = 7
        if square[0] == "H":
            self.x = 8
        self.y = int(square[1])
        self.square = square
        self.occupied = False
        self.piece = piece