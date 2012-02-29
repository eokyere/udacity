import unittest

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


class TestPatchedTestCase(PatchedTestCase):
    def test_list_of_lists(self):
        expected =  [[0.06666, 0.06666, 0.06666],
                     [0.06666, 0.26666, 0.26666],
                     [0.06666, 0.06666, 0.06666]]
        
        actual   = [[0.0666611, 0.06666, 0.06666],
                    [0.06666212, 0.266664352, 0.26666234],
                    [0.0666496564, 0.0666612, 0.066662]]
        
        self.assertAlmostEqual(expected, actual, places=4)
        
        try:
            actual = [[0.0666611, 0.06666, 0.06666],
                      [0.06666212, 0.266664352, 0.26666234],
                      [0.0666096564, 0.0666612, 0.066662]]
            self.assertAlmostEqual(expected, actual, places=4)
            fail('This should not pass')
        except: pass
        
    def test_list(self):
        expected = [0.1111, 0.3333, 0.3333, 0.1111, 0.1111]
        actual   = [0.11109, 0.3333, 0.3333, 0.1111, 0.11106]
        self.assertAlmostEqual(expected, actual, places=4)

if __name__ == "__main__":
    unittest.main()