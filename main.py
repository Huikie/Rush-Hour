from Algorithms.breadthfirst import Breadthfirst
from Classes.board import Board
from Algorithms.rndmover import RandomAlgorithm
import sys
import os.path

def main():
    algorithm = Breadthfirst()
    algorithm2 = RandomAlgorithm()
    board = Board()
    i = 0
    if os.path.exists(sys.argv[1]):
        with open(sys.argv[1], "r") as file:
            for i, l in enumerate(file):
                i += 1
            file.seek(0)
            if sys.argv[2] == "random":
                algorithm2.board.load_board(file, i)
                algorithm2.branchBound(100, i)
            elif sys.argv[2] == "breadthfirst":
                algorithm.board.load_board(file, i)
                algorithm.boards.append(algorithm.board)
                algorithm.breadthFirst(i)
            else:
                print("invalid algorithm")
    else:
        print("No such file '{}'".format(sys.argv[1]))

if __name__ == "__main__":
    main()
