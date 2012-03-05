from math import pi, sqrt, exp
from matrix import matrix

# Junior takes distance scans 10x per second with the laser range finder
# about 10 ** 6 data points

#def coconut_monkey():
#    monkey = 6 #coconuts
#    x 

def main():
    print 'The number of coconuts are: ', coconuts()
    
#    for x in xrange(1, 20000):
#        print 'fx is: ', x *.1, guassian(mu=10., sigma2=4., x=x * .1)

    kf = KalmanFilter()
    print kf._mu_prime(sigma2=4., r2=4., mu=10., nu=12.)
    print kf._sigma2_prime(sigma2=4., r2=4.)

    print kf._mu_prime(sigma2=8., r2=2., mu=10., nu=13.)
    print kf._sigma2_prime(sigma2=8., r2=2.)
    
    mu, sigma2, u, r2 = 8., 4., 10., 6.
    print kf.predict(mu=mu, u=u, sigma2=sigma2, r2=r2)

def coconuts():    
    """5 people and 1 monkey collect n coconuts.
    Each of the 5 persons take turns in giving a coconut to the monkey,
    and then stashing 1/5th of the remaining coconuts. The number of coconuts
    left at each turn, after a coconut has been given to the monkey is divisible
    by 5. How many coconuts did they originally collect?
    """
    def f(n):
        for i in range(6):
            n -= 1 # given to monkey
            if n % 5 is not 0:
                return False
            n -= n/5 # stash away 1/5th
        return True
    
    i = 1
    while True:
        if f(i):
            break
        i += 1
    return i


def gaussian(x, mu, sigma2):
    """f(x) = 1/2*pi*sigma2 * exp(-.5(x-mu)**2/sigma2)
    """
    return exp(-.5 * (x - mu) ** 2 / sigma2) / sqrt(2 * pi * sigma2)


class KalmanFilter(object):
    """Represents all distributions by Guassians
    """
    def run(self, measurements, motion, measurement_sig, motion_sig, mu, sig):
        for nu, vu in zip(measurements, motion):
            mu, sig = self.measure(mu=mu, sigma2=sig, nu=nu, r2=measurement_sig)
            mu, sig = self.predict(mu=mu, sigma2=sig, nu=vu, r2=motion_sig)
        return mu, sig
    
    def update(self, mu, sigma2, nu, r2):
        """Uses Bayes' rule (product)"""
        return (self._mu_prime(mu=mu, sigma2=sigma2, nu=nu, r2=r2),
                self._sigma2_prime(sigma2, r2))
    measure=update
    
    def predict(self, mu, nu, sigma2, r2):
        """Motion update - Uses total probablity (convolution/addition)"""
        return mu + nu, sigma2 + r2

    def _mu_prime(self, mu, sigma2, nu, r2):
        return (r2 * mu + sigma2 * nu) / (r2 + sigma2)
    
    def _sigma2_prime(self, sigma2, r2):
        return 1. / (1./sigma2 + 1./r2)
    

class MultivariateGaussian(object):
    """Parameters mu, sigma
    """
#    def p(self, x, mu, sigma, n):
#        """
#        x is an n dimensional vector of real numbers
#        """
#        return (2*pi) ** -.5*n * det(sigma) ** -.5 * \
#               exp(-.5 * transpose((x - mu)) * sigma ** -1 * (x-mu))
#    
#    def _mu(self, m, x):
#        """mu is the avg of all the training examples in x
#        """
#        pass
#    
#    def _sigma(self, m, x):
#        pass
    pass

    
class NDKalmanFilter(object):
    def run(self, measurements, x, u, F, P, H, R, I=None):
        """
        measurements observations/measurements
        x initial estimate (an n dimensional vector of Real numbers)
        F state transition matrix
        u motion vector
        P uncertainty covariance
        """
        for Z in measurements:
            x, P = self.measure(Z=Z, x=x, H=H, R=R, P=P, I=I)
            x, P = self.predict(x=x, u=u, F=F, P=P)
        return x, P
    
    def run2(self, measurements, x, u, F, P, H, R, I=None):
        """
        measurements observations/measurements
        x initial estimate (an n dimensional vector of Real numbers)
        F state transition matrix
        u motion vector
        P uncertainty covariance
        """
        for Z in measurements:
            x, P = self.predict(x=x, u=u, F=F, P=P)
            x, P = self.measure(Z=Z, x=x, H=H, R=R, P=P, I=I)
        return x, P
    
    def predict(self, x, u, F, P):
        """
        x initial estimate (an n dimensional vector of Real numbers)
        F state transition matrix
        u motion vector
        P uncertainty covariance
        """
        x = (F * x) + u
        P = F * P * F.transpose()
        return x, P
    
    def measure(self, Z, x, H, R, P, I=None):
        """
        Z measurement
        H measurement function
        R measurement noise
        K Kalman gain
        P uncertainty covariance
        """
        Z = matrix([Z]) # assume measurements are passed in as lists
        y = Z.transpose() - (H * x)        
        S = H * P * H.transpose() + R
        K = P * H.transpose() * S.inverse()
        x = x + (K * y)
        
        if not I:
            I = self._eye(x.dimx) #matrix([[1., 0.], [0., 1.]]) # identity matrix
        P = (I - (K * H)) * P
        return x, P

    def _eye(self, dim):
        m = matrix([[]])
        m.identity(dim)
        return m
    
    def _scale(self, mx, scalar):
        sx = matrix([[]])
        sx.zero(mx.dimx, mx.dimy)
        
        for i in range(mx.dimx):
            for j in range(mx.dimy):
                sx.value[i][j] = mx.value[i][j] * scalar
        return sx

if __name__ == "__main__":
    main()
