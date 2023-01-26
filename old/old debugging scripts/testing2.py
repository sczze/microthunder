import chess
import evaluation

board = chess.Board()
score = evaluation.evaluate_position(board)
print(score)

