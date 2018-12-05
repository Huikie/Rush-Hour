from Classes.board import Board
import random
from random import shuffle
import copy as copy

class RandomAlgorithm:
    def __init__(self):
        self.board = Board()
        self.boards = []
        self.cars = []

    def branchboundSolver(self):
        counter = 0
        newbest = 0
        while counter != 10:
            new_score = self.randMover()
            print(counter)
            print(newbest)
            print(new_score)
            if counter == 0:
                newbest = self.randMover()
                counter += 1
            elif newbest > new_score:
                newbest = new_score
                counter += 1
            else:
                counter += 1
        print(newbest)
        return True

    def randMover(self):
        counter = 0
        self.board_temp = copy.deepcopy(self.board)
        while counter != 1000000:
            if self.board_temp.won() == False:
                move = random.randint(-5,5)
                car_list = list(self.board_temp.cars.cars.keys())
                car_list_suffle = random.sample(car_list, len(car_list))
                car = car_list_suffle[0]
                #print (move)
                #print(car)
                if self.board_temp.move(car[0], move) == True:
                    #print(self.board)
                    counter += 1
            else:
                return counter
                #return True
                #if self.board.move(car, move) != False:
