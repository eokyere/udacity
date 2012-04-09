def _(key):
    return not key

ON = True
OFF = _(ON)

class ParticleFilter(object):
    _m = {}
    def __init__(self):
        pass
    
    def a(self, obs, given, value):
        self._m[given] = {   obs: value,
                          _(obs): 1 - value}
        
    def p(self, obs, given):
        return self._m[given][obs]
    
    def w(self, measurement, index, xs, states=[ON, OFF]):
        # count
        count = {}
        for k in states:
            count[k] = 0

        for x in xs:
            count[x.state] += 1        
        
        #total weight
        weight = {}
        for s in states:
            weight[s] = count[s] * self.p(measurement, s)
        total_weight = sum([x for x in weight.values()])
        
        # normalize
        return self.p(measurement, xs[index].state) / total_weight
    

class X(object):
    def __init__(self, state, name=None):
        self.name = name
        self.state = state
        
    def __str__(self):
        return self.name if self.name else '{x}'



def main():
    # assume ON is on a red square
    xs = [X(OFF, 'TL'), X(OFF, 'TL'), X(OFF, 'TL'), 
          X(OFF, 'TR'), X(OFF, 'TR'), X(OFF, 'TR'), 
          X(ON, 'BL'), X(ON, 'BL'), X(ON, 'BL'),
          X(OFF, 'BR'), X(OFF, 'BR'), X(OFF, 'BR')]
    
    RED = True
    GREEN = _(RED)
    
    pf = ParticleFilter()
    pf.a(RED, ON, 0.8)
    pf.a(RED, OFF, 0.2)
    
    for i in xrange(len(xs)):
        print '%s - %.4f' % (xs[i], pf.w(RED, i, xs),)


main()
    