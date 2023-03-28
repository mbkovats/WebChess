from Pieces import *
from Location import Location
from flask import Flask, render_template, request
from json import dumps, loads

app = Flask(__name__)


@app.route("/")
def mainhtml():
    print(request.form)
    return render_template("page.html")


board = []
turnCounter = 0


def buildBoard():
    global board
    board = []
    global turnCounter
    turnCounter = 0
    for i in range(8):
        col = []
        for j in range(8):
            if i == 1:
                col.append(Pawn(j, i, True))
            elif i == 0:
                if j == 0 or j == 7:
                    col.append(Rook(j, i, True))
                if j == 1 or j == 6:
                    col.append(Knight(j, i, True))
                if j == 2 or j == 5:
                    col.append(Bishop(j, i, True))
                if j == 3:
                    col.append(Queen(j, i, True))
                if j == 4:
                    col.append(King(j, i, True))
            elif i == 6:
                col.append(Pawn(j, i, False))
            elif i == 7:
                if j == 0 or j == 7:
                    col.append(Rook(j, i, False))
                if j == 1 or j == 6:
                    col.append(Knight(j, i, False))
                if j == 2 or j == 5:
                    col.append(Bishop(j, i, False))
                if j == 3:
                    col.append(Queen(j, i, False))
                if j == 4:
                    col.append(King(j, i, False))
            else:
                col.append(Blank(j, i, False))
        board.append(col)


buildBoard()


def converter(square):
    if square[0] == "A":
        x = 0
    elif square[0] == "B":
        x = 1
    elif square[0] == "C":
        x = 2
    elif square[0] == "D":
        x = 3
    elif square[0] == "E":
        x = 4
    elif square[0] == "F":
        x = 5
    elif square[0] == "G":
        x = 6
    elif square[0] == "H":
        x = 7
    return board[int(square[1]) - 1][x]


temp = ""


@app.route("/move", methods=["POST", "GET"])
def javascript():
    global turnCounter
    global temp
    if request.method == "POST":
        arr = request.get_json(force=True)
        before = arr[0] + arr[1]
        after = arr[2] + arr[3]
        piece = converter(before)
        moveto = converter(after)
        if turnCounter % 2 == 0:
            if piece.white == True:
                pass
            else:
                return dumps("FAIL")
        elif turnCounter % 2 == 1:
            if piece.white == False:
                pass
            else:
                return dumps("FAIL")
        if isinstance(piece, Blank):
            pass
        else:
            move = piece.ifPossible(moveto.location, board)
            if move == "FAIL":
                pass
            else:
                turnCounter += 1
                board[piece.location.y - 1][piece.location.x - 1] = Blank(
                    piece.location.x - 1, piece.location.y - 1, False
                )
                board[moveto.location.y - 1][moveto.location.x - 1] = piece
                moveto.location.occupied = True
                moveto.location.piece = piece
                piece.location.occupied = False
                piece.location.piece.location = moveto.location
                if move == "SCASTLE":
                    if piece.white == True:
                        board[0][0] = Blank(0, 7, False)
                        board[0][5] = Rook(5, 0, True)
                    else:
                        board[7][7] = Blank(7, 7, False)
                        board[7][5] = Rook(5, 7, False)
                elif move == "LCASTLE":
                    if piece.white == True:
                        board[0][7] = Blank(0, 7, False)
                        board[0][3] = Rook(5, 0, True)
                    else:
                        board[7][0] = Blank(7, 7, False)
                        board[7][3] = Rook(5, 7, False)
                elif (
                    move == "PROMOTION" or move == "PROMOTIONB" or move == "PROMOTIONW"
                ):
                    temp = (
                        str(moveto.location.y)
                        + str(moveto.location.x)
                        + str(piece.white)
                    )
            return dumps(move)
    if request.method == "GET":
        buildBoard()
    return dumps("FAIL")


@app.route("/promote", methods=["POST"])
def promotion():
    global temp
    if temp[2] == "T":
        color = True
    else:
        color = False
    piece = request.get_json(force=True)
    if piece == "queen":
        board[int(temp[0]) - 1][int(temp[1]) - 1] = Queen(
            int(temp[1]) - 1, int(temp[0]) - 1, color
        )
    if piece == "bishop":
        board[int(temp[0]) - 1][int(temp[1]) - 1] = Bishop(
            int(temp[1]) - 1, int(temp[0]) - 1, color
        )
    if piece == "rook":
        board[int(temp[0]) - 1][int(temp[1]) - 1] = Rook(
            int(temp[1]) - 1, int(temp[0]) - 1, color
        )
    if piece == "knight":
        board[int(temp[0]) - 1][int(temp[1]) - 1] = Knight(
            int(temp[1]) - 1, int(temp[0]) - 1, color
        )
    return "PASS"


if __name__ == "__main__":
    app.run(debug=True)
