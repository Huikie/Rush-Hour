from Classes.cars import Cars
import copy as copy
class Board:
    def __init__(self):
        self.board = [
        ['#', '#', '#', '#', '#', '#', '#','#'],
        ['#', '-', '-', '-', '-', '-', '-','#'],
        ['#', '-', '-', '-', '-', '-', '-','#'],
        ['#', '-', '-', '-', '-', '-', '-','>'],
        ['#', '-', '-', '-', '-', '-', '-','#'],
        ['#', '-', '-', '-', '-', '-', '-','#'],
        ['#', '-', '-', '-', '-', '-', '-','#'],
        ['#', '#', '#', '#', '#', '#', '#','#'],
        ]

# Board 9x9:
# ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
# ['#', '-', '-', '-', '-', '-', '-', '-', '-', '-', '#'],
# ['#', '-', '-', '-', '-', '-', '-', '-', '-', '-', '#'],
# ['#', '-', '-', '-', '-', '-', '-', '-', '-', '-', '#'],
# ['#', '-', '-', '-', '-', '-', '-', '-', '-', '-', '#'],
# ['#', '-', '-', '-', '-', '-', '-', '-', '-', '-', '>'],
# ['#', '-', '-', '-', '-', '-', '-', '-', '-', '-', '#'],
# ['#', '-', '-', '-', '-', '-', '-', '-', '-', '-', '#'],
# ['#', '-', '-', '-', '-', '-', '-', '-', '-', '-', '#'],
# ['#', '-', '-', '-', '-', '-', '-', '-', '-', '-', '#'],
# ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
# ]
        self.cars = Cars()
        self.board_temp = []
        self.cars_temp = {}
        self.parent = 0

    #Function that turns the board representation into a string
    def __repr__(self):
        return '\n' + '\n'.join(' '.join(field) for field in self.board)

    def load_board(self, file):
            board_text = file
            counter1 = 0
            dict = {}
            print(board_text)
            for row in board_text:
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
                        self.board[counter1][counter2] = char
            self.cars.add(dict)

    def won(self):
        if self.cars.cars["z"][1][1]  ==  6:
            return True
        else:
            return False


    def move(self, car, moves):
        lijst = []
        # Move cars that are positioned horizontally
        if self.cars.cars[car][0][0]== self.cars.cars[car][1][0]:
            # moves cars to the right
            if moves > 0:
                # checks if move is valid
                for i in range(1, moves + 1):
                    for cordinate in self.cars.cars[car]:
                        if self.board[cordinate[0]][cordinate[1] + i] != "." and self.board[cordinate[0]][cordinate[1] + i] != car :
                            return False
                #print(self.board)
                for cordinate in self.cars.cars[car]:
                    self.board[cordinate[0]][cordinate[1]] = "."
                for cordinate in self.cars.cars[car]:
                    self.board[cordinate[0]][cordinate[1]+ moves] = car
                for cordinate in self.cars.cars[car]:
                    lijst.append([cordinate[0], cordinate[1] + moves])
                    self.cars.cars[car] = lijst
                return True
                # moves car to the left
            elif moves < 0:
                # checks if move is valid
                for i in range(-1, moves -1, -1):
                    for cordinate in self.cars.cars[car]:
                        if self.board[cordinate[0]][cordinate[1] + i] != "." and self.board[cordinate[0]][cordinate[1] + i] != car :
                            return False
                for cordinate in self.cars.cars[car]:
                    self.board[cordinate[0]][cordinate[1]] = "."
                for cordinate in self.cars.cars[car]:
                    self.board[cordinate[0]][cordinate[1] + moves] = car
                for cordinate in self.cars.cars[car]:
                    lijst.append([cordinate[0], cordinate[1] + moves])
                    self.cars.cars[car] = lijst
                return True
        # Move cars that are positioned vertically
        else:
            # moves cars down
            if moves > 0:
                # checks if move is valid
                for i in range(1, moves + 1):
                    for cordinate in self.cars.cars[car]:
                        if self.board[cordinate[0] + i][cordinate[1]] != "." and self.board[cordinate[0] + i][cordinate[1]] != car :
                            return False
                for cordinate in self.cars.cars[car]:
                    self.board[cordinate[0]][cordinate[1]] = "."
                for cordinate in self.cars.cars[car]:
                    self.board[cordinate[0]+ moves][cordinate[1]] = car
                for cordinate in self.cars.cars[car]:
                    lijst.append([cordinate[0] + moves, cordinate[1]])
                    self.cars.cars[car] = lijst
                return True
                #self.cars.cars[car] = lijst
                #print(self.cars.cars[car])
            # moves cars up
            elif moves < 0:
                # checks if move is valid
                for i in range(-1, moves -1, -1):
                    for cordinate in self.cars.cars[car]:
                        if self.board[cordinate[0] + i][cordinate[1]] != "." and self.board[cordinate[0] + i][cordinate[1]] != car :
                            return False
                for cordinate in self.cars.cars[car]:
                    self.board[cordinate[0]][cordinate[1]] = "."
                for cordinate in self.cars.cars[car]:
                    self.board[cordinate[0]+ moves][cordinate[1]] = car
                for cordinate in self.cars.cars[car]:
                    lijst.append([cordinate[0] + moves, cordinate[1]])
                    self.cars.cars[car] = lijst
                return True

    def check_move(self, car, moves):
        lijst = []
        # Move cars that are positioned horizontally
        if self.cars.cars[car][0][0]== self.cars.cars[car][1][0]:
            # moves cars to the right
            if moves > 0:
                # checks if move is valid
                for i in range(1, moves + 1):
                    for cordinate in self.cars.cars[car]:
                        if self.board[cordinate[0]][cordinate[1] + i] != "." and self.board[cordinate[0]][cordinate[1] + i] != car :
                            return False
                return True
                # moves car to the left
            elif moves < 0:
                # checks if move is valid
                for i in range(-1, moves -1, -1):
                    for cordinate in self.cars.cars[car]:
                        if self.board[cordinate[0]][cordinate[1] + i] != "." and self.board[cordinate[0]][cordinate[1] + i] != car :
                            return False
                return True
        # Move cars that are positioned vertically
        else:
            # moves cars down
            if moves > 0:
                # checks if move is valid
                for i in range(1, moves + 1):
                    for cordinate in self.cars.cars[car]:
                        if self.board[cordinate[0] + i][cordinate[1]] != "." and self.board[cordinate[0] + i][cordinate[1]] != car :
                            return False
                return True
                #self.cars.cars[car] = lijst
                #print(self.cars.cars[car])
            # moves cars up
            elif moves < 0:
                # checks if move is valid
                for i in range(-1, moves -1, -1):
                    for cordinate in self.cars.cars[car]:
                        if self.board[cordinate[0] + i][cordinate[1]] != "." and self.board[cordinate[0] + i][cordinate[1]] != car :
                            return False
                return True
