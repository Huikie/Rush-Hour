from Algorithms.breathfirst import Breathfirst
from Classes.board import Board
from Algorithms.rndmover import RandomAlgorithm
def main():
    algorithm = Breathfirst()
    algorithm2 = RandomAlgorithm()
    board = Board()
    with open("Game_1.txt", "r") as file:
        algorithm.board.load_board(file)
        algorithm.boards.append(algorithm.board)

    if algorithm.move() == True:
        print("harrie")

    if algorithm.board_temp.won() == True:
        print("Won!")
        print(len(algorithm.boards))
        #return True
        parent = len(algorithm.boards) -1
        print(algorithm.boards[parent].board)
        counter = 0
        while parent != 0:
            counter += 1
            parent = algorithm.boards[parent].parent
            print(algorithm.boards[parent].board)
        print(counter)

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
