from Classes.cars import Cars
class Board:
    def __init__(self):
        self.board = [
['#', '#', '#', '#', '#', '#', '#', '#'],
['#', '-', '-', '-', '-', '-', '-', '#'],
['#', '-', '-', '-', '-', '-', '-', '#'],
['#', '-', '-', '-', '-', '-', '-', '>'],
['#', '-', '-', '-', '-', '-', '-', '#'],
['#', '-', '-', '-', '-', '-', '-', '#'],
['#', '-', '-', '-', '-', '-', '-', '#'],
['#', '#', '#', '#', '#', '#', '#', '#']
]
        self.cars = Cars()
    def move(self, car, moves):
        lijst = []
        # Move cars that are positioned horizontally
        if self.cars.cars[car][0][0]== self.cars.cars[car][1][0]:
            # moves cars to the right
            if moves > 0:
                # checks if move is valid
                for i in range(1, moves + 1):
                    for cordinate in self.cars.cars[car]:
                        validMoveHorizontal(self, car, moves, i, lijst, cordinate)
                # moves car to the left
            elif moves < 0:
                # checks if move is valid
                for i in range(-1, moves -1, -1):
                    for cordinate in self.cars.cars[car]:
                        validMoveHorizontal(self, car, moves, i, lijst, cordinate)
        # Move cars that are positioned vertically
        else:
            # moves cars down
            if moves > 0:
                # checks if move is valid
                for i in range(1, moves + 1):
                    for cordinate in self.cars.cars[car]:
                        validMoveVertical(self, car, moves, i, lijst, cordinate)
                #self.cars.cars[car] = lijst
                #print(self.cars.cars[car])
            # moves cars up
            elif moves < 0:
                # checks if move is valid
                for i in range(-1, moves -1, -1):
                    for cordinate in self.cars.cars[car]:
                        validMoveVertical(self, car, moves, i, lijst, cordinate)

#Function that checks if a horizontal move is valid
def validMoveHorizontal(self, car, moves, i, lijst, cordinate):
        if self.board[cordinate[0]][cordinate[1] + i] != "." and self.board[cordinate[0]][cordinate[1] + i] != car :
            print ("invalid move")
            return False
        for cordinate in self.cars.cars[car]:
            self.board[cordinate[0]][cordinate[1]] = "."
        for cordinate in self.cars.cars[car]:
            self.board[cordinate[0]][cordinate[1]+ moves] = car
        for cordinate in self.cars.cars[car]:
            lijst.append([cordinate[0], cordinate[1] + moves])
            self.cars.cars[car] = lijst
        return True


#Function that checks if a vertical move is valid
def validMoveVertical(self, car, moves, i, lijst, cordinate):
    if self.board[cordinate[0] + i][cordinate[1]] != "." and self.board[cordinate[0] + i][cordinate[1]] != car :
        print ("invalid move")
        return False
    for cordinate in self.cars.cars[car]:
        self.board[cordinate[0]][cordinate[1]] = "."
    for cordinate in self.cars.cars[car]:
        self.board[cordinate[0]+ moves][cordinate[1]] = car
    for cordinate in self.cars.cars[car]:
        lijst.append([cordinate[0] + moves, cordinate[1]])
        self.cars.cars[car] = lijst
    return True
