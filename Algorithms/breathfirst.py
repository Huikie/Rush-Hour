from Classes.board import Board
class Breathfirst:
    def __init__(self):
        self.breathfirst = []
        self.board = Board()
    def move(self, moves):
        for move in range(1, moves + 1):
            for car in self.board.cars.cars.key():
                board.move(car, move)
                print(self.board.cars.cars)
                print(self.board.board)
        return True
