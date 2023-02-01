import chess
import evaluation

# Create a board
fen = "1k6/7P/8/B1Q5/Rp6/1KPN4/8/8 w - - 0 1"
board = chess.Board(fen)

# Get the legal moves
moves = list(board.legal_moves)

# Evaluate each move
for move in moves:
    move_value = evaluation.evaluate_move(board, move)
    print(f"Move: {move}, Value: {move_value}")
