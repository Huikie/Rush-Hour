from board import Board
def main():
    board = Board()
    counter1 = 0
    with open("Game_1.txt", "r") as file:
        for row in file:
            counter2 = 0
            counter1 += 1
            for char in row:
                counter2 += 1
                if char != "\n":
                    board.board[counter1][counter2] = char
    print(board.board)





if __name__ == "__main__":
    main()
