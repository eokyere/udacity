def main():
    world = [['green', 'green'],
             ['red', 'green']]

    def _sense(p, Z):
        return _chunked(sense(_flatten(p), Z, _flatten(world)), len(world[0]))

    
    n = len(world) * len(world[0])
    p = _chunked([1. / n ] * n, len(world[0]))
    debug(p)    
    p = _sense(p, 'red')
    debug(p)
    #p = move(p, 'N')
    p = [[0.714, 0.286],
         [0., 0.]]
    debug(p)
    p = _sense(p, 'red')
    debug(p)
    
def debug(p):
    print
    for row in p:
        _printf(row)
    
def sense(p, Z, world):
    q = [(_score(i, Z, world) * p[i]) for i in range(len(p))]
    s = sum(q)
    return [i/s for i in q]

def move(p, dir):
    pass

def _score(i, Z, world):
    return 0.8 if Z == world[i] else 0.2    


def _chunked(seq, size):
    return [seq[pos:pos + size] for pos in xrange(0, len(seq), size)]
    
def _flatten(two_d):
    return [col for row in two_d for col in row]

def _printf(x, format='%.4f'):
    if isinstance(x, list):
        print [format % i for i in x]
    elif isinstance(x, float):
        print format % x
    else:
        print x
        
if __name__ =="__main__":
    main()
    