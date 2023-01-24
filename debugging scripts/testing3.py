import chess
import evaluation

# create a board and set a position
board = chess.Board()
board.set_fen("r7/ppp3p1/7p/8/5k2/2BP4/PP4PP/7K w - - 1 24")

# print the FEN of the position
print("FEN:", board.fen())

# evaluate the position using the evaluation function
score = evaluation.evaluate_position(board)
print("Evaluation Score:", score)