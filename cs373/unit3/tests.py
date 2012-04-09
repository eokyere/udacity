import unittest
from robot import robot
from math import pi
from lecture import ParticleFilter

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


#Kalman filters are more efficient vs Histogram filters
class ParticleFilterTests(unittest.TestCase):
    def test_particles(self):
        pf = ParticleFilter(1000)
        self.assertEqual(1000, len(pf.particles))
    
class RobotTests(PatchedTestCase):
    def setUp(self):
        self.bot = robot()
        self.bot.set(x=30., y=50., orientation=pi/2)
        self.expected_val0 = [39.0512, 46.0977, 39.0512, 46.0977]
        self.expected_val1 = [32.0156, 53.1507, 47.1699, 40.3113]
        
    def test_question_0(self):
        bot = self.bot
        bot.set_noise(forward_noise=0., turn_noise=0., sense_noise=0.)
        bot = self.first_move()
        self.assertAlmostEqual(self.expected_val0, bot.sense(), places=4)
        bot = self.second_move()
        self.assertAlmostEqual(self.expected_val1, bot.sense(), places=4)
        
        
    def test_question_1(self):
        bot = self.bot
        bot = self.first_move()
        self.assertAlmostEqual(self.expected_val0, bot.sense(), places=4)
        bot.set_noise(forward_noise=5., turn_noise=0.1, sense_noise=5.)
        bot = self.second_move()
        try:
            self.assertAlmostEqual(self.expected_val1, bot.sense(), places=4)
            fail('The values should differ from test without added noise')
        except: pass
            
    def first_move(self):
        self.bot = self.bot.move(turn=-pi/2, forward=15.)
        return self.bot
        
    def second_move(self):
        self.bot = self.bot.move(turn=-pi/2, forward=10.)
        return self.bot
        
if __name__ == "__main__":
    unittest.main()
        