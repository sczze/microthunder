import chess
import time
import movegen

# Set up the board
board = chess.Board()

# Set a maximum search depth for the bot
max_depth = 5

while not board.is_game_over():
    # Get the best move for the current player
    start_time = time.time()
    best_move = movegen.get_best_move(board, max_depth)
    end_time = time.time()
    print("Time taken for move:", end_time - start_time)
    print("Evaluation score:", movegen.evaluate_position(board))
    print("Best move:", best_move)
    print()

    # Make the move on the board
    board.push(best_move)
    print(board)