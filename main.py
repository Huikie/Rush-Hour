from Classes.board import Board
def main():
    board = Board()
    with open("Game_1.txt", "r") as file:
        board.load_board(file)

    print(board.board)
    print(board.cars.cars)
    if board.move("C",1) == True:
        print("yes")
    print(board. board)
    print(board.cars.cars)





if __name__ == "__main__":
    main()
