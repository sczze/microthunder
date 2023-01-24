import chess
import evaluation

# create a board and set a position
board = chess.Board()
board.set_fen("r3k2r/ppp1b1pp/3p1n2/2qbpp2/3n4/8/PPPPPPPP/RNBQKBNR w KQkq - 16 13")

# print the FEN of the position
print("FEN:", board.fen())

# evaluate the position using the evaluation function
score = evaluation.evaluate_position(board)
print("Evaluation Score:", score)