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


    def breathfirstSolver():
        moveCount = 0
        while not gameWon():
            #If zz can be moved to >, move the car to > and gameWon()
                #return gameWon()
            #else:
                #Do a random move and check again


    def gameWon():
        if ....
            # If car zz reaches >, end breathfirst and game won
            #return True
        else
            #return false
