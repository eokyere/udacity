# ----------
# User Instructions:
# 
# Implement the function optimum_policy2D() below.
#
# You are given a car in a grid with initial state
# init = [x-position, y-position, orientation]
# where x/y-position is its position in a given
# grid and orientation is 0-3 corresponding to 'up',
# 'left', 'down' or 'right'.
#
# Your task is to compute and return the car's optimal
# path to the position specified in `goal'; where
# the costs for each motion are as defined in `cost'.

# EXAMPLE INPUT:

# grid format:
#     0 = navigable space
#     1 = occupied space 
grid = [[1, 1, 1, 0, 0, 0],
        [1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1]]
goal = [2, 0] # final position
init = [4, 3, 0] # first 2 elements are coordinates, third is direction
cost = [2, 1, 20] # the cost field has 3 values: right turn, no turn, left turn

# EXAMPLE OUTPUT:
# calling optimum_policy2D() should return the array
# 
# [[' ', ' ', ' ', 'R', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', '#'],
#  ['*', '#', '#', '#', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', ' '],
#  [' ', ' ', ' ', '#', ' ', ' ']]
#
# ----------


# there are four motion directions: up/left/down/right
# increasing the index in this array corresponds to
# a left turn. Decreasing is is a right turn.

forward = [[-1,  0], # go up
           [ 0, -1], # go left
           [ 1,  0], # go down
           [ 0,  1]] # do right
forward_name = ['up', 'left', 'down', 'right']

# the cost field has 3 values: right turn, no turn, left turn
action = [-1, 0, 1]
action_name = ['R', '#', 'L']


# ----------------------------------------
# modify code below
# ----------------------------------------

def optimum_policy2D():

    return policy2D # Make sure your function returns the expected grid.

def _optimum_policy2d(grid=grid, init=init, goal=goal, cost=cost):
    value, policy = _optimum_policy(grid, goal, cost)

    y, x, orientation = init
    p = [[' ' for col in range(len(grid[0]))]
              for row in range(len(grid))]
    p[y][x] = policy[orientation][y][x]
    
    while policy[orientation][y][x] != '*':
        if policy[orientation][y][x] == '#':
            dir = orientation
        elif policy[orientation][y][x] == 'R':
            dir = (orientation - 1) % 4
        elif policy[orientation][y][x] == 'L':
            dir = (orientation + 1) % 4
        y += forward[dir][0]
        x += forward[dir][1]
        orientation = dir
        p[y][x] = policy[orientation][y][x]
    return p

def _optimum_policy(grid=grid, goal=goal, cost=cost):
    value = [[[999 for col in range(len(grid[0]))]
                   for row in range(len(grid))]
                   for dir in range(len(forward))]

    policy = [[[' ' for col in range(len(grid[0]))]
                    for row in range(len(grid))]
                    for dir in range(len(forward))]

    y, x = goal
    
    for orientation in range(4):
        value[orientation][y][x] = 0
        policy[orientation][y][x] = '*'
    
    updated = True
    
    while updated:
        updated = False
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                for orientation in range(len(forward)):
                    if [y, x] != goal and grid[y][x] == 0:
                        
                        for i in range(3):
                            dir = (orientation + action[i]) % 4
                            pos = move(grid, [y, x], forward[dir])
                            
#                        for index, action in enumerate(delta):
#                            pos = move(grid, [y, x], action)
                            if pos:
                                v = value[dir][pos[0]][pos[1]] + cost[i]
                                if v < value[orientation][y][x]:
                                    value[orientation][y][x] = v
                                    policy[orientation][y][x] = action_name[i]
                                    updated = True
    return value, policy


def move(grid, pos, dt):
    y, x = pos
    y, x = [y + dt[0], x + dt[1]]
    valid = y >= 0 and y <= len(grid) - 1 and \
            x >= 0 and x <= len(grid[0]) - 1
    return [y, x] if valid and grid[y][x] == 0 else None

