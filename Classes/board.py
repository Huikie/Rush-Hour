import copy as copy
class Board:
    def __init__(self):
        self.board = []
        self.cars = {}
        self.board_temp = []
        #self.cars_temp = {}
        self.parent = 0

    #Function that turns the board representation into a string
    def __repr__(self):
        return '\n' + '\n'.join(' '.join(field) for field in self.board)

    #Select an appropriate board representation based on size
    def select_board(self, size):
        if size == 6:
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
        elif size == 9:
            self.board = [
            ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
            ['#', '-', '-', '-', '-', '-', '-', '-', '-', '-', '#'],
            ['#', '-', '-', '-', '-', '-', '-', '-', '-', '-', '#'],
            ['#', '-', '-', '-', '-', '-', '-', '-', '-', '-', '#'],
            ['#', '-', '-', '-', '-', '-', '-', '-', '-', '-', '#'],
            ['#', '-', '-', '-', '-', '-', '-', '-', '-', '-', '>'],
            ['#', '-', '-', '-', '-', '-', '-', '-', '-', '-', '#'],
            ['#', '-', '-', '-', '-', '-', '-', '-', '-', '-', '#'],
            ['#', '-', '-', '-', '-', '-', '-', '-', '-', '-', '#'],
            ['#', '-', '-', '-', '-', '-', '-', '-', '-', '-', '#'],
            ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
            ]
        elif size == 12:
            self.board = [
            ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
            ['#', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '#'],
            ['#', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '#'],
            ['#', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '#'],
            ['#', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '#'],
            ['#', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '#'],
            ['#', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '>'],
            ['#', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '#'],
            ['#', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '#'],
            ['#', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '#'],
            ['#', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '#'],
            ['#', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '#'],
            ['#', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '#'],
            ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
            ]
        else:
            print("Error inppropriate board size. Supported sizes are: 6x6, 9x9 and 12x12.")
            return False

    def load_board(self, file, num):
            self.select_board(num)
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
            self.add(dict)

    def won(self, size):
        if self.cars["z"][1][1]  ==  size:
            return True
        else:
            return False

    def add(self, car):
        self.cars = car

    def move(self, car, moves):
        lijst = []
        # Move cars that are positioned horizontally
        if self.cars[car][0][0]== self.cars[car][1][0]:
            # moves cars to the right
            if moves > 0:
                # checks if move is valid
                for i in range(1, moves + 1):
                    for cordinate in self.cars[car]:
                        if self.board[cordinate[0]][cordinate[1] + i] != "." and self.board[cordinate[0]][cordinate[1] + i] != car :
                            return False
                #print(self.board)
                for cordinate in self.cars[car]:
                    self.board[cordinate[0]][cordinate[1]] = "."
                for cordinate in self.cars[car]:
                    self.board[cordinate[0]][cordinate[1]+ moves] = car
                for cordinate in self.cars[car]:
                    lijst.append([cordinate[0], cordinate[1] + moves])
                    self.cars[car] = lijst
                return True
                # moves car to the left
            elif moves < 0:
                # checks if move is valid
                for i in range(-1, moves -1, -1):
                    for cordinate in self.cars[car]:
                        if self.board[cordinate[0]][cordinate[1] + i] != "." and self.board[cordinate[0]][cordinate[1] + i] != car :
                            return False
                for cordinate in self.cars[car]:
                    self.board[cordinate[0]][cordinate[1]] = "."
                for cordinate in self.cars[car]:
                    self.board[cordinate[0]][cordinate[1] + moves] = car
                for cordinate in self.cars[car]:
                    lijst.append([cordinate[0], cordinate[1] + moves])
                    self.cars[car] = lijst
                return True
        # Move cars that are positioned vertically
        else:
            # moves cars down
            if moves > 0:
                # checks if move is valid
                for i in range(1, moves + 1):
                    for cordinate in self.cars[car]:
                        if self.board[cordinate[0] + i][cordinate[1]] != "." and self.board[cordinate[0] + i][cordinate[1]] != car :
                            return False
                for cordinate in self.cars[car]:
                    self.board[cordinate[0]][cordinate[1]] = "."
                for cordinate in self.cars[car]:
                    self.board[cordinate[0]+ moves][cordinate[1]] = car
                for cordinate in self.cars[car]:
                    lijst.append([cordinate[0] + moves, cordinate[1]])
                    self.cars[car] = lijst
                return True
                #self.cars.cars[car] = lijst
                #print(self.cars.cars[car])
            # moves cars up
            elif moves < 0:
                # checks if move is valid
                for i in range(-1, moves -1, -1):
                    for cordinate in self.cars[car]:
                        if self.board[cordinate[0] + i][cordinate[1]] != "." and self.board[cordinate[0] + i][cordinate[1]] != car :
                            return False
                for cordinate in self.cars[car]:
                    self.board[cordinate[0]][cordinate[1]] = "."
                for cordinate in self.cars[car]:
                    self.board[cordinate[0]+ moves][cordinate[1]] = car
                for cordinate in self.cars[car]:
                    lijst.append([cordinate[0] + moves, cordinate[1]])
                    self.cars[car] = lijst
                return True
