from Classes.board import Board
class Breathfirst:
    def __init__(self):
        self.breathfirst = []
        self.board = Board()
        self.boards = {}
        self.counter = 0
    def move(self):
        for move in range(-1, -5, -1):
            print (move)
            for car in self.board.cars.cars.keys():
                if self.board.move(car, move) == True:
                    print(self.board.cars.cars)
                    print(self.board.board)
        for move in range(1, 5):
            print (move)
            for car in self.board.cars.cars.keys():
                if self.board.move(car, move) == True:
                    print(self.board.cars.cars)
                    print(self.board.board)
        return True

    # def breathfirstSolver():
    #     moveCount = 0
    #     while not gameWon():
            #If zz can be moved to >, move the car to > and gameWon()
                #return gameWon()
            #else:
                #Do a random move and check again


    # def gameWon():
    #     if ....
            # If car zz reaches >, end breathfirst and game won
            #return True
        # else
            #return false
