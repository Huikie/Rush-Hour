from Algorithms.breathfirst import Breathfirst
def main():
    algorithm = Breathfirst()
    with open("Game_1.txt", "r") as file:
        algorithm.board.load_board(file)

    print(algorithm.board.board)
    print(algorithm.board.cars.cars.keys())
    #algorithm.move(1)
    # print(algorithm.board.cars.cars)
    # if algorithm.board.move("C",1) == True:
    #     print("yes")
    # print(algorithm.board.board)
    # print(algorithm.board.cars.cars)





if __name__ == "__main__":
    main()
