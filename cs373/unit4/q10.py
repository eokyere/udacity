# -----------
# User Instructions:
#
# Modify the the search function so that it returns
# a shortest path as follows:
# 
# [['>', 'v', ' ', ' ', ' ', ' '],
#  [' ', '>', '>', '>', '>', 'v'],
#  [' ', ' ', ' ', ' ', ' ', 'v'],
#  [' ', ' ', ' ', ' ', ' ', 'v'],
#  [' ', ' ', ' ', ' ', ' ', '*']]
#
# Where '>', '<', '^', and 'v' refer to right, left, 
# up, and down motions. NOTE: the 'v' should be 
# lowercase.
#
# Your function should be able to do this for any
# provided grid, not just the sample grid below.
# ----------


# Sample Test case
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

#def search():
#    goal, actions = _search()
#    for row in actions:
#        print row

FAIL = 'fail'

def policy(grid=grid, init=init, goal=goal):
    goal, actions = _search()

    if goal is not FAIL:
        print 'actions: '
        for row in actions:
            print row
        g, y, x = goal
        p = [[' ' for col in range(len(grid[0]))]
             for row in range(len(grid))]
        p[y][x] = '*'
        y0, x0 = init

        while not (y == y0 and x == x0):
            print y, x
            index = actions[y][x]
            dt = delta[index]
            
            y1, x1 = dt
            print delta_name[index], y1, x1
            
            y -= y1
            x -= x1
            p[y][x] = delta_name[index]
        return p
    return None
    
def _search(grid=grid, init=init, goal=goal):
    unchecked = [[0, None] + init]
    checked = []
    expansion = [[-1 for col in range(len(grid[0]))] 
                 for row in range(len(grid))]
    expansion_index = 0
    
    actions = [[-1 for col in range(len(grid[0]))] 
              for row in range(len(grid))]
    
    while unchecked:
        # sort by g-value
        unchecked.sort(key=lambda x: x[0], reverse=True)
        
        # expand
        g, action, y, x = unchecked.pop()
        checked.append([y, x])
        actions[y][x] = action
        expansion[y][x] = expansion_index
        expansion_index += 1

        if [y, x] ==  goal:
            return [g, y, x], actions

        for action, dt in enumerate(delta):
            pos = move(grid, [y, x], dt)
            if pos and pos not in checked:
                node = [g + 1, action] + pos
                # use a set for this?
                if node not in unchecked:
                    unchecked.append(node)
    return FAIL, actions

p = policy()
if p:
    for row in p:
        print row