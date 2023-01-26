import chess
import evaluation

fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
board = chess.Board(fen)

print("Evaluation of position: ", evaluation.evaluate_position(board))
