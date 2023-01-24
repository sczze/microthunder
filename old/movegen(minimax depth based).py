import chess
import evaluation

max_depth = 3

def minimax(board, depth, maximizing_player):
    if depth == 0 or board.is_game_over():
        return evaluation.evaluate_position(board)

    best_value = -float("inf") if maximizing_player else float("inf")
    best_move = None

    for move in board.legal_moves:
        board.push(move)
        value = minimax(board, depth - 1, not maximizing_player)
        board.pop()

        if maximizing_player:
            if value > best_value:
                best_value = value
                best_move = move
        else:
            if value < best_value:
                best_value = value
                best_move = move

    if depth == max_depth:
        return best_move
    else:
        return best_value

def get_best_move(board, depth):
    return minimax(board, depth, True)
