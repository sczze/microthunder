import search
import chess

# Define the maximum depth of the minimax algorithm
max_depth = 3

# Initialize the board
board = chess.Board()

# Call the minimax function
try:
    best_move, best_score = search.minimax(board, max_depth, maximizing_player=True)
    print("Best move: ", best_move)
    print("Best score: ", best_score)
except Exception as e:
    print("An error occurred: ", e)
