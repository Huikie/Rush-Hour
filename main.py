from Code.Algorithms.breadthfirst import Breadthfirst
from Code.Classes.board import Board
from Code.Algorithms.randomBound import RandomBound
import sys
import os.path

def main():
    algorithm = Breadthfirst()
    algorithm2 = RandomBound()
    board = Board()
    i = 0

    # Checks if file board file exists
    if os.path.exists("Data/"+sys.argv[1]):
        with open("Data/"+sys.argv[1], "r") as file:

            # Gives the correct board size
            for i, l in enumerate(file):
                i += 1
            file.seek(0)

            # Starts Random bound algorithm
            if sys.argv[2] == "randombound":
                algorithm2.board.load_board(file, i)
                algorithm2.randomBound(100, i)

            # Starts breadthfirst algorithm
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
