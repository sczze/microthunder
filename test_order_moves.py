import chess
from movegen import order_moves
from evaluation import evaluate_move

# Initialize board with a FEN position
board = chess.Board("rnbqk1nr/ppppp2p/5pp1/3N4/2P5/5N2/PP1bPPPP/R1BQKB1R w KQkq - 0 5")

# Generate list of legal moves
moves = list(board.legal_moves)

# Print moves and their values before ordering
print("Moves before ordering:")
for move in moves:
    print(f"{move}: {evaluate_move(move, board)}")

# Order moves using order_moves function
ordered_moves = order_moves(board, moves)

# Print moves and their values after ordering
print("Moves after ordering:")
for move in ordered_moves:
    print(f"{move}: {evaluate_move(move, board)}")
