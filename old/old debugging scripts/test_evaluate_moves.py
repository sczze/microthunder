import chess
import evaluation

# create a new chess board
board = chess.Board()
board.set_fen("r7/ppp3pk/2n4p/8/2B5/5P2/PP4PP/n6K w - - 1 24")

# make a move on the board


move = chess.Move.from_uci("c4d3")
board.push(move)

# call the evaluate_move function and print the move value
move_value = evaluation.evaluate_move(move, board)
print(f"Move value: {move_value}")
