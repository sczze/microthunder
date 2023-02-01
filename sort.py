import chess

PROMOTION_VALUES = {
    chess.KNIGHT: 20,
    chess.BISHOP: 30,
    chess.ROOK: 50,
    chess.QUEEN: 100
}

def mvv_lva(victim, aggressor):
    """
    Function to get MVV-LVA values for a captured piece
    """
    MVV_LVA_VALUES = [                
        [0, 0, 0, 0, 0, 0, 0],       # victim K, attacker K, Q, R, B, N, P, None
        [50, 51, 52, 53, 54, 55, 0], # victim Q, attacker K, Q, R, B, N, P, None
        [40, 41, 42, 43, 44, 45, 0], # victim R, attacker K, Q, R, B, N, P, None
        [30, 31, 32, 33, 34, 35, 0], # victim B, attacker K, Q, R, B, N, P, None
        [20, 21, 22, 23, 24, 25, 0], # victim N, attacker K, Q, R, B, N, P, None
        [10, 11, 12, 13, 14, 15, 0], # victim P, attacker K, Q, R, B, N, P, None
        [0, 0, 0, 0, 0, 0, 0],       # victim None, attacker K, Q, R, B, N, P, None
    ]

    MVV_LVA_PIECE_TYPES = [chess.KING, chess.QUEEN, chess.ROOK, chess.BISHOP, chess.KNIGHT, chess.PAWN, None]

    if victim is None or aggressor is None:
        return 0
    
    victim_index = MVV_LVA_PIECE_TYPES.index(victim.piece_type)
    aggressor_index = MVV_LVA_PIECE_TYPES.index(aggressor.piece_type)
    return MVV_LVA_VALUES[victim_index][aggressor_index]

