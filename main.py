from Algorithms.breathfirst import Breathfirst
from Classes.board import Board
from Algorithms.rndmover import RandomAlgorithm
import time

def main():
    start_time = time.time()
    algorithm = Breathfirst()
    algorithm2 = RandomAlgorithm()
    board = Board()
    with open("Game_2.txt", "r") as file:
        algorithm.board.load_board(file)
        algorithm.boards.append(algorithm.board)
    #algorithm2.branchboundSolver(10000)

    algorithm.move()
        #print("harrie")
    print(len(algorithm.boards))
    print(algorithm.counter_move)
    if algorithm.board_temp.won() == True:
        print("Won!")
        print(len(algorithm.boards))
        #return True
        parent = len(algorithm.boards) - 1
        print(algorithm.boards[parent])
        counter = 0
        while parent != 0:
            counter += 1
            parent = algorithm.boards[parent].parent
            print(algorithm.boards[parent])
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
