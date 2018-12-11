from Classes.board import Board
import copy as copy
import time
class Breathfirst:
    def __init__(self):
        self.breathfirst = []
        self.board = Board()
        self.boards = []
        self.cars = []
        self.counter = 0
        self.counter_move = 0
        self.archive = {}
    def move(self):
        for j in self.boards:
            for move in range(-5, 5):
                self.board_temp = copy.deepcopy(self.boards[self.counter])
                self.board_temp2 = copy.deepcopy(self.boards[self.counter])
                for car in self.board.cars.cars.keys():
                    if self.board_temp.move(car, move) == True:
                        self.counter_moves =+ 1
                        if str([self.board_temp.board]) not in self.archive:
                            self.boards.append(copy.deepcopy(self.board_temp))
                            self.boards[len(self.boards)-1].parent = self.counter
                            self.archive[str([self.board_temp.board])] = self.board_temp2
                            if self.board_temp.won() == True:
                                self.won_info()
                                return True
                        self.board_temp.move(car, -move)
            self.counter += 1

    def won_info(self):
        start_time = time.time()
        parent = len(self.boards) - 1
        print(self.boards[parent])
        counter = 0
        while parent != 0:
            counter += 1
            parent = self.boards[parent].parent
            print(self.boards[parent])
            elapsed_time = time.time() - start_time
        print("\nPlease read the solution from bottom to top!")
        print("\nThe algorithm took", round(elapsed_time, 2), "seconds to solve the board!")
        print("Minimum amount of moves required to win the game:", counter)
