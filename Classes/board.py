import copy as copy
class Board:
    def __init__(self):
        self.board = []
        self.cars = {}
        self.board_temp = []
        self.parent = 0

    def __repr__(self):
        """Function that turns the board representation into a string."""
        return '\n' + '\n'.join(' '.join(field) for field in self.board)

    def select_board(self, size):
        """Function that selects an appropriate board representation based on size."""
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
        """Function that loads a file (file parameter) with a Rush Hour board into a board, if
           the measures of the board in the file are a supported size (num parameter)."""

        # Select a board based on the length of the board in the file
        self.select_board(num)
        board_text = file
        # Row coordinate of the cars
        y = 0
        dict = {}
        print(board_text)
        for row in board_text:
            # Column coordinate of the cars
            x = 0
            y += 1
            for char in row:
                x += 1
                if char.isalpha():
                    if char in dict:
                        dict[char].append([y, x])
                    else:
                        dict[char] = [[y, x]]
                if char != "\n":
                    self.board[y][x] = char
        self.add(dict)

    def won(self, size):
        """Function that checks if the red car (zz) stands on winning coordinates
           this coordinates depend on the size of the board (size parameter)."""
        if self.cars["z"][1][1]  ==  size:
            return True
        else:
            return False

    def add(self, cars_dict):
        """Function that sets the cars dictionary equal to a dictionary has been created (cars_dict)"""
        self.cars = cars_dict

    def move(self, car, moves):
        """This function makes it possible to move a car (car parameter) in a
        Rush Hour board with a certain amount of moves (moves parameter)."""

        # List that holds coordinates of all cars (keys) in the board as a value in the cars dictionary
        car_coordinates = []
        # Move cars are positioned horizontally
        if self.cars[car][0][0] == self.cars[car][1][0]:
            # Move car to the right
            if moves > 0:
                # Check if move is valid
                for move in range(1, moves + 1):
                    for coordinate in self.cars[car]:
                        if self.board[coordinate[0]][coordinate[1] + move] != "." and self.board[coordinate[0]][coordinate[1] + move] != car :
                            # Move is invalid
                            return False
                # Move is valid, so move the car, update the board and change the coordinates of the moved car
                for coordinate in self.cars[car]:
                    self.board[coordinate[0]][coordinate[1]] = "."
                for coordinate in self.cars[car]:
                    self.board[coordinate[0]][coordinate[1] + moves] = car
                for coordinate in self.cars[car]:
                    car_coordinates.append([coordinate[0], coordinate[1] + moves])
                    self.cars[car] = car_coordinates
                return True

            # Move car to the left
            elif moves < 0:
                # Check if move is valid
                for move in range(-1, moves -1, -1):
                    for coordinate in self.cars[car]:
                        if self.board[coordinate[0]][coordinate[1] + move] != "." and self.board[coordinate[0]][coordinate[1] + move] != car :
                            # Move is invalid
                            return False
                # Move is valid, so move the car, update the board and change the coordinates of the moved car
                for coordinate in self.cars[car]:
                    self.board[coordinate[0]][coordinate[1]] = "."
                for coordinate in self.cars[car]:
                    self.board[coordinate[0]][coordinate[1] + moves] = car
                for coordinate in self.cars[car]:
                    car_coordinates.append([coordinate[0], coordinate[1] + moves])
                    self.cars[car] = car_coordinates
                return True

        # Move cars that are positioned vertically
        else:
            # Move car down
            if moves > 0:
                # Check if move is valid
                for move in range(1, moves + 1):
                    for coordinate in self.cars[car]:
                        if self.board[coordinate[0] + move][coordinate[1]] != "." and self.board[coordinate[0] + move][coordinate[1]] != car :
                            # Move is invalid
                            return False
                # Move is valid, so move the car, update the board and change the coordinates of the moved car
                for coordinate in self.cars[car]:
                    self.board[coordinate[0]][coordinate[1]] = "."
                for coordinate in self.cars[car]:
                    self.board[coordinate[0]+ moves][coordinate[1]] = car
                for coordinate in self.cars[car]:
                    car_coordinates.append([coordinate[0] + moves, coordinate[1]])
                    self.cars[car] = car_coordinates
                return True

            # Move cars up
            elif moves < 0:
                # Check if move is valid
                for move in range(-1, moves -1, -1):
                    for coordinate in self.cars[car]:
                        if self.board[coordinate[0] + move][coordinate[1]] != "." and self.board[coordinate[0] + move][coordinate[1]] != car :
                            # Move is invalid
                            return False
                # Move is valid, so move the car, update the board and change the coordinates of the moved car
                for coordinate in self.cars[car]:
                    self.board[coordinate[0]][coordinate[1]] = "."
                for coordinate in self.cars[car]:
                    self.board[coordinate[0]+ moves][coordinate[1]] = car
                for coordinate in self.cars[car]:
                    car_coordinates.append([coordinate[0] + moves, coordinate[1]])
                    self.cars[car] = car_coordinates
                return True
