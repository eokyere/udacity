import unittest

import lecture as lt
from lecture import KalmanFilter
from lecture import NDKalmanFilter
from matrix import matrix

import homework as hw

class PatchedTestCase(unittest.TestCase):
    _assertAlmostEqual = unittest.TestCase.assertAlmostEqual
    def assertAlmostEqual(self, val0, val1, places=None, msg=None, delta=None):
        if type(val0) is not type(val1):
            print 'type of val0: ', type(val0)
            print 'type of val1: ', type(val1)
        assert type(val0) is type(val1)
        
        if type(val0) in [list, tuple]:
            assert len(val0) is len(val1)
            for val0, val1 in zip(val0, val1):
                self.assertAlmostEqual(val0, val1, places, msg, delta)
        else:
            self._assertAlmostEqual(val0, val1, places, msg, delta)

class MonkeyTests(unittest.TestCase):
    def test_monkey_coconuts_5(self):
        n = lt.coconuts()
        pass

class GaussianTests(unittest.TestCase):
    def test_fx(self):
        self.assertAlmostEqual(0.120985, lt.gaussian(mu=10., sigma2=4., x=8.), 
                               places=6)

class KalmanFilterTests(unittest.TestCase):
    def test_update(self):
        f = KalmanFilter()
        mu, sigma2, nu, r2 = 10., 8., 13., 2.
        mu_prime, sigma2_prime = f.update(mu=mu, nu=nu, sigma2=sigma2, r2=r2)
        self.assertAlmostEqual(12.4, mu_prime, places=1)
        self.assertAlmostEqual(1.6, sigma2_prime, places=1)
        
    def test_predict(self):
        f = KalmanFilter()
        mu, sigma2, nu, r2 = 10., 4., 12., 4.
        mu_prime, sigma2_prime = f.predict(mu=mu, nu=nu, sigma2=sigma2, r2=r2)
        self.assertAlmostEqual(22.0, mu_prime, places=1)
        self.assertAlmostEqual(8.0, sigma2_prime, places=1)
        
    def test_all(self):
        expected_mu = 10.9999
        expected_sig = 4.0059

        mu = 0.
        sig = 10000.
        measurement_sig, motion_sig = 4., 2.
        measurements = [5., 6., 7., 9., 10.]
        motion = [1., 1., 2., 1., 1.]
        
        f = KalmanFilter()
        mu, sig = f.run(measurements=measurements, motion=motion, 
                        measurement_sig=measurement_sig, motion_sig=motion_sig,
                        mu=mu, sig=sig)
        self.assertAlmostEqual(expected_mu, mu, places=4)
        self.assertAlmostEqual(expected_sig, sig, places=4)


class NDKalmanFilterTests(PatchedTestCase):
    def test_filter(self):
        measurements = [[1.], [2.], [3.]] # locations
        
        x = matrix([[0.], [0.]]) #initial state (location and velocity)
        P = matrix([[1000., 0.], [0., 1000.]]) # initial uncertainty
        u = matrix([[0.], [0.]]) # intial external motion
        F = matrix([[1., 1.], [0., 1.]]) # new state function
        H = matrix([[1., 0.]]) # measurement function
        R = matrix([[1.]]) # measurement uncertainty
        
        ndkf = NDKalmanFilter()
        x, P = ndkf.run(measurements=measurements,
                        x=x, P=P, u=u, F=F, H=H, R=R)
        
        expected_x = [[4.0], [1.0]]
        expected_P = [[2.3319, 0.9992],
                      [0.9992, 0.4995]]
        
        self.assertAlmostEqual(expected_x, x.value, places=0)
        self.assertAlmostEqual(expected_P, P.value, places=4)


class TestHomework(PatchedTestCase):
    def test_example_0(self):
        expected_x = [[10.0], [0.0], [10.0], [-20.0]]
        expected_P = [[0.0396, 0.0, 0.0659, 0.0],
                      [0.0, 0.0396, 0.0, 0.0659],
                      [0.0659, 0.0, 0.1099, 0.0],
                      [0.0, 0.0659, 0.0, 0.1099]]
        
        measurements = [[5., 10.], [6., 8.], [7., 6.], 
                        [8., 4.],  [9., 2.], [10., 0.]]
        initial_xy = [4., 12.]
        self._test(measurements, initial_xy, expected_x, expected_P)

    def test_example_1(self):
        expected_x = [[16.0], [-8.0], [50.0], [-40.0]]
        expected_P = [[0.0533, 0.0, 0.1333, 0.0],
                      [0.0, 0.0533, 0.0, 0.1333],
                      [0.1333, 0.0, 0.3332, 0.0],
                      [0.0, 0.1333, 0.0, 0.3332]]
        
        measurements = [[1., 4.], [6., 0.], [11., -4.], [16., -8.]]
        initial_xy = [-4., 8.]
        self._test(measurements, initial_xy, expected_x, expected_P)

    def test_example_2(self):
        expected_x = [[1.0], [11.0], [0.0], [-20.0]]
        expected_P = [[0.0533, 0.0, 0.1333, 0.0],
                      [0.0, 0.0533, 0.0, 0.1333],
                      [0.1333, 0.0, 0.3332, 0.0],
                      [0.0, 0.1333, 0.0, 0.3332]]
        measurements = [[1., 17.], [1., 15.], [1., 13.], [1., 11.]]
        initial_xy = [1., 19.]
        self._test(measurements, initial_xy, expected_x, expected_P)
    
    def _test(self, measurements, initial_xy, expected_x, expected_P):
        ndkf = NDKalmanFilter()

        dt = 0.1
        
        x = matrix([[initial_xy[0]], [initial_xy[1]], [0.], [0.]]) # initial state (location and velocity)
        u = matrix([[0.], [0.], [0.], [0.]]) # external motion


        x, P = ndkf.run2(measurements=measurements,
                         x=x, P=hw.P, u=u, F=hw.F, H=hw.H, R=hw.R, I=hw.I)
        
        self.assertAlmostEqual(expected_x, x.value, places=0)
        self.assertAlmostEqual(expected_P, P.value, places=4)


if __name__ == "__main__":
    unittest.main()