from z3 import *

puzzle2 = [
    [2, 6, 0, 0, 1, 0, 0, 5, 0],
    [8, 0, 0, 0, 6, 0, 4, 0, 0],
    [0, 0, 0, 0, 2, 0, 3, 0, 0],
    [5, 0, 0, 0, 0, 9, 7, 0, 0],
    [0, 0, 7, 0, 0, 8, 0, 3, 0],
    [0, 3, 2, 0, 0, 0, 0, 0, 0],
    [7, 0, 0, 0, 8, 0, 0, 0, 1],
    [6, 0, 0, 0, 0, 4, 5, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

puzzle_easy = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
		[5, 2, 0, 0, 0, 0, 0, 0, 0],
		[0, 8, 7, 0, 0, 0, 0, 3, 1],
		[0, 0, 3, 0, 1, 0, 0, 8, 0],
		[9, 0, 0, 8, 6, 3, 0, 0, 5],
		[0, 5, 0, 0, 9, 0, 6, 0, 0],
		[1, 3, 0, 0, 0, 0, 2, 5, 0],
		[0, 0, 0, 0, 0, 0, 0, 7, 4],
		[0, 0, 5, 2, 0, 6, 3, 0, 0]]

puzzle = [ #grid evil
    [0, 0, 8, 0, 0, 5, 0, 0, 3],
    [0, 6, 0, 0, 8, 0, 0, 2, 0],
    [2, 0, 0, 9, 0, 0, 1, 0, 0],
    [3, 0, 0, 8, 0, 0, 7, 0, 0],
    [0, 5, 0, 0, 1, 0, 0, 3, 0],
    [0, 0, 7, 0, 0, 4, 0, 0, 2],
    [0, 0, 4, 0, 0, 7, 0, 0, 6],
    [0, 1, 0, 0, 6, 0, 0, 4, 0],
    [6, 0, 0, 3, 0, 0, 5, 0, 0]
]

puzzle = [ #grid evil
    [0, 0, 8, 0, 0, 5, 0, 0, 3],
    [0, 6, 0, 0, 8, 0, 0, 2, 0],
    [2, 0, 0, 9, 0, 0, 1, 0, 0],
    [3, 0, 0, 8, 0, 0, 7, 0, 0],
    [0, 5, 0, 0, 1, 0, 0, 3, 0],
    [0, 0, 7, 0, 0, 4, 0, 0, 2],
    [0, 0, 4, 0, 0, 7, 0, 0, 6],
    [0, 1, 0, 0, 6, 0, 0, 4, 0],
    [6, 0, 0, 3, 0, 0, 5, 0, 0]
]

def print_grid(grid, model=None):
    for r in range(9):
        if r % 3 == 0 and r != 0:
            print('-'*21)
        row = ''
        for c in range(9):
            if c % 3 == 0 and c != 0:
                row += '| '
            value = model.evaluate(grid[r][c]) if model else grid[r][c]
            row += f'{value} '
        print(row)

def add_puzzle_constraints(solver, grid, puzzle):
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] != 0:
                solver.add(grid[r][c] == puzzle[r][c])


#create a solver instance
s = Solver()
grid = [
    [ Int(f'cell-{i}-{j}') for j in range(9) ]
    for i in range(9)
]

#each cell contains a value in {1, ..., 9}
for r in range(9):
    for c in range(9):
        cell = grid[r][c]
        s.add(1 <= cell, cell <= 9)

#each row contains a digit at most once
for r in range(9):
    s.add(Distinct(grid[r]))

#each column contains a digit at most once
for c in range(9):
    s.add(Distinct([grid[r][c] for r in range(9)]))

#each 3x3 square contains a digit at most once
for r in range(0, 9, 3):
    for c in range(0, 9, 3):
        s.add(Distinct([
            grid[r + i][c + j]
            for i in range(3) for j in range(3)
        ]))



add_puzzle_constraints(s, grid, puzzle)



if s.check() == sat:
    m = s.model()
    print_grid(grid, m)
else:
    print("The puzzle cannot be solved.")
