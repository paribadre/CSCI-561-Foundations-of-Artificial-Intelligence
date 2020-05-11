import sys
import copy

def get_max(my_list):
    m = None
    for item in my_list:
        if isinstance(item, list):
            item = get_max(item)
        if not m or m < item:
            m = item
    return m

def index_2d(myList, v):
    for i, x in enumerate(myList):
        if v in x:
            return (i, x.index(v))

def place(ind, grid):
    x, y = ind
    i = 0
    j = 0
    size = len(grid)
    while i >= 0 and j >= 0 and i < size and j < size:
        grid[x][j] = -999
        grid[i][y] = -999
        i += 1
        j += 1
    i = x
    j = y
    while i < size and j < size:
        grid[i][j] = -999
        i += 1
        j += 1
    i = x
    j = y
    while i >= 0 and j >= 0:
        grid[i][j] = -999
        i -= 1
        j -= 1
    i = x
    j = y
    while i < size and j >= 0:
        grid[i][j] = -999
        i += 1
        j -= 1
    i = x
    j = y
    while i >= 0 and j< size:
        grid[i][j] = -999
        i -= 1
        j += 1
    return
def restart(grid, value):
    grid = value
    max = get_max(grid)
    index = index_2d(grid, max)
    x, y = index
    grid[x][y] = -999
    return grid


f = open("input.txt")
o = open("output.txt", "w")
g = int(f.readline())
p = int(f.readline())
s = int(f.readline())
grid = [[0 for x in range(g)] for y in range(g)]
print(grid)
value = grid
for line in f:
    y = line.rstrip().split(",")
    i = int(y[0])
    j = int(y[1])
    grid[i][j] += 1
print(grid)
opt = 0
for x in range(p):
    max = get_max(grid)
    print(max)
    if(max == -999):
        grid = restart(grid,value)
    opt += max
    index = index_2d(grid, max)
    print(index)
    place(index, grid)
    print(grid)

print(opt)
o.write(str(opt))
o.close
f.close()