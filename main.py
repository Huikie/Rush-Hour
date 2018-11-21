from Algorithms.breathfirst import Breathfirst
def main():
    algorithm = Breathfirst()
    with open("Game_1.txt", "r") as file:
        algorithm.board.load_board(file)
        algorithm.boards.append(algorithm.board)
    #print(algorithm.board.board)
    #print(algorithm.board.cars.cars.keys())
    #print(algorithm.board.cars.cars)
    if algorithm.move() == True:
         print("yes")
         for board in algorithm.boards:
             print(board.board)
    if algorithm.board.won() == True:
        print("yes")





if __name__ == "__main__":
    main()
