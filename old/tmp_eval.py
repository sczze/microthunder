from chess import *
from evaluation_values import *

# TEST/OLD IMPLEMENTATIONS

def evaluate_position(board):
    score = 0
    endgame = is_endgame(board)

    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece is None:
            continue
        piece_type = piece.piece_type
        color = piece.color
        if endgame:
            piece_value = ENDGAME_PIECE_VALUES[piece_type]
            psqt = ENDGAME_PSQT[piece_type]
        else:
            piece_value = MIDGAME_PIECE_VALUES[piece_type]
            psqt = MIDGAME_PSQT[piece_type]
        
        square_value = psqt[square] if color == chess.WHITE else psqt[chess.square_mirror(square)]
        score += piece_value + square_value if color == chess.WHITE else -(piece_value + square_value)
    return score

def evaluate_position(board):
    score = 0
    endgame = is_endgame(board)
    phase = calculate_phase(board)

    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece is None:
            continue
        piece_type = piece.piece_type
        color = piece.color
        midgame_piece_value = MIDGAME_PIECE_VALUES[piece_type]
        endgame_piece_value = ENDGAME_PIECE_VALUES[piece_type]
        midgame_psqt = MIDGAME_PSQT[piece_type]
        endgame_psqt = ENDGAME_PSQT[piece_type]

        piece_value = (midgame_piece_value * (256 - phase) + endgame_piece_value * phase) / 256
        psqt = (midgame_psqt * (256 - phase) + endgame_psqt * phase) / 256
        
        square_value = psqt[square] if color == chess.WHITE else psqt[chess.square_mirror(square)]
        score += piece_value + square_value if color == chess.WHITE else -(piece_value + square_value)
    return score


def calculate_phase(board):
    wp = len([square for square in chess.SQUARES if board.piece_at(square) == chess.Piece(chess.PAWN, chess.WHITE)])
    bp = len([square for square in chess.SQUARES if board.piece_at(square) == chess.Piece(chess.PAWN, chess.BLACK)])
    wn = len([square for square in chess.SQUARES if board.piece_at(square) == chess.Piece(chess.KNIGHT, chess.WHITE)])
    bn = len([square for square in chess.SQUARES if board.piece_at(square) == chess.Piece(chess.KNIGHT, chess.BLACK)])
    wb = len([square for square in chess.SQUARES if board.piece_at(square) == chess.Piece(chess.BISHOP, chess.WHITE)])
    bb = len([square for square in chess.SQUARES if board.piece_at(square) == chess.Piece(chess.BISHOP, chess.BLACK)])
    wr = len([square for square in chess.SQUARES if board.piece_at(square) == chess.Piece(chess.ROOK, chess.WHITE)])
    br = len([square for square in chess.SQUARES if board.piece_at(square) == chess.Piece(chess.ROOK, chess.BLACK)])
    wq = len([square for square in chess.SQUARES if board.piece_at(square) == chess.Piece(chess.QUEEN, chess.WHITE)])
    bq = len([square for square in chess.SQUARES if board.piece_at(square) == chess.Piece(chess.QUEEN, chess.BLACK)])

    TotalPhase = 16 * PawnPhase + 4 * KnightPhase + 4 * BishopPhase + 4 * RookPhase + 2 * Queen Phase
    phase = TotalPhase
    phase -= wp * PawnPhase
    phase -= wn * KnightPhase
    phase -= wb * BishopPhase
    phase -= wr * RookPhase
    phase -= wq * QueenPhase
    phase -= bp * PawnPhase
    phase -= bn * KnightPhase
    phase -= bb * BishopPhase
    phase -= br * RookPhase
    phase -= bq * Queen Phase
    phase = (phase * 256 + (TotalPhase / 2)) // TotalPhase
    return phase



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
        mid_psqt = MIDGAME_PSQT[piece_type] 
        end_psqt = ENDGAME_PSQT[piece_type]
        square_value = mid_psqt[square] * (256 - phase) + end_psqt[square] * phase / 256
        square_value = square_value if color == chess.WHITE else -square_value

        score += piece_value + square_value if color == chess.WHITE else -(piece_value + square_value)
    return score





def evaluate_position(board):
    # The phase is a value between 0 and 256, with 0 representing the midgame and 256 representing the endgame
    phase = calculate_phase(board)
    
    # Create two separate tables for midgame and endgame evaluations
    midgame_eval = evaluate_midgame_position(board)
    endgame_eval = evaluate_endgame_position(board)
    
    # Interpolate between the midgame and endgame evaluations based on the phase
    return int((midgame_eval * (256 - phase) + endgame_eval * phase) / 256)

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
    pawn_phase = 0
    knight_phase = 1
    bishop_phase = 1
    rook_phase = 2
    queen_phase = 4
    total_phase = pawn_phase * 16 + knight_phase * 4 + bishop_phase * 4 + rook_phase * 4 + queen_phase * 2

    phase = total_phase
    for piece_type, count in board.piece_count().items():
        if piece_type == chess.PAWN:
            phase -= count * pawn_phase
        elif piece_type == chess.KNIGHT:
            phase -= count * knight_phase
        elif piece_type == chess.BISHOP:
            phase -= count * bishop_phase
        elif piece_type == chess.ROOK:
            phase -= count * rook_phase
        elif piece_type == chess.QUEEN:
            phase -= count * queen_phase

    phase = (phase * 256 + total_phase // 2) // total_phase
    return phase
