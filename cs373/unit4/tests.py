import unittest

import q08, q09, q10, q12, q17

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
            self.assertEqual(policy1, q10.policy(grid=grid))
        except:
            self.assertEqual(policy2, q10.policy(grid=grid))
    
    def test_a_star(self):
        grid = [[0, 1, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 0]]
        
        expected = [[0, -1, -1, -1, -1, -1],
                    [1, -1, -1, -1, -1, -1],
                    [2, -1, -1, -1, -1, -1],
                    [3, -1,  8,  9, 10, 11],
                    [4,  5,  6,  7, -1, 12]]
        
        self.assertEqual(expected, q12.search(grid=grid))

    def test_value_function(self):
        grid = [[0, 0, 1, 0, 0, 0],
                [0, 0, 1, 0, 0, 0],
                [0, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 1, 0],
                [0, 0, 1, 1, 1, 0],
                [0, 0, 0, 0, 1, 0]]
        
        expected = [[12, 11, 99,  7,  6,  5],
                    [11, 10, 99,  6,  5,  4],
                    [10,  9, 99,  5,  4,  3],
                    [ 9,  8,  7,  6, 99,  2],
                    [10,  9, 99, 99, 99,  1],
                    [11, 10, 11, 12, 99,  0]]

        goal = [len(grid)-1, len(grid[0])-1]

        
        self.assertEqual(expected, q17._compute_value(grid=grid, goal=goal))
        
        grid = [[0, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 0],
                [0, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 1, 0],
                [0, 0, 1, 1, 1, 0],
                [0, 0, 0, 0, 1, 0]]
        
        expected = [[10,  9,  8,  7,  6,  5],
                    [11, 10, 99,  6,  5,  4],
                    [10,  9, 99,  5,  4,  3],
                    [ 9,  8,  7,  6, 99,  2],
                    [10,  9, 99, 99, 99,  1],
                    [11, 10, 11, 12, 99,  0]]
        
        
        self.assertEqual(expected, q17._compute_value(grid=grid, goal=goal))
        
        
if __name__ == "__main__":
    unittest.main()
        