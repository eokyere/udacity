# ----------
# User Instructions:
# 
# Create a function compute_value() which returns
# a grid of values. Value is defined as the minimum
# number of moves required to get from a cell to the
# goal. 
#
# If it is impossible to reach the goal from a cell
# you should assign that cell a value of 99.

# ----------

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

cost_step = 1 # the cost associated with moving from a cell to an adjacent one.

# ----------------------------------------
# insert code below
# ----------------------------------------

from q08 import move

def compute_value():
    value = _compute_value()
    for row in value:
        print row
    return value #make sure your function returns a grid of values as demonstrated in the previous video.

def _compute_value(grid=grid, goal=goal):
    value = [[99 for col in range(len(grid[0]))]
             for row in range(len(grid))]
    
    value[goal[0]][goal[1]] = 0
    
    updated = True
    while updated:
        updated = False
        for y in xrange(len(grid)):
            for x in xrange(len(grid[0])):
                if [y, x] != goal and grid[y][x] == 0:
                    for action in delta:
                        pos = move(grid, [y, x], action)
                        if pos:
                            v = value[pos[0]][pos[1]] + cost_step
                            if v < value[y][x]:
                                value[y][x] = v
                                updated = True
    return value

compute_value()