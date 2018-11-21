from Algorithms.breathfirst import Breathfirst
def main():
    algorithm = Breathfirst()
    with open("Game_1.txt", "r") as file:
        algorithm.board.load_board(file)
        algorithm.boards.append(algorithm.board.board)
        algorithm.cars.append(algorithm.board.cars.cars)
    print(algorithm.board.board)
    print(algorithm.board.cars.cars.keys())
    print(algorithm.board.cars.cars)
    if algorithm.move() == True:
         print("yes")

         print(algorithm.board.board)
         print(algorithm.board.cars.cars)





if __name__ == "__main__":
    main()
