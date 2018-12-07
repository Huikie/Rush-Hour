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
        start_time = time.time()
        self.iterationCount = 0
        self.newbest = 0
        while self.iterationCount != iterations:
            new_score = self.randMover()
            print("Iteration counter: ", self.iterationCount)
            print("Best score: ", self.newbest)
            if new_score == self.newbest:
                print("No faster solution found!")
                print("")
            else:
                print("Score of this iteration: ", new_score)
                print("")
            if self.iterationCount == 0:
                self.newbest = new_score
                self.iterationCount += 1
            elif self.newbest > new_score:
                self.newbest = new_score
                self.iterationCount += 1
            else:
                self.iterationCount += 1
        elapsed_time = time.time() - start_time
        print("Board_1")
        print("Best result found after", self.iterationCount," iterations: ", self.newbest)
        print("The algorithm took", round(elapsed_time, 2), "to complete", self.iterationCount, "iterations!\n")
        return True

    def randMover(self):
        counter = 0
        self.board_temp = copy.deepcopy(self.board)
        while counter != 1000000:
            if self.board_temp.won() == False:
                move = random.randint(-5,5)
                car_list = list(self.board_temp.cars.cars.keys())
                car_list_suffle = random.sample(car_list, 1)
                car = car_list_suffle[0]
                #print (move)
                #print(car)
                if self.board_temp.move(car[0], move) == True:
                    #print(self.board)
                    counter += 1
                    if self.iterationCount != 0 and counter == self.newbest:
                        return counter
            else:
                return counter
                #return True
                #if self.board.move(car, move) != False:
