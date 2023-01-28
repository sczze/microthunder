import chess
import time
import search
import evaluation

board = chess.Board()

# set the time control for the game (in seconds)
search.set_time_control(180)

while not board.is_game_over():
    search.set_start_time()
    best_move = search.get_best_move(board, 5)
    print(f"Best move: {best_move}")
    print(f"Evaluation score: {evaluation.evaluate_position(board)}")
    print(f"Time taken for move: {time.time() - search.start_time}")
    print(f"Time remaining: {search.get_time_remaining()} seconds")
    board.push(best_move)
    print(board)