from Code.Classes.board import Board
import copy as copy
import time
import queue

class Breadthfirst:
    def __init__(self):
        self.breathfirst = []
        self.board = Board()
        self.boards = []
        self.archive = {}
        self.queue = queue.Queue()
        """Function that runs the breadthfirst algorithm and stops if it has found
        the best solution.
        """

    def breadthFirst(self, size):
        self.start_time = time.time()
        self.first_board = copy.deepcopy(self.board.board)
        self.queue.put(self.board)

        # Iterates over all the boards.
        while not self.queue.empty():
            board = self.queue.get()

            # Selects each move.
            for move in range(-(size - 1), (size - 1)):

                # Makes deepcopy of board for move.
                self.board_temp = copy.deepcopy(board)
                self.board_temp2 = copy.deepcopy(board)

                # select each car.
                for car in self.board.cars.keys():

                    # Checks if move is possible.
                    if self.board_temp.move(car, move) == True:

                        # Checks if board is already in archive.
                        if str([self.board_temp.board]) not in self.archive:

                            # Saves board.
                            self.queue.put(copy.deepcopy(self.board_temp))
                            self.archive[str([self.board_temp.board])] = str([self.board_temp2.board])

                            # Checks if won.
                            if self.board_temp.won(size) == True:
                                self.won_info()
                                return True

                        # Moves car back.
                        self.board_temp.move(car, -move)

    def won_info(self):
        """Function that displays information about the results of the breadthfirst algorithm.
        """
        counter = 2

        # Prints winning board.
        self.makeup(str([self.board_temp.board]))

        # Selects parent and prints it.
        self.makeup(self.archive[str([self.board_temp.board])])

        # Selects parent of parent and prints it.
        parent = self.archive[str([self.board_temp.board])]
        self.makeup(self.archive[parent])

        # Prints parent board until the first board is reached.
        while self.archive[parent] != str([self.first_board]):
            counter += 1

            # Selects parent of child and prints it.
            parent = self.archive[parent]
            self.makeup(self.archive[parent])

        # Prints extra info.
        elapsed_time = time.time() - self.start_time
        print("\nPlease read the solution from bottom to top!")
        print("\nThe algorithm took", round(elapsed_time, 2), "seconds to solve the board!")
        print("Minimum amount of moves required to win the game:", counter)

    def makeup(self, board):

        # Makes better representation of board.
        board = board.replace("[","")
        board = board.replace(",","")
        board = board.replace("'","")
        board = board.replace("]","\n")
        board = " " + board
        print(board)
