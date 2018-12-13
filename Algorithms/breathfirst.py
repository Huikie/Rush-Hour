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

    def breadthFirst(self, size):
        self.start_time = time.time()

        # iterates over all the boards
        for j in self.boards:

            # selects each move
            for move in range(-(size - 1), (size - 1)):

                # makes deepcopy of board for move
                self.board_temp = copy.deepcopy(self.boards[self.counter])
                self.board_temp2 = copy.deepcopy(self.boards[self.counter])

                # select each car
                for car in self.keys():

                    # checks if move is possible
                    if self.board_temp.move(car, move) == True:
                        self.counter_moves =+ 1

                        # checks if board is already in archive
                        if str([self.board_temp.board]) not in self.archive:

                            # saves board
                            self.boards.append(copy.deepcopy(self.board_temp))
                            self.boards[len(self.boards)-1].parent = self.counter
                            self.archive[str([self.board_temp.board])] = self.board_temp2

                            # checks if won
                            if self.board_temp.won(size) == True:
                                self.won_info()
                                return True

                        # moves car back
                        self.board_temp.move(car, -move)
            self.counter += 1

    def won_info(self):

        # selects parent and prints it
        parent = len(self.boards) - 1
        print(self.boards[parent])
        counter = 0

        # prints parent board until the first board is reached
        while parent != 0:
            counter += 1
            parent = self.boards[parent].parent
            print(self.boards[parent])
        elapsed_time = time.time() - self.start_time

        # prints extra info
        print("\nPlease read the solution from bottom to top!")
        print("\nThe algorithm took", round(elapsed_time, 2), "seconds to solve the board!")
        print("Minimum amount of moves required to win the game:", counter)
