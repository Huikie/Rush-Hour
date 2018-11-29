from Classes.board import Board
import random
from random import shuffle

class RandomAlgorithm:
    def __init__(self):
        self.board = Board()
        self.boards = []
        self.cars = []

    def randMover(self):
        for move in range(-1, -5, -1):
            random.shuffle(self.board.cars.cars.keys())
            for car in self.board.cars.cars.keys():
                print(car)
                #if self.board.move(car, move) != False:
