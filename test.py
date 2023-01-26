import chess
import movegen

board = chess.Board()

while not board.is_game_over():
    # Print the moves before ordering
    print("Moves before ordering:")
    for move in board.legal_moves:
        print(move)
        
    # Order the moves
    ordered_moves = movegen.order_moves(board, board.legal_moves)
    
    # Print the moves after ordering
    print("Moves after ordering:")
    for move in ordered_moves:
        print(move)
    
    # Get the best move
    best_move = movegen.get_best_move(board, 4)
    print("Best move:", best_move)
    
    # Make the best move
    board.push(best_move)
