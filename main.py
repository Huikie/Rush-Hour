from Algorithms.breathfirst import Breathfirst
from Classes.board import Board
def main():
    algorithm = Breathfirst()
    board = Board()
    with open("Game_1.txt", "r") as file:
        algorithm.board.load_board(file)
        algorithm.boards.append(algorithm.board)



    if algorithm.move() == True:
            if algorithm.board_temp.won() == True:
                print("Won!")
                return True
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
