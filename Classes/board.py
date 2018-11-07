class Board:
""""
This is the class Board
""""

starting_grid = [
[' ', ' ', 'P', 'b', 'b', 'G'],
[' ', ' ', 'P', ' ', ' ', 'G'],
[' ', ' ', 'P', 'r', 'r', 'G', '>'],
[' ', ' ', ' ', 'O', 'o', 'o'],
['d', 'c', 'c', 'O', ' ', ' '],
['d', ' ', ' ', 'O', 't', 't']
]

car_list = ['P', 'b', 'G', 't', 'O', 'd', 'c', 'r']

for car in car_list:
    print(car, [(i, x.index(car)) for i, x in enumerate(starting_grid) if car in x])
