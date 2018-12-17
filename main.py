from Code.Algorithms.breadthfirst import Breadthfirst
from Code.Classes.board import Board
from Code.Algorithms.randomBound import RandomBound
import sys
import os.path

def main():
    """Function that makes it possible to run the algorithms form the command line.
    """
    algorithmBF = Breadthfirst()
    algorithmRB = RandomBound()
    board = Board()
    i = 0

    # Checks if board file exists and if so opens it
    if os.path.exists("Data/"+sys.argv[1]):
        with open("Data/"+sys.argv[1], "r") as file:

            # Gives the board size
            for i, l in enumerate(file):
                i += 1
            file.seek(0)

            # Starts Random bound algorithm
            if sys.argv[2] == "randombound":
                algorithmRB.board.load_board(file, i)
                if int(sys.argv[3]) > 0:
                    algorithmRB.randomBound(sys.argv[3], i)
                else:
                    print("Invalid iteration size.")

            # Starts breadthfirst algorithm
            elif sys.argv[2] == "breadthfirst":
                algorithmBF.board.load_board(file, i)
                algorithmBF.boards.append(algorithmBF.board)
                algorithmBF.breadthFirst(i)
            else:
                print("Invalid algorithm.")
    else:
        print("No such file '{}'".format(sys.argv[1]))

if __name__ == "__main__":
    main()
