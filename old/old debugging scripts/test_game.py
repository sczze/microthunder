import chess
import time
import movegen
import evaluation

board = chess.Board()

# set the time control for the game (in seconds)
movegen.set_time_control(180)

while not board.is_game_over():
    movegen.set_start_time()
    best_move = movegen.get_best_move(board, 5)
    print(f"Best move: {best_move}")
    print(f"Evaluation score: {evaluation.evaluate_position(board)}")
    print(f"Time taken for move: {time.time() - movegen.start_time}")
    print(f"Time remaining: {movegen.get_time_remaining()} seconds")
    board.push(best_move)
    print(board)