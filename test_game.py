import chess
import time
from evaluation import evaluate_move, evaluate_position
from movegen import order_moves, get_best_move

# Set up the board and initial position
board = chess.Board()

# Set the search depth
depth = 5

while not board.is_game_over():
    # Print the current board position
    print("Current position:")
    print(board)
    print()
    
    # Get the legal moves and their values before ordering
    moves = list(board.legal_moves)
    moves_values = [(move, evaluate_move(move, board)) for move in moves]
    print("Moves before ordering:")
    for move, value in moves_values:
        print(f"{move}: {value}")
    print()
    
    # Order the moves based on their values
    ordered_moves = order_moves(board, moves)
    moves_values = [(move, evaluate_move(move, board)) for move in ordered_moves]
    print("Moves after ordering:")
    for move, value in moves_values:
        print(f"{move}: {value}")
    print()

    # Get the best move
    best_move = get_best_move(board, 5)
    print("Best move:", best_move)
    print()

    # Make the move
    board.push(best_move)

# Print the final result of the game
print("Final position:")
print(board)
result = board.result()
print("Result:", result)
