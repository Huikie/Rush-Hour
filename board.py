from cars import Cars
class Board:
#"""
#This is the class Board
#"""
    def __init__(self):
        self.board = [
['#', '#', '#', '#', '#', '#', '#', '#'],
['#', '-', '-', '-', '-', '-', '-', '#'],
['#', '-', '-', '-', '-', '-', '-', '#'],
['#', '-', '-', '-', '-', '-', '-', '>'],
['#', '-', '-', '-', '-', '-', '-', '#'],
['#', '-', '-', '-', '-', '-', '-', '#'],
['#', '-', '-', '-', '-', '-', '-', '#'],
['#', '#', '#', '#', '#', '#', '#', '#']
]

#car_list = ['P', 'b', 'G', 't', 'O', 'd', 'c', 'r']

#for car in car_list:
    #print(car, [(i, x.index(car)) for i, x in enumerate(starting_grid) if car in x])
