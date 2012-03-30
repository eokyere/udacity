import unittest

import q08

class SearchTest(unittest.TestCase):
    def test_q_08(self):
        self.assertEqual([11, 4, 5], q08.search())

        grid = [[0, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 0],
                [0, 0, 1, 1, 1, 0],
                [0, 0, 0, 0, 1, 0]]
        
        self.assertEqual([9, 4, 5], q08._search(grid))
        
        grid = [[0, 0, 1, 0, 0, 0],
                [0, 0, 1, 0, 0, 0],
                [0, 0, 1, 0, 1, 0],
                [0, 0, 1, 0, 1, 0],
                [0, 0, 0, 0, 1, 0]]
        
        self.assertEqual([15, 4, 5], q08._search(grid))
        
        grid = [[0, 0, 1, 0, 0, 0],
                [0, 0, 1, 0, 0, 0],
                [0, 0, 1, 0, 1, 0],
                [0, 0, 1, 0, 1, 0],
                [0, 0, 1, 0, 1, 0]]
        self.assertEqual('fail', q08._search(grid))
        
if __name__ == "__main__":
    unittest.main()
        