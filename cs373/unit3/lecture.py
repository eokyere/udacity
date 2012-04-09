from robot import robot
import random

def update(p):
    return p.move(0.1, 5.)

def particle():
    p = robot()
    p.set_noise(0.5, 0.5, 5)
    return p
        
def re_sample(ws):
    n = len(ws)
    index = random.random() * n
    beta = 0.0
    W = max(ws)
    xs = []
    for _ in range(n):
        beta += random.random() * 2.0 * W
        while beta > wx[index]:
            beta -= wx[index]
            index = (index + 1) % n
        xs.append(index)
    return xs

class ParticleFilter(object):
    """
    Properties:
    state space - continuous
    belief - multimodal
    
    - It is a mistake to represent PF over 4 dimensions
    - Really easy to program
    - Flexible
    
    # look at measurements
    # compute weights
    # sample
    # predict
    """
    def __init__(self, N):
        self.bot = robot()
        self.particles = []
        for i in range(N):
            self.particles.append(particle())

    def run(self, n):
        for i in range(n):
            self.measure()
            self.particles = [self.particles[i] \
                              for i in re_sample(self.compute_weights())]

    def measure(self):
        self.bot = update(self.bot)
        self.particles = map(update, self.particles)

    def compute_weights(self):
        wx =  [p.measurement_prob(self.bot) for p in self.particles]
        #normalize
        W = sum(wx)
        return [w/W for w in wx]
    
    
def main():
    pass

