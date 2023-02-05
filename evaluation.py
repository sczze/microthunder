import chess
from sort import mvv_lva, PROMOTION_VALUES
from evaluation_values import MIDGAME_PIECE_VALUES, ENDGAME_PIECE_VALUES, MIDGAME_PSQT, ENDGAME_PSQT

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

def count_pieces(board, piece_type):
    return len(board.pieces(piece_type, chess.WHITE)) + len(board.pieces(piece_type, chess.BLACK))

def evaluate_midgame_position(board):
    score = 0
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece is None:
            continue
        piece_type = piece.piece_type
        color = piece.color
        piece_value = MIDGAME_PIECE_VALUES[piece_type]
        psqt = MIDGAME_PSQT[piece_type]
        square_value = psqt[square] if color == chess.WHITE else psqt[chess.square_mirror(square)]
        score += piece_value + square_value if color == chess.WHITE else -(piece_value + square_value)
    return score

def evaluate_endgame_position(board):
    score = 0
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece is None:
            continue
        piece_type = piece.piece_type
        color = piece.color
        piece_value = ENDGAME_PIECE_VALUES[piece_type]
        psqt = ENDGAME_PSQT[piece_type]
        square_value = psqt[square] if color == chess.WHITE else psqt[chess.square_mirror(square)]
        score += piece_value + square_value if color == chess.WHITE else -(piece_value + square_value)
    return score

def calculate_phase(board):
    PAWN_PHASE = 0
    KNIGHT_PHASE = 1
    BISHOP_PHASE = 1
    ROOK_PHASE = 2
    QUEEN_PHASE = 4
    phase = 0
    total_phase = 16 * PAWN_PHASE + 4 * (KNIGHT_PHASE + BISHOP_PHASE + ROOK_PHASE) + 2 * QUEEN_PHASE
    
    for piece_type in [chess.PAWN, chess.KNIGHT, chess.BISHOP, chess.ROOK, chess.QUEEN]:
        for color in [chess.WHITE, chess.BLACK]:
            count = len(board.pieces(piece_type, color))
            if piece_type == chess.PAWN:
                phase -= count * PAWN_PHASE
            elif piece_type == chess.KNIGHT:
                phase -= count * KNIGHT_PHASE
            elif piece_type == chess.BISHOP:
                phase -= count * BISHOP_PHASE
            elif piece_type == chess.ROOK:
                phase -= count * ROOK_PHASE
            elif piece_type == chess.QUEEN:
                phase -= count * QUEEN_PHASE
    phase = (phase * 256 + (total_phase // 2)) // total_phase
    return phase


def evaluate_position(board):
    # The phase is a value between 0 and 256, with 0 representing the midgame and 256 representing the endgame
    phase = calculate_phase(board)
    
    # Create two separate tables for midgame and endgame evaluations
    midgame_eval = evaluate_midgame_position(board)
    endgame_eval = evaluate_endgame_position(board)
    
    # Interpolate between the midgame and endgame evaluations based on the phase
    return int((midgame_eval * (256 - phase) + endgame_eval * phase) / 256)

def evaluate_move(board, move):
    move_value = 0
    if board.is_capture(move):
        if True:
            victim = board.piece_at(move.to_square)
            aggressor = board.piece_at(move.from_square)
            move_value += mvv_lva(victim, aggressor)

    if move.promotion:
        move_value += PROMOTION_VALUES[move.promotion]

    return move_value
