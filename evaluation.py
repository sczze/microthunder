import chess

# Michniewski's piece values
PAWN_VALUE = 100
KNIGHT_VALUE = 325
BISHOP_VALUE = 325
ROOK_VALUE = 500
QUEEN_VALUE = 975
KING_VALUE = 20000


PAWN_PSQT = [
    0,  0,  0,  0,  0,  0,  0,  0,
    50, 50, 50, 50, 50, 50, 50, 50,
    10, 10, 20, 30, 30, 20, 10, 10,
    5,  5, 10, 25, 25, 10,  5,  5,
    0,  0,  0, 20, 20,  0,  0,  0,
    5, -5,-10,  0,  0,-10, -5,  5,
    5, 10, 10,-20,-20, 10, 10,  5,
    0,  0,  0,  0,  0,  0,  0,  0
]
KNIGHT_PSQT = [
    -50,-40,-30,-30,-30,-30,-40,-50,
    -40,-20,  0,  0,  0,  0,-20,-40,
    -30,  0, 10, 15, 15, 10,  0,-30,
    -30,  5, 15, 20, 20, 15,  5,-30,
    -30,  0, 15, 20, 20, 15,  0,-30,
    -30,  5, 10, 15, 15, 10,  5,-30,
    -40,-20,  0,  5,  5,  0,-20,-40,
    -50,-40,-30,-30,-30,-30,-40,-50,
]
BISHOP_PSQT = [
    -20,-10,-10,-10,-10,-10,-10,-20,
    -10,  0,  0,  0,  0,  0,  0,-10,
    -10,  0,  5, 10, 10,  5,  0,-10,
    -10,  5,  5, 10, 10,  5,  5,-10,
    -10,  0, 10, 10, 10, 10,  0,-10,
    -10, 10, 10, 10, 10, 10, 10,-10,
    -10,  5,  0,  0,  0,  0,  5,-10,
    -20,-10,-10,-10,-10,-10,-10,-20,
]
ROOK_PSQT = [
    0,  0,  0,  0,  0,  0,  0,  0,
    5, 10, 10, 10, 10, 10, 10,  5,
    -5,  0,  0,  0,  0,  0,  0, -5,
    -5,  0,  0,  0,  0,  0,  0, -5,
    -5,  0,  0,  0,  0,  0,  0, -5,
    -5,  0,  0,  0,  0,  0,  0, -5,
    -5,  0,  0,  0,  0,  0,  0, -5,
    0,  0,  0,  5,  5,  0,  0,  0
]
QUEEN_PSQT =[
    -20,-10,-10, -5, -5,-10,-10,-20,
    -10,  0,  0,  0,  0,  0,  0,-10,
    -10,  0,  5,  5,  5,  5,  0,-10,
    -5,  0,  5,  5,  5,  5,  0, -5,
    0,  0,  5,  5,  5,  5,  0, -5,
    -10,  5,  5,  5,  5,  5,  0,-10,
    -10,  0,  5,  0,  0,  0,  0,-10,
    -20,-10,-10, -5, -5,-10,-10,-20
]
MIDDLEGAME_KING_PSQT = [
    -30,-40,-40,-50,-50,-40,-40,-30,
    -30,-40,-40,-50,-50,-40,-40,-30,
    -30,-40,-40,-50,-50,-40,-40,-30,
    -30,-40,-40,-50,-50,-40,-40,-30,
    -20,-30,-30,-40,-40,-30,-30,-20,
    -10,-20,-20,-20,-20,-20,-20,-10,
     20, 20,  0,  0,  0,  0, 20, 20,
     20, 30, 10,  0,  0, 10, 30, 20
]
ENDGAME_KING_PSQT = [
    -50,-40,-30,-20,-20,-30,-40,-50,
    -30,-20,-10,  0,  0,-10,-20,-30,
    -30,-10, 20, 30, 30, 20,-10,-30,
    -30,-10, 30, 40, 40, 30,-10,-30,
    -30,-10, 30, 40, 40, 30,-10,-30,
    -30,-10, 20, 30, 30, 20,-10,-30,
    -30,-30,  0,  0,  0,  0,-30,-30,
    -50,-40,-30,-30,-30,-30,-40,-50
]

def is_endgame(board):
    # Count the number of queens and rooks on the board
    queens = 0
    rooks = 0
    for piece in board.piece_map().values():
        if piece.piece_type == chess.QUEEN:
            queens += 1
        elif piece.piece_type == chess.ROOK:
            rooks += 1
    # check if there are less than a queen and a rook left on the board
    if queens + rooks < 2:
        return True
    # check if there are less than a queen and a minor piece left on the board
    minor_pieces = 0
    for piece in board.piece_map().values():
        if piece.piece_type in [chess.KNIGHT, chess.BISHOP]:
            minor_pieces += 1
    if queens + minor_pieces < 2:
        return True
    return False

def evaluate_position(board):
    score = 0
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece is None:
            continue
        piece_value = 0
        if piece.piece_type == chess.PAWN:
            piece_value = PAWN_VALUE + PAWN_PSQT[square]
        elif piece.piece_type == chess.KNIGHT:
            piece_value = KNIGHT_VALUE + KNIGHT_PSQT[square]
        elif piece.piece_type == chess.BISHOP:
            piece_value = BISHOP_VALUE + BISHOP_PSQT[square]
        elif piece.piece_type == chess.ROOK:
            piece_value = ROOK_VALUE + ROOK_PSQT[square]
        elif piece.piece_type == chess.QUEEN:
            piece_value = QUEEN_VALUE + QUEEN_PSQT[square]
        elif piece.piece_type == chess.KING:
            if is_endgame(board):
                piece_value = KING_VALUE + MIDDLEGAME_KING_PSQT[square]
            else:
                piece_value = KING_VALUE + ENDGAME_KING_PSQT[square]

        score += piece_value if piece.color == chess.WHITE else -piece_value
    return score
