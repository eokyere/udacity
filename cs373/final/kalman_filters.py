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



def main():
    kf = KalmanFilter()
    values = [[1.0, 1.0, 1.0, 1.0],
              [1.0, 1.0, 5.0, 1.0],
              [1.0, 1.0, 5.0, 4.0]]
    
    print 'Measurement'
    for mu, sigma2, nu, r2 in values:
        print kf.update(sigma2=sigma2, r2=r2, mu=mu, nu=nu)

    print '\nPrediction'
    for mu, sigma2, nu, r2 in values:
        print kf.predict(sigma2=sigma2, r2=r2, mu=mu, nu=nu) 

    
    
main()