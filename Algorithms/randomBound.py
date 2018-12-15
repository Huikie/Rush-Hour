from Classes.board import Board
import random
from random import shuffle
import copy as copy
import time

class RandomBound:
    def __init__(self):
        self.board = Board()
        self.boards = []
        self.cars = []

    def randomBound(self, iterations, size):
        """Function that runs the randomMover a certain amount of times (iterations parameter)
           and puts a bound, so that the randMover will only look for better solutions.
           Also the board size is important for the randMover, so the board size must be specified (size parameter)."""

        self.start_time = time.time()
        self.iterationCount = 0
        self.newbest = 0

        # Runs as long as the specified amount of iterations hasn't been reached.
        while self.iterationCount != iterations:
            # Find  a new solution for every iteration.
            new_score = self.randomMover(size)
            # Keep track of how many iterations has been done.
            print("Iteration counter: ", self.iterationCount + 1)
            # In the first iteration set newbest equal to the first new_score.
            if self.iterationCount == 0:
                self.newbest = new_score
                self.iterationCount += 1
                print("Initial score is set ", new_score)
            # In the other iterations set newbest equal to a new_score if that's a better score.
            elif self.newbest > new_score:
                self.newbest = new_score
                self.iterationCount += 1
                print("Better solution has been found: ", new_score)
            # No better solution has been found.
            else:
                self.iterationCount += 1
        self.won_info()

    def randomMover(self, size):
        """Function that does a random move in a range of the size (size parameter) of
           the board on a random car that is in the board."""
        moves = 0
        self.board_temp = copy.deepcopy(self.board)
        # So that the function keeps running until it reaches a winning board.
        while self.board_temp.won(size) == False:
            # Generates a random move.
            move = random.randint(-(size - 1), (size - 1))
            car_list = list(self.board_temp.cars.keys())
            # Generates a list with a random car.
            car_list_shuffle = random.sample(car_list, 1)
            # Get the random car out of the list.
            car = car_list_shuffle[0]
            # Move a car if it's an invalid move.
            if self.board_temp.move(car[0], move) == True:
                moves += 1
                # Makes the function stop iterating if the number of moves done is equal to the best solution found so far.
                if self.iterationCount != 0 and moves == self.newbest:
                    return moves
        else:
            return moves

    def won_info(self):
        """Function that displays information about the results of the randomBound solver."""
        elapsed_time = time.time() - self.start_time
        print("")
        print("Best result found after", self.iterationCount," iterations: ", self.newbest)
        print("The algorithm took", round(elapsed_time, 2), "to complete", self.iterationCount, "iterations!\n")
        return True
