from Classes.board import Board
import random
from random import shuffle

class RandomAlgorithm:
    def __init__(self):
        self.board = Board()
        self.boards = []
        self.cars = []

    def randMover(self):
        counter = 0
        while counter != 1000000:
            if self.board.won() == False:
                move = random.randint(-5,5)
                car_list = list(self.board.cars.cars.keys())
                print(car_list)
                car = random.shuffle(car_list[0])

                print(car)
                print(move)
                #if self.board.move(car[0], move) == True:
                #    print(self.board)
                #    counter += 1
            else:
                return True
                #if self.board.move(car, move) != False:
