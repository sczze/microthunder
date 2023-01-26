import chess
import evaluation
import time
from evaluation import PROMOTION_BONUS
from evaluation import PIECE_VALUES
from evaluation import CHECK_BONUS

# global variables for depth and time control
max_depth = 5
time_control = None

def set_depth(depth):
    global max_depth
    max_depth = depth

def set_time_control(tc):
    global time_control
    time_control = tc

start_time = None
def set_start_time():
    global start_time
    start_time = time.time()

# function to get remaining time 
def get_time_remaining():
    global start_time
    global time_control
    return time_control - (time.time() - start_time)

# function to adjust depth based on remaining time
def adjust_depth(depth):
    time_remaining = get_time_remaining()
    if time_remaining < 30:
        depth = 1
    elif time_remaining < 60:
        depth = 2
    elif time_remaining < 120:
        depth = 3
    elif time_remaining < 240:
        depth = 4
    else:
        depth = max_depth
    return depth

def order_moves(board):
    """
    Function to order moves based on their value, as determined by the evaluate_move function
    """
    move_value = [(move, evaluation.evaluate_move(move, board)) for move in board.legal_moves]
    return [move for move, value in sorted(move_value, key=lambda x: x[1], reverse=True)]

def alpha_beta_pruning(board, move, depth, alpha, beta, maximizing_player):
    if depth == 0 or board.is_game_over():
        return evaluation.evaluate_position(board)

    board.push(move)
    if maximizing_player:
        value = -float("inf")
        for next_move in order_moves(board, board.legal_moves):
            value = max(value, alpha_beta_pruning(board, next_move, depth - 1, alpha, beta, False))
            alpha = max(alpha, value)
            if alpha >= beta:
                break
    else:
        value = float("inf")
        for next_move in order_moves(board, board.legal_moves):
            value = min(value, alpha_beta_pruning(board, next_move, depth - 1, alpha, beta, True))
            beta = min(beta, value)
            if alpha >= beta:
                break
    board.pop()
    return value

def get_best_move(board, depth):
    alpha = -float("inf")
    beta = float("inf")
    best_move = None
    best_value = -float("inf")
    for move in board.legal_moves:
        value = alpha_beta_pruning(board, move, depth - 1, alpha, beta, False)
        if value > best_value:
            best_value = value
            best_move = move
    return best_move