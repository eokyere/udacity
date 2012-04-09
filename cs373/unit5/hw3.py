# -------------
# User Instructions
#
# Now you will be incorporating fixed points into
# your smoother. 
#
# You will need to use the equations from gradient
# descent AND the new equations presented in the
# previous lecture to implement smoothing with
# fixed points.
#
# Your function should return the newpath that it
# calculates. 
#
# Feel free to use the provided solution_check function
# to test your code. You can find it at the bottom.
#
# --------------
# Testing Instructions
# 
# To test your code, call the solution_check function with
# two arguments. The first argument should be the result of your
# smooth function. The second should be the corresponding answer.
# For example, calling
#
# solution_check(smooth(testpath1), answer1)
#
# should return True if your answer is correct and False if
# it is not.

from math import *

# Do not modify path inside your function.
path=[[0, 0], #fix 
      [1, 0],
      [2, 0],
      [3, 0],
      [4, 0],
      [5, 0],
      [6, 0], #fix
      [6, 1],
      [6, 2],
      [6, 3], #fix
      [5, 3],
      [4, 3],
      [3, 3],
      [2, 3],
      [1, 3],
      [0, 3], #fix
      [0, 2],
      [0, 1]]

# Do not modify fix inside your function
fix = [1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0]

######################## ENTER CODE BELOW HERE #########################

from copy import deepcopy

def smooth(path, fixed, alpha=0.0, beta=0.1, gamma=0.05, tolerance=0.00001):
    """
    (xi, yi) <- (xi, yi)*gamma * [2 * (xi-1, yi-1) - (xi-2, yi-2) - (xi, yi)]
    (xi, yi) <- (xi, yi)*gamma * [2 * (xi+1, yi+1) - (xi+2, yi+2) - (xi, yi)]
    """
    p = deepcopy(path)
    
    
    change = tolerance
    
    while change >= tolerance:
        change = 0.0
        for i in range(len(path)):
            if not fixed[i]:
                for j in range(len(path[0])):
                    aux = p[i][j]
                    p[i][j] += alpha * (path[i][j] - p[i][j])
                    prev = (i - 1) % len(path)
                    next = (i + 1) % len(path)
                    p[i][j] += beta * (p[prev][j] + \
                                       p[next][j] - 2.0 * p[i][j])
                    p[i][j] += gamma * (2.0 * p[prev][j] - p[(i - 2) % len(path)][j] - p[i][j])
                    p[i][j] += gamma * (2.0 * p[next][j] - p[(i + 2) % len(path)][j] - p[i][j])
                    change += abs(aux - p[i][j])
    return p



