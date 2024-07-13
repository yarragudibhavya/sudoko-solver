import numpy as np
# to take input(sudoko grid)
def input_grid():
    grid = []
    print("Enter the Sudoku grid row by row (use 0 for empty cells):")
    for _ in range(9):
        while True:
            row = input().strip()
            try:
                row = list(map(int, row.split()))
                if len(row) != 9:
                    raise ValueError("Each row must have 9 numbers.")
                grid.append(row)
                break
            except ValueError as e:
                print(f"Invalid input: {e}. Please re-enter the row.")
    return grid

def possible(grid,row,column,number):
    #checking whether number is already appeared in row or not
    for i in range(0,9):
        if grid[row][i]==number:
            return False
        
    #checking whether number is already appeared in column or not
    for i in range(0,9):
         if grid[i][column]==number:
            return False
    #checking whether number is already appeared in grid or not
    x=row//3*3#section are 0,3,6
    y=column//3 *3
    for i in range(0,3):
        for j in range(0,3):
            if grid[x+i][y+j]==number:
                return False
    return True
def solve(grid):
    for i in range(0,9):
        for j in range(0,9):
            if grid[i][j]==0:
                for num in range(1,10):
                    if possible(grid,i,j,num):
                        grid[i][j]=num
                        if solve(grid):
                            return True
                        grid[i][j]=0
                return False
                    
    print(np.matrix(grid))
    input('More possible solutions')
    return True
grid=input_grid()
if not solve(grid):
    print("no possible solution")
    
    
