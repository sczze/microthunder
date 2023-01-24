def minimax(board, depth, evaluate_func, maximizingPlayer=True, alpha=-float('inf'), beta=float('inf')):
    """Implement the minimax algorithm with alpha-beta pruning"""
    if depth == 0 or board.is_game_over():
        return evaluate_func(board)
    best_move = None
    if maximizingPlayer:
        max_eval = -float('inf')
        for move in board.legal_moves:
            board.push(move)
            eval = minimax(board, depth - 1, evaluate_func, False, alpha, beta)
            board.pop()
            if eval > max_eval:
                max_eval = eval
                best_move = move
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return best_move
    else:
        min_eval = float('inf')
        for move in board.legal_moves:
            board.push(move)
            eval = minimax(board, depth - 1, evaluate_func, True, alpha, beta)
            board.pop()
            if eval < min_eval:
                min_eval = eval
                best_move = move
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return best_move
