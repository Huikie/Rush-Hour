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
        if self.cars.cars[car][0][0]== self.cars.cars[car][1][0]:
            # horzontaal
            for i in range(0, moves + 1):
                for cordinate in self.cars.cars[car]:
                    if not self.board[cordinate[0]][cordinate[1] + i] == ".":
                        print ("invalid move")
                        return False
            #self.board[cordinate]


            return True
        else:
            for i in range(0, moves + 1):
                for cordinate in self.cars.cars[car]:
                    if not self.board[cordinate[0] + i][cordinate[1]] == ".":
                        print ("invalid move")
                        return False
            return True
            #self.board[cordinate]
            # verticaal
