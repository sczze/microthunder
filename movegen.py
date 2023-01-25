import chess
import evaluation
from evaluation import PROMOTION_BONUS
from evaluation import PIECE_VALUES
from evaluation import CHECK_BONUS


def alpha_beta_pruning(board, depth, alpha, beta, maximizing_player):
    # adjust the search depth based on remaining time
    depth = adjust_depth(depth)
    if depth == 0 or board.is_game_over():
        return evaluation.evaluate_position(board)

    if maximizing_player:
        best_value = -float("inf")
        for move in sorted(board.legal_moves, key=lambda m: evaluation.evaluate_move(board, m), reverse=True):
            board.push(move)
            value = alpha_beta_pruning(board, depth - 1, alpha, beta, False)
            board.pop()
            best_value = max(best_value, value)
            alpha = max(alpha, best_value)
            if beta <= alpha:
                break
        return best_value
    else:
        best_value = float("inf")
        for move in sorted(board.legal_moves, key=lambda m: evaluation.evaluate_move(board, m)):
            board.push(move)
            value = alpha_beta_pruning(board, depth - 1, alpha, beta, True)
            board.pop()
            best_value = min(best_value, value)
            beta = min(beta, best_value)
            if beta <= alpha:
                break
        return best_value



def get_best_move(board, depth):
    alpha = -float("inf")
    beta = float("inf")
    best_move = None
    best_value = -float("inf")
    for move in board.legal_moves:
        board.push(move)
        value = alpha_beta_pruning(board, depth - 1, alpha, beta, False)
        board.pop()

        if value > best_value:
            best_value = value
            best_move = move
    return best_move
