from Classes.board import Board
def main():
    board = Board()
    counter1 = 0
    dict = {}
    with open("Game_1.txt", "r") as file:
        for row in file:
            counter2 = 0
            counter1 += 1
            for char in row:
                counter2 += 1
                if char.isalpha():
                    if char in dict:
                        dict[char].append([counter1, counter2])
                    else:
                        dict[char] = [[counter1, counter2]]
                if char != "\n":
                    board.board[counter1][counter2] = char
    board.cars.add(dict)
    print(board.cars.cars)
    if board.move("C") == True:
        print("yes")





if __name__ == "__main__":
    main()
