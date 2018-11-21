from Algorithms.breathfirst import Breathfirst
def main():
    algorithm = Breathfirst()
    with open("Won_board.txt", "r") as file:
        algorithm.board.load_board(file)
        algorithm.boards.append(algorithm.board)
    print(algorithm.board.board)
    print(algorithm.board.cars.cars.keys())
    print(algorithm.board.cars.cars)
    #if algorithm.move() == True:
         #print("yes")
    if algorithm.board.won() == True:
        print("yes")

    print(algorithm.board.board)
    print(algorithm.board.cars.cars)





if __name__ == "__main__":
    main()
