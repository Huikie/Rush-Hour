from Algorithms.breathfirst import Breathfirst
from Classes.board import Board
from Algorithms.rndmover import RandomAlgorithm
import sys

def main():
    algorithm = Breathfirst()
    algorithm2 = RandomAlgorithm()
    board = Board()
    i = 0
    games = ["Game_1.txt", "Game_2.txt", "Game_3.txt", "Game_4.txt", "Game_5.txt", "Game_6.txt", "Game_7.txt"]
    if sys.argv[1] not in games:
        print("That's an invalid game")
    else:
        with open(sys.argv[1], "r") as file:
            with open(sys.argv[1], "r") as f:
                for i, l in enumerate(f):
                    i += 1
            if sys.argv[2] == "random":
                algorithm2.board.load_board(file, i)
            elif sys.argv[2] == "breathfirst":
                algorithm.board.load_board(file, i)
            else:
                print("invalid algorithm")

        if sys.argv[2] == "random":
            algorithm2.branchBound(100, i)
        if sys.argv[2] == "breathfirst":
            algorithm.boards.append(algorithm.board)
            algorithm.breadthFirst(i)






if __name__ == "__main__":
    main()
