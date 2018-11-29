from Classes.board import Board
import copy as copy
class Breathfirst:
    def __init__(self):
        self.breathfirst = []
        self.board = Board()
        self.boards = []
        self.cars = []
        self.counter = 0
        self.archive =[]


    def move(self):
        counter = 0
        for j in self.boards:
            #print(j.board)
            for move in range(-1, -5, -1):
                self.board_temp = copy.deepcopy(self.boards[counter])
                for car in self.board.cars.cars.keys():
                    if self.board_temp.move(car, move) != False:
                        if self.board_temp.board not in self.archive:
                            self.board_temp.parent = counter
                            self.boards.append(copy.deepcopy(self.board_temp))
                            self.archive.append(copy.deepcopy(self.board_temp.board))
                            print(len(self.boards))
                            print(self.board_temp.parent)
                            print(self.board_temp.board)
                            if self.board_temp.won() == True:
                                return True
                    self.board_temp.move(car, -move)

            for move in range(1, 5):
                self.board_temp = copy.deepcopy(self.boards[counter])
                for car in self.board.cars.cars.keys():
                    if self.board_temp.move(car, move) != False:
                        if self.board_temp.board not in self.archive:
                            self.board_temp.parent = counter
                            self.boards.append(copy.deepcopy(self.board_temp))
                            self.archive.append(copy.deepcopy(self.board_temp.board))
                            print(len(self.boards))
                            print(self.board_temp.parent)
                            print(self.board_temp.board)
                            if self.board_temp.won() == True:
                                return True
                    self.board_temp.move(car, -move)

            counter = counter + 1
            if counter == 1000000:
                return True
