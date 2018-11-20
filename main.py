from Algorithms.breathfirst import Breathfirst
def main():
    algorithm = Breathfirst()
    with open("Game_1.txt", "r") as file:
        algorithm.board.load_board(file)

    print(algorithm.board.board)
    print(algorithm.board.cars.cars.keys())
    print(algorithm.board.cars.cars)
    if algorithm.board.move("a",-3) == True:
         print("yes")

         print(algorithm.board.board)
         print(algorithm.board.cars.cars)





if __name__ == "__main__":
    main()
