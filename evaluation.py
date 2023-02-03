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


PIECE_PHASES = {
    chess.PAWN: 0,
    chess.KNIGHT: 1,
    chess.BISHOP: 1,
    chess.ROOK: 2,
    chess.QUEEN: 4
}

def evaluate_position(board):
    score = 0
    endgame = is_endgame(board)
    total_phase = 0

    # total game phase
    for piece_type in [chess.PAWN, chess.KNIGHT, chess.BISHOP, chess.ROOK, chess.QUEEN, chess.KING]:
        total_phase += count_pieces(board, piece_type) * PIECE_PHASES.get(piece_type, 0)
    phase = (total_phase * 256 + (total_phase / 2)) / total_phase

    # score
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece is None:
            continue
        piece_type = piece.piece_type
        color = piece.color

        # piece value
        piece_value = (MIDGAME_PIECE_VALUES[piece_type] * (256 - phase) +
                       ENDGAME_PIECE_VALUES[piece_type] * phase) / 256

        # square value
        psqt = MIDGAME_PSQT[piece_type] if not endgame else ENDGAME_PSQT[piece_type]
        square_value = psqt[square] if color == chess.WHITE else psqt[chess.square_mirror(square)]

        score += piece_value + square_value if color == chess.WHITE else -(piece_value + square_value)
    return score

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
