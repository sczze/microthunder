import chess
import evaluation

fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
board = chess.Board(fen)
print("Position evalation (starting position): ", evaluation.evaluate_position(board))
start = evaluation.evaluate_position(board)

fen = "k3bqrr/8/8/8/8/8/8/K2BBQRR w - - 0 1"
board = chess.Board(fen)
print("Position evalation (Midgame white up material): ", evaluation.evaluate_position(board))
a = evaluation.evaluate_position(board)

fen = "k2bbqrr/8/8/8/8/8/8/K3BQRR w - - 0 1"
board = chess.Board(fen)
print("Position evaluation (Midgame black up material): ", evaluation.evaluate_position(board))
b = evaluation.evaluate_position(board)

fen = "k5rr/8/8/8/8/8/8/K2B2RR w - - 0 1"
board = chess.Board(fen)
print("Position evaluation (Endgame white up material): ", evaluation.evaluate_position(board))
c = evaluation.evaluate_position(board)

fen = "k2b2rr/8/8/8/8/8/8/K5RR w - - 0 1"
board = chess.Board(fen)
print("Position evaluation (Endgame black up material): ", evaluation.evaluate_position(board))
d = evaluation.evaluate_position(board)

fen = "k5rr/8/8/8/3K4/8/8/6RR w - - 0 1"
board = chess.Board(fen)
print("Position evaluation (Endgame white up position): ", evaluation.evaluate_position(board))
e = evaluation.evaluate_position(board)

fen = "6rr/8/8/3k4/8/8/8/K5RR w - - 0 1"
board = chess.Board(fen)
print("Position evaluation (Endgame black up position): ", evaluation.evaluate_position(board))
f = evaluation.evaluate_position(board)

print("\n")

if start == 0 and a > 0 and b < 0 and c > 0 and d < 0 and e > 0 and f < 0:
    print("evaluate_position and is_endgame working correctly!")
else:
    print("*NOT* working correctly!")
