import chess

# Piece values adapted from Michniewski's simplified evaluation function

PIECE_VALUES = {chess.PAWN: 100, chess.KNIGHT: 320, chess.BISHOP: 330, chess.ROOK: 500, chess.QUEEN: 900, chess.KING: 20000}

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
    white_queen = False
    black_queen = False
    white_rooks = 0
    black_rooks = 0
    white_minors = 0
    black_minors = 0
    
    for piece in board.piece_map().values():
        if piece.color == chess.WHITE:
            if piece.piece_type == chess.QUEEN:
                white_queen = True
            elif piece.piece_type == chess.ROOK:
                white_rooks += 1
            elif piece.piece_type in (chess.BISHOP, chess.KNIGHT):
                white_minors += 1
        else:
            if piece.piece_type == chess.QUEEN:
                black_queen = True
            elif piece.piece_type == chess.ROOK:
                black_rooks += 1
            elif piece.piece_type in (chess.BISHOP, chess.KNIGHT):
                black_minors += 1
    
    if white_queen and black_queen and white_minors <= 1 and black_minors <= 1:
        return True
    if white_rooks <= 2 and black_rooks <= 2 and white_minors <= 1 and black_minors <= 1:
        return True
    if white_rooks <= 1 and black_rooks <= 1 and white_minors <= 2 and black_minors <= 2:
        return True
    return False

def evaluate_position(board):
    score = 0
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece is None:
            continue
        piece_value = PIECE_VALUES[piece.piece_type]
        if piece.piece_type == chess.PAWN:
            piece_square_table = PAWN_PSQT
        elif piece.piece_type == chess.KNIGHT:
            piece_square_table = KNIGHT_PSQT
        elif piece.piece_type == chess.BISHOP:
            piece_square_table = BISHOP_PSQT
        elif piece.piece_type == chess.ROOK:
            piece_square_table = ROOK_PSQT
        elif piece.piece_type == chess.QUEEN:
            piece_square_table = QUEEN_PSQT
        elif piece.piece_type == chess.KING:
            if is_endgame(board):
                piece_square_table = ENDGAME_KING_PSQT
            else:
                piece_square_table = MIDDLEGAME_KING_PSQT
        
        if piece.color == chess.WHITE:
            score += piece_value + piece_square_table[square]
        else:
            score -= piece_value + piece_square_table[chess.square_mirror(square)]
    return score


PROMOTION_BONUS = {chess.QUEEN: 900, chess.ROOK: 500, chess.BISHOP: 330, chess.KNIGHT: 320}
ATTACK_VALUES = {chess.PAWN: 50, chess.KNIGHT: 160, chess.BISHOP: 150, chess.ROOK: 250, chess.QUEEN: 500, chess.KING: 10000}
CHECK_BONUS = 10

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
