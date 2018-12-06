from Classes.board import Board
import copy as copy
class Breathfirst:
    def __init__(self):
        self.breathfirst = []
        self.board = Board()
        self.boards = []
        self.cars = []
        self.counter = 0
        self.archive = {}
    def move(self):
        for j in self.boards:
            #print(j.board)
            for move in range(-5, 5):
                self.board_temp = copy.deepcopy(self.boards[self.counter])
                if self.board_temp.move("z", move) == True:
                    if str([self.board_temp.board]) not in self.archive:
                        self.boards.append(copy.deepcopy(self.board_temp))
                        self.boards[len(self.boards)-1].parent = self.counter
                        self.archive[str([self.board_temp.board])]=True
                        if self.board_temp.won() == True:
                            return True
                    self.board_temp.move("z", -move)                        
                for car in self.board.cars.cars.keys():
                    if self.board_temp.move(car, move) == True:
                        if str([self.board_temp.board]) not in self.archive:
                            self.boards.append(copy.deepcopy(self.board_temp))
                            self.boards[len(self.boards)-1].parent = self.counter
                            self.archive[str([self.board_temp.board])]=True
                            #print(self.board_temp.board)
                            if self.board_temp.won() == True:
                                return True
                        self.board_temp.move(car, -move)
                     #print(self.boards[self.counter].board)
                        #print(self.boards[self.counter].board)
            #for i in self.boards:
                #print(i.board)
            # for board in self.boards:
            #     print(board.board)

            self.counter += 1
            #print(self.boards[self.counter].board)
            #print(self.counter)
            #if self.board_temp.won() == True:
            #    print(len(self.boards))
            #    return True
            # if 1000 % self.counter == 0:
            #     print(self.counter)
            #if self.counter == 1000000:
            #    return True


    # def breathfirstSolver():
    #     moveCount = 0
    #     while not gameWon():
            #If zz can be moved to >, move the car to > and gameWon()
                #return gameWon()
            #else:
                #Do a random move and check again


    # def gameWon():
    #     if ....
            # If car zz reaches >, end breathfirst and game won
            #return True
        # else
            #return false
