import chess
import evaluation

def order_moves(board, moves):
    """
    Function to order moves based on their value, as determined by the evaluate_move function
    """
    move_value = [(move, evaluation.evaluate_move(move, board)) for move in moves]
    return [move for move, value in sorted(move_value, key=lambda x: x[1], reverse=True)]

def alpha_beta_pruning(board, depth, alpha, beta, maximizing_player):
    """
    Function to perform minimax search with alpha beta pruning, using the ordered moves
    generated by the order_moves function
    """
    if depth == 0 or board.is_game_over():
        return evaluation.evaluate_position(board)

    if maximizing_player:
        best_value = -float("inf")
        for move in order_moves(board, board.legal_moves):
            board.push(move)
            value = alpha_beta_pruning(board, depth - 1, alpha, beta, False)
            board.pop()
            best_value = max(best_value, value)
            alpha = max(alpha, best_value)
            if alpha >= beta:
                break
        return best_value
    else:
        best_value = float("inf")
        for move in order_moves(board, board.legal_moves):
            board.push(move)
            value = alpha_beta_pruning(board, depth - 1, alpha, beta, True)
            board.pop()
            best_value = min(best_value, value)
            beta = min(beta, best_value)
            if alpha >= beta:
                break
        return best_value

def get_best_move(board, depth):
    alpha = -float("inf")
    beta = float("inf")
    best_move = None
    best_value = -float("inf")
    moves = order_moves(board, board.legal_moves) # order moves before evaluating
    for move in moves:
        board.push(move)
        value = alpha_beta_pruning(board, depth - 1, alpha, beta, False)
        board.pop()
        if value > best_value:
            best_value = value
            best_move = move
    return best_move
