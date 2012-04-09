# -------------
# User Instructions
#
# Here you will be implementing a cyclic smoothing
# algorithm. This algorithm should not fix the end
# points (as you did in the unit quizzes). You  
# should use the gradient descent equations that
# you used previously.
#
# Your function should return the newpath that it
# calculates..
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
path=[[0, 0], 
      [1, 0],
      [2, 0],
      [3, 0],
      [4, 0],
      [5, 0],
      [6, 0],
      [6, 1],
      [6, 2],
      [6, 3],
      [5, 3],
      [4, 3],
      [3, 3],
      [2, 3],
      [1, 3],
      [0, 3],
      [0, 2],
      [0, 1]]

############# ONLY ENTER CODE BELOW THIS LINE ##########

# ------------------------------------------------
# smooth coordinates
# If your code is timing out, make the tolerance parameter
# larger to decrease run time.
#

from copy import deepcopy

def smooth(path, alpha=0.1, beta=0.1, tolerance=0.00001):
    """
    (xi - yi)^2 --> min
    (yi - yi+1)^2 --> min
    
    yi = yi + a(xi - yi)
    yi = yi + B(yi+1 + yi-1 - 2yi) 
    """
    p = deepcopy(path)
    
    
    change = tolerance
    
    while change >= tolerance:
        change = 0.0
        for i in range(len(path)):
            for j in range(len(path[0])):
                aux = p[i][j]
                p[i][j] += alpha * (path[i][j] - p[i][j])
                p[i][j] += beta * (p[(i - 1) % len(path)][j] + \
                                   p[(i + 1) % len(path)][j] - 2.0 * p[i][j])
                change += abs(aux - p[i][j])
    return p



