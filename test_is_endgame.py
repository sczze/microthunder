    # Check for endgame conditions
    # both sides have a queen and maximally one minor piece is endgame
    # both sides have two rook and maximally one minor piece is endgame
    # both sides have maximally one rook and maximally two minor pieces
    # Return True if endgame conditions are met, False otherwise

import chess
from evaluation import is_endgame

# FEN for middle game position
middle_game_fen = "2qknn2/8/8/8/8/8/8/2QKNN2 w - - 0 1"
board = chess.Board(middle_game_fen)
print(f"Is middle game endgame? {is_endgame(board)}")

# FEN for endgame position
endgame_fen = "2rknn2/8/8/8/8/8/8/2RKNN2 w - - 0 1"
board = chess.Board(endgame_fen)
print(f"Is endgame endgame? {is_endgame(board)}")
