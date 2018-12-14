from Classes.board import Board
import copy as copy
import time
import queue

class Breadthfirst:
    def __init__(self):
        self.breathfirst = []
        self.board = Board()
        self.boards = []
        self.cars = []
        self.counter = 0
        self.counter_move = 0
        self.archive = {}
        self.queue = queue.Queue()

    def breadthFirst(self, size):
        self.start_time = time.time()
        self.first_board = copy.deepcopy(self.board.board)
        self.queue.put(self.board)
        #print("test")
        # iterates over all the boards
        while not self.queue.empty():
            board = self.queue.get()
            # selects each move
            for move in range(-(size - 1), (size - 1)):
                #print("test2")

                # makes deepcopy of board for move
                self.board_temp = copy.deepcopy(board)
                self.board_temp2 = copy.deepcopy(board)

                # select each car
                for car in self.board.cars.keys():

                    # checks if move is possible
                    if self.board_temp.move(car, move) == True:
                        self.counter_moves =+ 1

                        # checks if board is already in archive
                        if str([self.board_temp.board]) not in self.archive:

                            # saves board
                            self.queue.put(copy.deepcopy(self.board_temp))
                            self.archive[str([self.board_temp.board])] = str([self.board_temp2.board])

                            # checks if won
                            if self.board_temp.won(size) == True:
                                self.won_info()
                                return True

                        # moves car back
                        self.board_temp.move(car, -move)
            self.counter += 1

    def won_info(self):
        counter = 0
        print(type(str([self.board_temp.board])))
        counter += 1
        self.makeup(self.archive[str([self.board_temp.board])])
        # selects parent and prints it
        counter += 1
        parent = self.archive[str([self.board_temp.board])]
        self.makeup(self.archive[parent])

        # prints parent board until the first board is reached
        while self.archive[parent] != str([self.first_board]):
            counter += 1
            parent = self.archive[parent]
            self.makeup(self.archive[parent])
        elapsed_time = time.time() - self.start_time

        # prints extra info
        print("\nPlease read the solution from bottom to top!")
        print("\nThe algorithm took", round(elapsed_time, 2), "seconds to solve the board!")
        print("Minimum amount of moves required to win the game:", counter)

    def makeup(self, board):
        board = board.replace("[","")
        board = board.replace(",","")
        board = board.replace("'","")
        board = board.replace("]","\n")
        board = " " + board

        print(board)
