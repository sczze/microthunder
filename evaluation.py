import chess

# Piece values adapted from Michniewski's simplified evaluation function

PROMOTION_BONUS = {chess.QUEEN: 975, chess.ROOK: 500, chess.BISHOP: 325, chess.KNIGHT: 325}
PIECE_VALUES = {chess.PAWN: 100, chess.KNIGHT: 320, chess.BISHOP: 330, chess.ROOK: 500, chess.QUEEN: 900, chess.KING: 20000}
ATTACK_VALUES = {chess.PAWN: 50, chess.KNIGHT: 160, chess.BISHOP: 150, chess.ROOK: 250, chess.QUEEN: 500, chess.KING: 10000}
CHECK_BONUS = 10


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
        if piece is not None:
            if piece.color == chess.WHITE:
                score += PIECE_VALUES[piece.piece_type]
            else:
                score -= PIECE_VALUES[piece.piece_type]
    return score

def evaluate_move(move, board):
    if move not in board.legal_moves:
        return -float("inf")
    
    move_value = 1
    piece = board.piece_at(move.from_square)

    # check for captures
    if move.to_square in board.piece_map():
        captured_piece = board.piece_at(move.to_square)
        move_value += PIECE_VALUES[captured_piece.piece_type]

    # check for promotions
    if move.promotion:
        move_value += PROMOTION_BONUS[move.promotion]

    # check for attacks
    attacked_piece = board.piece_at(move.to_square)
    if attacked_piece and attacked_piece.color != piece.color:
        move_value += ATTACK_VALUES[piece.piece_type]

    # check for material advantage
    if move_value > 1:
        move_value += PIECE_VALUES[piece.piece_type]
    elif move_value < 1:
        move_value -= PIECE_VALUES[piece.piece_type]

    # check for check
    board.push(move)
    if board.is_check():
        move_value += CHECK_BONUS
    board.pop()

    return move_value
