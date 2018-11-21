from Classes.board import Board
import copy as copy
class Breathfirst:
    def __init__(self):
        self.breathfirst = []
        self.board = Board()
        self.boards = []
        self.cars = []
        self.counter = 0
    def move(self):
        self.temp_board = copy.deepcopy(self.boards[0])
        for move in range(-1, -5, -1):
            print (move)
            for car in self.board.cars.cars.keys():
                if self.temp_board.move(car, move) != False:
                    self.counter += 1
                    self.boards.append(self.board)
                    for i in self.boards:
                        print(i.board)
        for move in range(1, 5):
            print (move)
            for car in self.board.cars.cars.keys():
                if self.temp_board.move(car, move) != False:
                    self.counter += 1
                    self.boards.append(self.board)
                    for i in self.boards:
                        print(self.boards[1].board)

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
