def evaluate(board):
    # Evaluation function only counts the material advantage as of now

    score = 0
    for piece, square in board.piece_map().items():
        score += PIECE_VALUES[piece.symbol()]
    return score
        
PIECE_VALUES = {
    'P': 100,
    'N': 320,
    'B': 330,
    'R': 500,
    'Q': 900,
    'K': 20000,
    'p': -100,
    'n': -320,
    'b': -330,
    'r': -500,
    'q': -900,
    'k': -20000
}
