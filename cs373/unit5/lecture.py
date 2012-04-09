from copy import deepcopy

def smooth(path, alpha=0.5, beta=0.1, tolerance=0.000001):
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
        for i in range(1, len(path) - 1):
            for j in range(len(path[0])):
                aux = p[i][j]
                p[i][j] += alpha * (path[i][j] - p[i][j])
                p[i][j] += beta * (p[i - 1][j] + p[i + 1][j] - 2.0 * p[i][j])
                change += abs(aux - p[i][j])
    return p



def debug(path, p):
    for i in range(len(path)):
        print '[' + ', '.join('%.3f' % x for x in path[i]) + '] -> [' + \
        ', '.join('%.3f' % x for x in p[i]) + ']'

path = [[0, 0], [0, 1], [0, 2], [1, 2], [2, 2], [3, 2], [4, 2], [4, 3], [4, 4]]
p = smooth(path, alpha=0, beta=0.1)
debug(path, p)