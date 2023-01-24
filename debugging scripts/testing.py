import chess
import evaluation

# create a board and set a position
board = chess.Board()
board.set_fen("r7/ppp3pk/7p/8/2B2n2/3P4/PP4PP/n6K w - - 1 24")

# print the FEN of the position
print("FEN:", board.fen())

# evaluate the position using the evaluation function
score = evaluation.evaluate_position(board)
print("Evaluation Score:", score)

# print the piece-square tables
print("PAWN_PSQT:", evaluation.PAWN_PSQT)
print("KNIGHT_PSQT:", evaluation.KNIGHT_PSQT)
print("BISHOP_PSQT:", evaluation.BISHOP_PSQT)
print("ROOK_PSQT:", evaluation.ROOK_PSQT)
print("QUEEN_PSQT:", evaluation.QUEEN_PSQT)
print("KING_PSQT:", evaluation.MIDDLEGAME_KING_PSQT)
print("KING_PSQT:", evaluation.ENDGAME_KING_PSQT)

# print the piece values
print("PAWN_VALUE:", evaluation.PAWN_VALUE)
print("KNIGHT_VALUE:", evaluation.KNIGHT_VALUE)
print("BISHOP_VALUE:", evaluation.BISHOP_VALUE)
print("ROOK_VALUE:", evaluation.ROOK_VALUE)
print("QUEEN_VALUE:", evaluation.QUEEN_VALUE)
print("KING_VALUE:", evaluation.KING_VALUE)

# print the piece count
print("PAWN COUNT:", board.piece_count(chess.PAWN))
print("KNIGHT COUNT:", board.piece_count(chess.KNIGHT))
print("BISHOP COUNT:", board.piece_count(chess.BISHOP))
print("ROOK COUNT:", board.piece_count(chess.ROOK))
print("QUEEN COUNT:", board.piece_count(chess.QUEEN))

# print the piece score for each piece
for piece in board.piece_map().values():
    print("PIECE:", piece)
    print("PIECE TYPE:", piece.piece_type)
    print("PIECE SQUARE:", piece.square)
    print("PIECE VALUE:", evaluation.PIECE_VALUES[piece.piece_type])
    print("PIECE PSQT:", evaluation.PIECE_PSQT[piece.piece_type][piece.square])
    print("-------------------")
