# --------------
# USER INSTRUCTIONS
#
# Write a function called stochastic_value that 
# takes no input and RETURNS two grids. The
# first grid, value, should contain the computed
# value of each cell as shown in the video. The
# second grid, policy, should contain the optimum
# policy for each cell.
#
# Stay tuned for a homework help video! This should
# be available by Thursday and will be visible
# in the course content tab.
#
# Good luck! Keep learning!
#
# --------------
# GRADING NOTES
#
# We will be calling your stochastic_value function
# with several different grids and different values
# of success_prob, collision_cost, and cost_step.
# In order to be marked correct, your function must
# RETURN (it does not have to print) two grids,
# value and policy.
#
# When grading your value grid, we will compare the
# value of each cell with the true value according
# to this model. If your answer for each cell
# is sufficiently close to the correct answer
# (within 0.001), you will be marked as correct.
#
# NOTE: Please do not modify the values of grid,
# success_prob, collision_cost, or cost_step inside
# your function. Doing so could result in your
# submission being inappropriately marked as incorrect.

# -------------
# GLOBAL VARIABLES
#
# You may modify these variables for testing
# purposes, but you should only modify them here.
# Do NOT modify them inside your stochastic_value
# function.

grid = [[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 1, 1, 0]]
       
goal = [0, len(grid[0])-1] # Goal is in top right corner


delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>'] # Use these when creating your policy grid.

success_prob = 0.5                      
failure_prob = (1.0 - success_prob)/2.0 # Probability(stepping left) = prob(stepping right) = failure_prob
collision_cost = 100                    
cost_step = 1.        
                     

############## INSERT/MODIFY YOUR CODE BELOW ##################
#
# You may modify the code below if you want, but remember that
# your function must...
#
# 1) ...be called stochastic_value().
# 2) ...NOT take any arguments.
# 3) ...return two grids: FIRST value and THEN policy.

def stochastic_value():
    return _stochastic_value(grid=grid, goal=goal)

def _stochastic_value(grid, goal):
    value = [[1000. for col in range(len(grid[0]))]
                   for row in range(len(grid))]
    
    policy = [[' ' for col in range(len(grid[0]))]
                   for row in range(len(grid))]
    
    y, x = goal
    value[y][x] = 0.
    policy[y][x] = '*'
    
    updated = True
    
    while updated:
        updated = False
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if [y, x] != goal and grid[y][x] == 0:
                    for index, _ in enumerate(delta):
                        v = cost_step
                        for i in range(-1, 2):
                            action = delta[(index + i) % len(delta)]
                            valid = move(grid, [y, x], action)

                            p = success_prob if i == 0. else \
                                (1.0 - success_prob) / 2.0
                            
                            scale = value[valid[0]][valid[1]] if valid else \
                                    collision_cost
                            v += p * scale

                        if v < value[y][x]:
                            value[y][x] = v
                            policy[y][x] = delta_name[index]
                            updated = True
                            
    return value, policy


def move(grid, pos, dt):
    y, x = pos
    y, x = [y + dt[0], x + dt[1]]
    valid = y >= 0 and y <= len(grid) - 1 and \
            x >= 0 and x <= len(grid[0]) - 1
    return [y, x] if valid and grid[y][x] == 0 else None


