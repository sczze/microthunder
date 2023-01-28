import chess
import search
import evaluation

# Initialize the chess board
board = chess.Board()

# Get the list of legal moves for the current position
moves = list(board.legal_moves)

# Order the moves using the move ordering function
ordered_moves = search.order_moves(board, moves)

# Print the value of each move along with the move
for move in ordered_moves:
    print(f"Move: {move}, Value: {evaluation.evaluate_move(move, board)}")
