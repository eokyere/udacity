# ----------
# User Instructions:
# 
# Create a function optimum_policy() that returns
# a grid which shows the optimum policy for robot
# motion. This means there should be an optimum
# direction associated with each navigable cell.
# 
# un-navigable cells must contain an empty string
# WITH a space, as shown in the previous video.
# Don't forget to mark the goal with a '*'

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
# modify code below
# ----------------------------------------

from q08 import move

def optimum_policy():
    value, policy = _optimum_policy()
    for row in value:
        print row
    return policy #make sure your function returns a grid of values as demonstrated in the previous video.

def _optimum_policy(grid=grid, goal=goal):
    value = [[99 for col in range(len(grid[0]))]
                 for row in range(len(grid))]
    
    policy = [[' ' for col in range(len(grid[0]))]
                   for row in range(len(grid))]
    
    y, x = goal
    value[y][x] = 0
    policy[y][x] = '*'
    
    updated = True
    
    while updated:
        updated = False
        for y in xrange(len(grid)):
            for x in xrange(len(grid[0])):
                if [y, x] != goal and grid[y][x] == 0:
                    for index, action in enumerate(delta):
                        pos = move(grid, [y, x], action)
                        if pos:
                            v = value[pos[0]][pos[1]] + cost_step
                            if v < value[y][x]:
                                value[y][x] = v
                                policy[y][x] = delta_name[index]
                                updated = True
    return value, policy



