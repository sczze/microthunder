import chess
import movegen

board = chess.Board()

while not board.is_game_over():
    print(board)
    best_move = None
    best_score = -9999
    for move in board.legal_moves:
        board.push(move)
        score = movegen.evaluate_move(move, board)
        board.pop()
        if score > best_score:
            best_score = score
            best_move = move
    print("Best move:", best_move, "Score:", best_score)
    board.push(best_move)
