# -----------
# User Instructions:
# 
# Modify the function search() so that it returns
# a table of values called expand. This table
# will keep track of which step each node was
# expanded.
#
# For grading purposes, please leave the return
# statement at the bottom.
# ----------


grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0]]

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

def search(grid=grid, init=init, goal=goal):
    goal, expand = _search(grid=grid)
    return expand #Leave this line for grading purposes!


def _search(grid=grid, init=init, goal=goal):
    open_nodes = [[0] + init]
    checked_nodes = []
    expansion = [[-1 for col in range(len(grid[0]))] 
                 for row in range(len(grid))]
    expansion_index = 0
    while open_nodes:
        # sort by g-value
        open_nodes.sort(key=lambda x: x[0], reverse=True)
        
        # expand
        g, y, x = open_nodes.pop()
        checked_nodes.append([y, x])
        expansion[y][x] = expansion_index
        expansion_index += 1

        if [y, x] ==  goal:
            return [g, y, x], expansion

        for d in delta:
            t = move(grid, [y, x], d)
            if t and t not in checked_nodes:
                new_node = [g + 1] + t
                # use a set for here?
                if new_node not in open_nodes:
                    open_nodes.append(new_node)
    return 'fail', expansion

for row in search():
    print row
