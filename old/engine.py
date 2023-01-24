import chess
import time
import search
import evaluation

class ChessEngine:
    def __init__(self):
        self.board = chess.Board()
        self.searching = False

    def uci(self):
        return "MicroThunder\nSamuel Z."

    def isready(self):
        return "readyok"

    def ucinewgame(self):
        self.board.reset()

    def position(self, position):
        self.board.set_fen(position)

    def go(self, wtime, btime, winc, binc, movestogo=None, depth=None):
        self.searching = True
        start_time = time.time()
        if self.board.turn:
            remaining_time = wtime
        else:
            remaining_time = btime
        while self.searching:
            best_move = search.minimax(self.board, depth, evaluation.evaluate)
            if movestogo:
                remaining_time -= (time.time() - start_time) / movestogo
            else:
                remaining_time -= (time.time() - start_time)
            if remaining_time < 0:
                break
            if self.board.turn:
                remaining_time += winc
            else:
                remaining_time += binc
        return "bestmove " + str(best_move)

    def stop(self):
        self.searching = False

    def quit(self):
        exit()