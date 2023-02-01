import time
import chess
from search import get_best_move

def play_game():
    board = chess.Board()
    while not board.is_game_over():
        move = get_best_move(board, depth=5)
        board.push(move)
        print(board)
        print("\n")
        time.sleep(1)

if __name__ == '__main__':
    play_game()
