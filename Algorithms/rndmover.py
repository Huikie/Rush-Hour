from Classes.board import Board
import random
from random import shuffle
import copy as copy
import time

class RandomAlgorithm:
    def __init__(self):
        self.board = Board()
        self.boards = []
        self.cars = []

    def branchboundSolver(self, iterations):
        self.iterationCount = 0
        self.newbest = 0
        while self.iterationCount != iterations:
            new_score = self.randMover()
            print("Iteration counter: ", self.iterationCount + 1)
            if new_score != self.newbest:
                print("Better solution has been found: ", new_score)
            if self.iterationCount == 0:
                self.newbest = new_score
                self.iterationCount += 1
            elif self.newbest > new_score:
                self.newbest = new_score
                self.iterationCount += 1
            else:
                self.iterationCount += 1
        self.won_info()

    def randMover(self):
        counter = 0
        self.board_temp = copy.deepcopy(self.board)
        while counter != 1000000:
            if self.board_temp.won() == False:
                move = random.randint(-5,5)
                car_list = list(self.board_temp.cars.cars.keys())
                car_list_suffle = random.sample(car_list, 1)
                car = car_list_suffle[0]
                if self.board_temp.move(car[0], move) == True:
                    counter += 1
                    if self.iterationCount != 0 and counter == self.newbest:
                        return counter
            else:
                return counter

    def won_info(self):
        start_time = time.time()
        elapsed_time = time.time() - start_time
        print("")
        print("Best result found after", self.iterationCount," iterations: ", self.newbest)
        print("The algorithm took", round(elapsed_time, 2), "to complete", self.iterationCount, "iterations!\n")
        return True
