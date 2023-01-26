import chess
import evaluation

fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
board = chess.Board(fen)

print("Evaluation of position (neutral position): ", evaluation.evaluate_position(board), "\n")
equal = evaluation.evaluate_position(board)

fen = "rnbqkbnr/pppppppp/8/8/2PP1B2/2NBPN2/PP3PPP/R2QK2R w KQkq - 0 1"
board = chess.Board(fen)

print("Evaluation of position (white better): ", evaluation.evaluate_position(board), "\n")
white_better = evaluation.evaluate_position(board)

fen = "r2qk2r/ppp3pp/2npbn2/2b1pp2/8/8/PPPPPPPP/RNBQKBNR b KQkq - 3 8"
board = chess.Board(fen)

print("Evaluation of position (black better): ", evaluation.evaluate_position(board), "\n")
black_better = evaluation.evaluate_position(board)

if equal == 0:
    if white_better == 50:
        if black_better == -50:
            print("position eval working correctly!")
        else:
            print("position eval not working correctly!")
