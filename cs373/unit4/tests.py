import unittest

import q08, q09, q10, q12, q17, q18, q19
import homework

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
    
    def test_value_function_with_cutoff(self):
        grid = [[0, 0, 1, 0, 0, 0],
                [0, 0, 1, 0, 0, 0],
                [0, 0, 1, 0, 0, 0],
                [0, 0, 1, 0, 1, 0],
                [0, 0, 1, 1, 1, 0],
                [0, 0, 0, 0, 1, 0]]
        
        expected = [[99, 99, 99,  7,  6,  5],
                    [99, 99, 99,  6,  5,  4],
                    [99, 99, 99,  5,  4,  3],
                    [99, 99, 99,  6, 99,  2],
                    [99, 99, 99, 99, 99,  1],
                    [99, 99, 99, 99, 99,  0]]
        
        
        goal = [len(grid)-1, len(grid[0])-1]
        self.assertEqual(expected, q17._compute_value(grid=grid, goal=goal))
    
    def test_dynamic_programming_policy(self):
        grid = [[0, 0, 1, 0, 0, 0],
                [0, 0, 1, 0, 0, 0],
                [0, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 1, 0],
                [0, 0, 1, 1, 1, 0],
                [0, 0, 0, 0, 1, 0]]
        
        expected = [['v', 'v', ' ', 'v', 'v', 'v'],
                    ['v', 'v', ' ', 'v', 'v', 'v'],
                    ['v', 'v', ' ', '>', '>', 'v'],
                    ['>', '>', '>', '^', ' ', 'v'],
                    ['^', '^', ' ', ' ', ' ', 'v'],
                    ['^', '^', '<', '<', ' ', '*']]

        goal = [len(grid)-1, len(grid[0])-1]
        _, policy = q18._optimum_policy(grid=grid, goal=goal)
        self.assertEqual(expected, policy)
        
    
    def test_turn_policy(self):
        init = [4, 3, 0]
        grid = [[1, 1, 1, 0, 0, 0],
                [1, 1, 1, 0, 1, 0],
                [0, 0, 0, 0, 0, 0],
                [1, 1, 1, 0, 1, 1],
                [1, 1, 1, 0, 1, 1]]
        goal = [2, 0]        
        cost = [2, 1, 1]
        expected = [[' ', ' ', ' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ', ' ', ' '],
                    ['*', '#', '#', 'L', ' ', ' '],
                    [' ', ' ', ' ', '#', ' ', ' '],
                    [' ', ' ', ' ', '#', ' ', ' ']]
    
        self.assertEqual(expected, q19._optimum_policy2d(grid, init, goal, cost))

        cost = [2, 1, 20]
        expected = [[' ', ' ', ' ', 'R', '#', 'R'],
                    [' ', ' ', ' ', '#', ' ', '#'],
                    ['*', '#', '#', '#', '#', 'R'],
                    [' ', ' ', ' ', '#', ' ', ' '],
                    [' ', ' ', ' ', '#', ' ', ' ']]
    
        self.assertEqual(expected, q19._optimum_policy2d(grid, init, goal, cost))


class PatchedTestCase(unittest.TestCase):
    _assertAlmostEqual = unittest.TestCase.assertAlmostEqual
    def assertAlmostEqual(self, val0, val1, places=None, msg=None, delta=None):
        if type(val0) is not type(val1):
            print 'type of val0: ', type(val0), val0
            print 'type of val1: ', type(val1), val1
        assert type(val0) is type(val1)
        
        if type(val0) in [list, tuple]:
            assert len(val0) is len(val1)
            for val0, val1 in zip(val0, val1):
                self.assertAlmostEqual(val0, val1, places, msg, delta)
        else:
            self._assertAlmostEqual(val0, val1, places, msg, delta)


class HomeworkTest(PatchedTestCase):
    def test_homework(self):
        grid = [[0, 0, 0],
                [0, 0, 0]]
        goal = [0, len(grid[0]) - 1]
        expected_value = [[60.472, 37.193, 0.],
                          [63.503, 44.770, 37.193]]
        expected_policy = [['>', '>', '*'],
                           ['>', '^', '^']]
        
        value, policy = homework._stochastic_value(grid, goal)
        self.assertEqual(expected_policy, policy)
        self.assertAlmostEqual(expected_value, value, 3)

        grid = [[0, 1, 0],
                [0, 0, 0]]
        expected_value = [[94.041, 1000., 0.000],
                          [86.082, 73.143, 44.286]]
        expected_policy = [['v', ' ', '*'],
                           ['>', '>', '^']]
        
        value, policy = homework._stochastic_value(grid, goal)
        self.assertEqual(expected_policy, policy)
        self.assertAlmostEqual(expected_value, value, 3)

    def test_homework_larger_grid(self):
        grid = [[0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 1, 1, 0]]
        goal = [0, len(grid[0]) - 1]
        expected_value = [[57.903, 40.278, 26.066, 0.000],
                          [47.055, 36.572, 29.994, 27.270],
                          [53.172, 42.023, 37.775, 45.092],
                          [77.586, 1000., 1000., 73.546]]
        expected_policy = [['>', 'v', 'v', '*'],
                           ['>', '>', '^', '<'],
                           ['>', '^', '^', '<'],
                           ['^', ' ', ' ', '^']]
        
        value, policy = homework._stochastic_value(grid, goal)
        self.assertEqual(expected_policy, policy)
        self.assertAlmostEqual(expected_value, value, 3)


if __name__ == "__main__":
    unittest.main()
        