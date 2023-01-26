import chess
from evaluation import evaluate_position


max_depth = 3

def alphabeta(board, depth, alpha, beta, maximizing_player):
    if depth == 0 or board.is_game_over():
        return evaluate_position(board)

    if maximizing_player:
        best_value = -float("inf")
        for move in board.legal_moves:
            board.push(move)
            best_value = max(best_value, alphabeta(board, depth - 1, alpha, beta, False))
            board.pop()

            alpha = max(alpha, best_value)
            if alpha >= beta:
                break
        return best_value
    else:
        best_value = float("inf")
        for move in board.legal_moves:
            board.push(move)
            best_value = min(best_value, alphabeta(board, depth - 1, alpha, beta, True))
            board.pop()

            beta = min(beta, best_value)
            if alpha >= beta:
                break
        return best_value

def get_best_move(board, depth):
    alpha = -float("inf")
    beta = float("inf")
    best_move = None
    best_value = -float("inf")
    for move in board.legal_moves:
        board.push(move)
        value = alphabeta(board, depth - 1, alpha, beta, False)
        board.pop()

        if value > best_value:
            best_value = value
            best_move = move
    return best_move
