'''

counter = 0
max_depth = 0

def negamax(board, depth, alpha, beta):
    global counter
    global max_depth
    max_depth = max(max_depth, depth)
    """
    Function to perform negamax with alpha beta pruning
    """
    if depth == 0 or board.is_game_over():
        return evaluate_position(board)

    best_value = -float("inf")
    for move in order_moves(board, board.legal_moves):
        counter += 1
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
    global counter
    global max_depth
    counter = 0
    max_depth = 0
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
    print("Number of moves searched: ", counter)
    print("Maximum depth searched: ", max_depth)
    return best_move



'''