colors = [['red', 'green', 'green', 'red' , 'red'],
          ['red', 'red', 'green', 'red', 'red'],
          ['red', 'red', 'green', 'green', 'red'],
          ['red', 'red', 'red', 'red', 'red']]

measurements = ['green', 'green', 'green' ,'green', 'green']


motions = [[0,0], [0,1], [1,0], [1,0], [0,1]]

sensor_right = 0.7

p_move = 0.8

def show(p):
    for i in range(len(p)):
        print p[i]

#DO NOT USE IMPORT
#ENTER CODE BELOW HERE
#ANY CODE ABOVE WILL CAUSE
#HOMEWORK TO BE GRADED
#INCORRECT

UP = -1
DOWN = 1
RIGHT = 1
LEFT = -1

class Robot():
    def __init__(self, world, sensor=None, movement=None):
        self.world = world
        self.sensor = sensor
        self.movement = movement
        
    def localize(self, measurements, motions, p=None):
        if not p:
            p = self._p()
        for measurement, motion in zip(measurements, motions):
            p = self.move(p, motion)
            p = self.sense(p, measurement)
        return p
    
    def sense(self, p, measurement):
        if isinstance(measurement, list):
            for z in measurement:
                p = self.sense(p, z)
        else:
            q = [[self._s(i, j, measurement) * val for j, val in enumerate(row)] \
                 for i, row in enumerate(p)]
            s = sum([col for row in q for col in row])
            p = [[i/s for i in row] for row in q]
        return p
    
    def move(self, p, motion):
        if isinstance(motion, list):
            if isinstance(motion[0], list):
                for m in motion:
                    p = self.move(p, m)
            else:
                _p = self._flatten(p)
                y, x = motion
                if y == UP:
                    p = p[1:] + [p[0]]
                elif y == DOWN:
                    p = [p[-1]] + p[:len(p) - 1]
                
                if x == RIGHT:
                    p = [self._move(xs, 1) for xs in p]
                elif x == LEFT:
                    p = [self._move(xs, len(xs) - 1) for xs in p]
                
                # if movement is None we assume movement has 1.0 accuracy
                if self.movement and self.movement < 1.0:
                    xs = zip([x * self.movement for x in self._flatten(p)], 
                             [x * (1.0 - self.movement) for x in _p])
                    p = self._chunked([sum(x) for x in xs], len(p[0]))
        return p
        
    def _move(self, p, U):
        """Move left or right"""
        n = len(p)
        x = n - (U % n)
        return p[x:] + p[:x]        

    def _s(self, i, j, Z):
        return self.sensor if Z == self.world[i][j] else 1.0 - self.sensor
    
    def _p(self, rows=None, cols=None):
        """Generate the uniform distribution"""
        if not (rows and cols):
            rows = len(self.world)
            cols = len(self.world[0])
        n = rows * cols
        return self._chunked([1./n] * n, cols)

    def _chunked(self, seq, size):
        return [seq[pos:pos + size] for pos in xrange(0, len(seq), size)]
        
    def _flatten(self, two_d):
        return [col for row in two_d for col in row]


def main():
    robot = Robot(world=colors)
    robot.sensor = sensor_right
    robot.movement = p_move
    p = robot.localize(measurements=measurements, 
                       motions=motions)
    
    #Your probability array must be printed 
    #with the following code.
    
    show(p)

if __name__ == "__main__":
    main()



