import chess
import chess.engine
import subprocess
import time
import search
import evaluation

def main():
    engine = chess.engine.SimpleEngine.popen_uci("/home/samuel/Documents/Github/microthunder/src/dist/engine")

    while True:
        cmd = input()
        if cmd == "uci":
            engine.uci()
        elif cmd.startswith("setoption"):
            engine.setoption(cmd)
        elif cmd == "isready":
            engine.isready()
        elif cmd.startswith("position"):
            engine.position(cmd)
        elif cmd.startswith("go"):
            engine.go(cmd)
        elif cmd == "stop":
            engine.stop()
        elif cmd == "ponderhit":
            engine.ponderhit()
        elif cmd == "quit":
            engine.quit()
            break
    engine.terminate()