import unittest

import q08
import q09
import q10

class SearchTest(unittest.TestCase):
    def test_search(self):
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
    
    def test_expand(self):
        grid = [[0, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 1, 0],
                [0, 0, 1, 0, 1, 0],
                [0, 0, 1, 0, 1, 0]]
        expand = q09.search()
        self.assertEqual(0, expand[0][0])
        self.assertEqual(22, expand[4][5])
        
        grid = [[0, 0, 1, 0, 0, 0],
                [0, 0, 1, 0, 0, 0],
                [0, 0, 1, 0, 1, 0],
                [0, 0, 1, 0, 1, 0],
                [0, 0, 1, 0, 1, 0]]
        
        expand = q09.search(grid=grid)
        unexpanded = [[-1 for row in range(len(grid[0]) - 2)] 
                      for col in range(len(grid))]
        self.assertEqual(unexpanded, 
                         [expand[i][2:] for i in xrange(len(expand))])
        
    def test_policy(self):
        grid = [[0, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 1, 0],
                [0, 0, 1, 0, 1, 0],
                [0, 0, 1, 0, 1, 0]]
        
        policy1 = [['>', 'v', ' ', ' ', ' ', ' '],
                   [' ', '>', '>', '>', '>', 'v'],
                   [' ', ' ', ' ', ' ', ' ', 'v'],
                   [' ', ' ', ' ', ' ', ' ', 'v'],
                   [' ', ' ', ' ', ' ', ' ', '*']]

        policy2 = [['v', ' ', ' ', ' ', ' ', ' '],
                   ['>', '>', '>', '>', '>', 'v'],
                   [' ', ' ', ' ', ' ', ' ', 'v'],
                   [' ', ' ', ' ', ' ', ' ', 'v'],
                   [' ', ' ', ' ', ' ', ' ', '*']]


        # both policies are equally likely
        try:
            self.assertEqual(policy1, q10.search(grid=grid))
        except:
            self.assertEqual(policy2, q10.search(grid=grid))
            
        
if __name__ == "__main__":
    unittest.main()
        