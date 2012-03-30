# ----------
# User Instructions:
# 
# Define a function, search() that takes no input
# and returns a list
# in the form of [optimal path length, x, y]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1] # Make sure that the goal definition stays in the function.

delta = [[-1, 0 ], # go up
        [ 0, -1], # go left
        [ 1, 0 ], # go down
        [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

cost = 1

def move(pos, dt):
    t = [pos[0] + dt[0], pos[1] + dt[1]]
    valid = t[0] >= 0 and t[0] <= len(grid) - 1 and \
            t[1] >= 0 and t[1] <= len(grid[0]) - 1
    return t if valid and grid[t[0]][t[1]] == 0 else None

def search():
    # ----------------------------------------
    # insert code here and make sure it returns the appropriate result
    # ----------------------------------------
    open_nodes = [[0] + init]
    checked_nodes = []
    while open_nodes:
        open_nodes.sort(key=lambda x: x[0])
        g, y, x = open_nodes[0]

        print [g, y, x]
        
        if [y, x] ==  goal:
            return [g, y, x]
        
        open_nodes = open_nodes[1:]
        checked_nodes.append([y, x])

        for d in delta:
            t = move([y, x], d)
            if t and t not in checked_nodes:
                open_nodes.append([g + 1] + t)
    return 'fail'
            
            


