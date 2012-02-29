from __future__ import division

R = 'red'
G = 'green'
WORLD = [G, R, R, G, G]
hit_score = 0.6
miss_score = 0.2

def main():
    n = 5
    Z = R    
    p = [1 / n ] * n
    
    print 'sense: ',
    _printf(sense(p, Z))
    _printf(sense_all(p, [R, G]))
    
    print '\nmove:'
    for i in range(10):
        print move([0,1,0,0,0], i)

    _printf(move1([0.2, 0.2, 0.2, 0.2, 0.2], 2))
    
    p = [0, 1, 0, 0, 0]
    U = 1
    _printf(move1(p, U))
    _printf(xmove(p, U, 1, 1, 0.8, 0.1, 0.1))
    
    print '\nmove limit (afer 200 iterations)'
    for i in range(200):
        p = xmove(p, U, 1, 0, 0.8, 0.1, 0.1)
    _printf(p)

    # sense and move exercise
    print '\nlocalize (sense and move)'
    p = [1 / n ] * n
    print 'world:\t\t', WORLD
    print 'red, green:\t', 
    _printf(localize(p, [R, G], [1, 1]))
    print 'red, red:\t',
    _printf(localize(p, [R, R], [1, 1]))

def localize(p, measurements, motions):
    for Z, U in zip(measurements, motions):
        p = sense(p, Z)
        p = xmove(p, U, 1, 1, 0.8, 0.1, 0.1)
    return p

def sense_all(p, measurements):
    for Z in measurements:
        p = sense(p, Z)
    return p

def sense(p, Z):
    q = [(_score(i, Z) * p[i]) for i in range(len(p))]
    s = sum(q)
    return [i/s for i in q]

def move1(p, U):
    """First implementation before generalizing with xmove
    """
    pe, po, pu = 0.8, 0.1, 0.1
    xs = zip(move([x * pe for x in p], U),
             move([x * po for x in p], U + 1),
             move([x * pu for x in p], U - 1))
    return [sum(x) for x in xs]
    
def xmove(p, U, o, u, pe, po, pu):
    xs = zip(move([x * pe for x in p], U),
             move([x * po for x in p], U + o),
             move([x * pu for x in p], U - u))
    return [sum(x) for x in xs]

def move(p, U):
    n = len(p)
    x = n - (U % n)
    return p[x:] + p[:x]

def _score(i, Z):
    return hit_score if Z == WORLD[i] else miss_score

def _printf(x, format='%.4f'):
    if isinstance(x, list):
        print [format % i for i in x]
    elif isinstance(x, float):
        print format % x
    else:
        print x
    
if __name__ == "__main__":
    main()