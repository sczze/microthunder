import time
import chess
from evaluation import evaluate_move, evaluate_position

def order_moves(board, moves):
    """
    Function to order moves based on their value, as determined by the evaluate_move function
    """
    move_value = [(move, evaluate_move(move, board)) for move in moves]
    return [move for move, value in sorted(move_value, key=lambda x: x[1], reverse=True)]

def negamax(board, depth, alpha, beta):
    """
    Function to perform negamax with alpha beta pruning
    """
    if depth == 0 or board.is_game_over():
        return evaluate_position(board)

    best_value = -float("inf")
    for move in order_moves(board, board.legal_moves):
        board.push(move)
        best_value = max(best_value, -negamax(board, depth - 1, -beta, -alpha))
        alpha = max(alpha, best_value)
        board.pop()
        if alpha >= beta:
            break
    return best_value

def get_best_move(board, depth, time_control=None, start_time=None):
    """
    Function to get the best move from the current board position using negamax and move ordering
    """
    alpha = -float("inf")
    beta = float("inf")
    best_move = None
    best_value = -float("inf")

    moves = order_moves(board, board.legal_moves)

    for move in moves:
        board.push(move)
        value = -negamax(board, depth - 1, -beta, -alpha)
        board.pop()
        if value > best_value:
            best_value = value
            best_move = move
        alpha = max(alpha, best_value)
        if alpha >= beta:
            break
    return best_move
