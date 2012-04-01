# -----------
# User Instructions:
#
# Modify the the search function so that it becomes
# an A* search algorithm as defined in the previous
# lectures.
#
# Your function should return the expanded grid
# which shows, for each element, the count when
# it was expanded or -1 if the element was never expanded.
#
# Your function only needs to work for a 5x6 grid.
# You do not need to modify the heuristic.
# ----------

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]

heuristic = [[9, 8, 7, 6, 5, 4],
            [8, 7, 6, 5, 4, 3],
            [7, 6, 5, 4, 3, 2],
            [6, 5, 4, 3, 2, 1],
            [5, 4, 3, 2, 1, 0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

cost = 1

# ----------------------------------------
# modify code below
# ----------------------------------------

from q08 import move 

def search(grid=grid):
    result, expand = _search(grid=grid)
    for row in expand:
        print row

    return expand #Leave this line for grading purposes!

def _search(grid=grid, init=init, goal=goal):
    y, x = init
    g = 0
    h = heuristic[y][x]
    f = g + h
#    action = None
#    unchecked = [[f, g, h, action, y, x]]
    unchecked = [[f, g, y, x]]
    
    checked = [[0 for col in range(len(grid[0]))]
               for row in range(len(grid))]
    expansion = [[-1 for col in range(len(grid[0]))] 
                 for row in range(len(grid))]
    expansion_index = 0
    
#    actions = [[-1 for col in range(len(grid[0]))] 
#              for row in range(len(grid))]
    
    while unchecked:
        # sort by g-value
        unchecked.sort(reverse=True)
        
        for row in unchecked:
            print row
        
        # expand
#        f, g, h, action, y, x = unchecked.pop()
#        print f, g, h, action, y, x
        f, g, y, x = unchecked.pop()
        print f, g, y, x
        
        checked[y][x] = 1
#        actions[y][x] = action
        expansion[y][x] = expansion_index
        expansion_index += 1

        if [y, x] ==  goal:
            return [g, y, x], expansion

        for action, dt in enumerate(delta):
            pos = move(grid, [y, x], dt)
            if pos:
                y1, x1 = pos
                if not checked[y1][x1]:
                    g1 = g + cost
                    h = heuristic[y1][x1]
    #                node = [f, g1, h, action] + pos
                    node = [g1 + h, g1, y1, x1]
                    # use a set for this?
                    if node not in unchecked:
                        unchecked.append(node)
    return FAIL, expansion

search()
