from Algorithms.breathfirst import Breathfirst
from Classes.board import Board
from Algorithms.rndmover import RandomAlgorithm
import time

def main():
    start_time = time.time()
    algorithm = Breathfirst()
    algorithm2 = RandomAlgorithm()
    board = Board()
    with open("Game_1.txt", "r") as file:
        algorithm.board.load_board(file)
        algorithm.boards.append(algorithm.board)
    #algorithm2.branchboundSolver(10000)

    algorithm.move()
        #print("harrie")

    if algorithm.board_temp.won() == True:
        print("Won!")
        print(len(algorithm.boards))
        #return True
        parent = algorithm.archive[str([self.board_temp.board])]
        print(algorithm.archive[parent])
        counter = 0
        while parent != 0:
            counter += 1
            parent = algorithm.archive[parent]
            print(algorithm.archive[parent])
        elapsed_time = time.time() - start_time
        print("\nPlease read the solution from bottom to top!")
        print("\nThe algorithm took", round(elapsed_time, 2), "seconds to solve the board!")
        print("Minimum amount of moves required to win the game:", counter)

    #algorithm.board.move("d", -2)
    #print(algorithm.board.board)


    #     board.load_board(file)
    #
    # if board.move("z", 3) == True:
    #     print("yes")
    # else:
    #     print("nope")
    #print(algorithm.board.board)
    #print(algorithm.board.cars.cars.keys())
    #print(algorithm.board.cars.cars)





if __name__ == "__main__":
    main()
