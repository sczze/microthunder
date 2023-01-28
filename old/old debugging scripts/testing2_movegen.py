import chess
import evaluation
import search
import time

board = chess.Board()

while not board.is_game_over():
    print("Evaluation score: ", evaluation.evaluate_position(board))
    start_time = time.time()
    best_move = search.get_best_move(board, 3)
    end_time = time.time()
    print("Time taken for move: ", end_time - start_time)
    board.push(best_move)
    print(board)
