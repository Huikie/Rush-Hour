from Algorithms.breathfirst import Breathfirst
from Classes.board import Board
from Algorithms.rndmover import RandomAlgorithm

def main():
    algorithm = Breathfirst()
    algorithm2 = RandomAlgorithm()
    board = Board()
    with open("Game_3.txt", "r") as file:
        algorithm2.board.load_board(file)
        #algorithm.boards.append(algorithm.board)
    algorithm2.branchboundSolver(100)

    # algorithm.move()






if __name__ == "__main__":
    main()
