import chess
import evaluation

board = chess.Board()

# test evaluate_move function
def test_evaluate_move():
    move_list = list(board.legal_moves)
    for move in move_list:
        move_value = evaluation.evaluate_move(move, board)
        print(f"Move: {move}, Value: {move_value}")

# test the function
test_evaluate_move()
