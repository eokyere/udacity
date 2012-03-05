import unittest
import random, string 

import homework as hw
import lecture as lt

def random_strings(n=10):
    return ''.join(random.choice(string.letters + string.digits) \
                   for i in xrange(n))

class LectureTests(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(24, lt.factorial(4))
        self.assertEqual(6, lt.factorial(3))


class HomeworkTests(unittest.TestCase):
    def test_udacify(self):
        for s in random_strings(20):
            self.assertTrue(hw.udacify(s).startswith('U'))
    
    def test_median(self):
        self.assertEqual(2, hw.median(1, 2, 3))
        self.assertEqual(2, hw.median(1, 3, 2))
        self.assertEqual(2, hw.median(2, 3, 1))
        self.assertEqual(2, hw.median(2, 1, 3))
        self.assertEqual(2, hw.median(3, 1, 2))
        self.assertEqual(2, hw.median(3, 2, 1))
        self.assertEqual(6, hw.median(9, 3, 6))
        self.assertEqual(6, hw.median(6, 3, 9))
        self.assertEqual(7, hw.median(7, 8, 7))
        self.assertEqual(7, hw.median(7, 7, 8))


if __name__ == "__main__":
    unittest.main()