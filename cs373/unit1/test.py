from __future__ import division
import unittest
import testutil
from lecture import *

class LectureTests(testutil.PatchedTestCase):
    def test_sense(self):
        expected = [0.1111, 0.3333, 0.3333, 0.1111, 0.1111]
        n = 5
        p = [1 / n ] * n
        self.assertAlmostEqual(expected, sense(p, R), places=4)

    def test_sense_all(self):
        expected = [0.2000, 0.2000, 0.2000, 0.2000, 0.2000]
        n = 5
        p = [1 / n ] * n
        self.assertAlmostEqual(expected, sense_all(p, [R, G]))

    def test_move(self):
        xs = [1, 0, 0, 0, 0]
        self.assertAlmostEqual([0, 1, 0, 0, 0], move(xs, 1), places=0)
        self.assertAlmostEqual([0, 0, 1, 0, 0], move(xs, 2), places=0)
        self.assertAlmostEqual([0, 0, 0, 1, 0], move(xs, 3), places=0)
        self.assertAlmostEqual([0, 0, 0, 0, 1], move(xs, 4), places=0)
        self.assertAlmostEqual([1, 0, 0, 0, 0], move(xs, 5), places=0)
    
    def test_move1(self):
        expected = [0.0000, 0.1000, 0.8000, 0.1000, 0.0000]
        p = [0, 1, 0, 0, 0]
        U = 1
        self.assertAlmostEqual(expected, move1(p, U), places=4)
        
        expected = [0.2000, 0.2000, 0.2000, 0.2000, 0.2000]
        p = [0.2, 0.2, 0.2, 0.2, 0.2] 
        U = 2         
        p = move1(p, U)
        self.assertAlmostEqual(expected, p, places=4)
        
    def test_xmove(self):
        expected = [0.0000, 0.1000, 0.8000, 0.1000, 0.0000]
        p = [0, 1, 0, 0, 0]
        U = 1
        p = xmove(p, U, 1, 1, 0.8, 0.1, 0.1)
        self.assertAlmostEqual(expected, p, places=4)

    def test_move_limit_after_200_iterations(self):
        expected = [0.2000, 0.2000, 0.2000, 0.2000, 0.2000]
        p = [0, 1, 0, 0, 0]
        U = 1
        for i in range(200):
            p = xmove(p, U, 1, 0, 0.8, 0.1, 0.1)
        self.assertAlmostEqual(expected, p, places=4)
        
    def test_localize(self):
        n = 5
        p = [1 / n ] * n
        
        expected = [0.2116, 0.1516, 0.0811, 0.1684, 0.3874]
        result = localize(p, [R, G], [1, 1])
        self.assertAlmostEqual(expected, result, places=4)

        expected = [0.0788, 0.0753, 0.2247, 0.4329, 0.1882] 
        result = localize(p, [R, R], [1, 1])
        self.assertAlmostEqual(expected, result, places=4)


if __name__ == "__main__":
    unittest.main()