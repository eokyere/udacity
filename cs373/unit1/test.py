from __future__ import division
import unittest
import testutil

import lecture as lt
from homework import Robot

from lecture import R, G


class HomeworkTests(testutil.PatchedTestCase):
    def test_values_0(self):
        expected = [[0.0, 0.0, 0.0],
                    [0.0, 1.0, 0.0],
                    [0.0, 0.0, 0.0]]
        
        colors=[['green', 'green', 'green'],
                ['green', 'red', 'green'],
                ['green', 'green', 'green']]
        
        robot = Robot(world=colors)
        robot.sensor = 1.0
        robot.movement = 1.0
        p = robot._p(len(colors), len(colors[0]))
        actual = robot.localize(p=p, 
                                measurements=['red'], 
                                motions=[0, 0])
        self.assertAlmostEqual(expected, actual)

    def test_values_1(self):
        expected = [[0.0, 0.0, 0.0],
                    [0.0, 0.5, 0.5],
                    [0.0, 0.0, 0.0]]
        colors=[['green', 'green', 'green'],
                ['green', 'red', 'red'],
                ['green', 'green', 'green']]
        
        robot = Robot(world=colors)
        robot.sensor = 1.0
        robot.movement = 1.0
        p = robot._p(len(colors), len(colors[0]))
        actual = robot.localize(p=p, measurements=['red'], motions=[[0, 0]])
        self.assertAlmostEqual(expected, actual)

    def test_values_2(self):
        expected = [[0.06666, 0.06666, 0.06666],
                    [0.06666, 0.26666, 0.26666],
                    [0.06666, 0.06666, 0.06666]]
        
        colors=[['green', 'green', 'green'],
                ['green', 'red', 'red'],
                ['green', 'green', 'green']]
        
        robot = Robot(world=colors)
        robot.sensor = 0.8
        robot.movement = 1.0
        actual = robot.localize(measurements=['red'], motions=[[0, 0]])
        self.assertAlmostEqual(expected, actual, places=4)

    def test_values_3(self):
        expected = [[0.03333, 0.03333, 0.03333],
                    [0.13333, 0.13333, 0.53333],
                    [0.03333, 0.03333, 0.03333]]

        colors = [['green', 'green', 'green'],
                  ['green', 'red', 'red'],
                  ['green', 'green', 'green']]
        
        robot = Robot(world=colors)
        robot.sensor = 0.8
        robot.movement = 1.0
        p = robot._p(len(colors), len(colors[0]))
        actual = robot.localize(p=p, 
                                measurements=['red', 'red'], 
                                motions=[[0, 0], [0, 1]])
        self.assertAlmostEqual(expected, actual, places=4)
        
    def test_values_4(self):
        expected = [[0.0, 0.0, 0.0],
                    [0.0, 0.0, 1.0],
                    [0.0, 0.0, 0.0]]

        colors = [['green', 'green', 'green'],
                  ['green', 'red', 'red'],
                  ['green', 'green', 'green']]
        
        robot = Robot(world=colors)
        robot.sensor = 1.0
        robot.movement = 1.0
        p = robot._p(len(colors), len(colors[0]))
        actual = robot.localize(p=p, 
                                measurements=['red', 'red'], 
                                motions=[[0, 0], [0, 1]])
        self.assertAlmostEqual(expected, actual, places=4)

    def test_values_5(self):
        expected = [[0.02898, 0.02898, 0.02898],
                    [0.07246, 0.28985, 0.46376],
                    [0.02898, 0.02898, 0.02898]]

        colors = [['green', 'green', 'green'],
                  ['green', 'red', 'red'],
                  ['green', 'green', 'green']]
        
        robot = Robot(world=colors)
        robot.sensor = 0.8
        robot.movement = 0.5
        p = robot._p(len(colors), len(colors[0]))
        actual = robot.localize(p=p, 
                                measurements=['red', 'red'], 
                                motions=[[0, 0], [0, 1]])
        self.assertAlmostEqual(expected, actual, places=4)

    def test_values_6(self):
        expected = [[0.0, 0.0, 0.0],
                    [0.0, 0.33333, 0.66666],
                    [0.0, 0.0, 0.0]]

        colors = [['green', 'green', 'green'],
                  ['green', 'red', 'red'],
                  ['green', 'green', 'green']]
        
        robot = Robot(world=colors)
        robot.sensor = 1.0
        robot.movement = 0.5
        p = robot._p(len(colors), len(colors[0]))
        actual = robot.localize(p=p, 
                                measurements=['red', 'red'], 
                                motions=[[0, 0], [0, 1]])
        self.assertAlmostEqual(expected, actual, places=4)

    def test_values_7(self):
        expected = [[0.01105, 0.02464, 0.06799, 0.04472, 0.024651],
                    [0.00715, 0.01017, 0.08696, 0.07988, 0.00935],
                    [0.00739, 0.00894, 0.11272, 0.35350, 0.04065],
                    [0.00910, 0.00715, 0.01434, 0.04313, 0.03642]]

        colors = [['red', 'green', 'green', 'red','red'],
                  ['red', 'red', 'green', 'red', 'red'],
                  ['red', 'red', 'green', 'green', 'red'],
                  ['red', 'red', 'red', 'red', 'red']]
        
        robot = Robot(world=colors)
        robot.sensor = 0.7
        robot.movement = 0.8
        p = robot._p(len(colors), len(colors[0]))
        actual = robot.localize(p=p, 
                                measurements=['green', 'green', 'green', 
                                              'green', 'green'], 
                                motions=[[0, 0], [0, 1], [1, 0], [1, 0], 
                                         [0, 1]])
        self.assertAlmostEqual(expected, actual, places=4)

    def test_values_8(self):
        expected = [[0.0, 0.0, 0.0],
                    [1.0, 0.0, 0.0],
                    [0.0, 0.0, 0.0]]

        colors = [['green', 'green', 'green'],
                  ['red', 'red', 'green'],
                  ['green', 'green', 'green']]
        
        robot = Robot(world=colors)
        robot.sensor = 1.0
        robot.movement = 1.0
        p = robot._p(len(colors), len(colors[0]))
        actual = robot.localize(p=p, 
                                measurements=['red', 'red'], 
                                motions=[[0, 0], [0, -1]])
        self.assertAlmostEqual(expected, actual, places=1)


    def test_values_9(self):
        expected = [[0.0, 1.0, 0.0],
                    [0.0, 0.0, 0.0],
                    [0.0, 0.0, 0.0]]

        colors = [['green', 'red', 'green'],
                  ['green', 'red', 'green'],
                  ['green', 'green', 'green']]
        
        robot = Robot(world=colors)
        robot.sensor = 1.0
        robot.movement = 1.0
        p = robot._p(len(colors), len(colors[0]))
        actual = robot.localize(p=p, 
                                measurements=['red', 'red'], 
                                motions=[[0, 0], [-1, 0]])
        self.assertAlmostEqual(expected, actual, places=1)



class WordTests(unittest.TestCase):
    def setUp(self):
        self.world = [[1, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0]]
        
    def test_stand_still(self):
        bot = Robot(world=self.world)
        self.assertEqual([[1, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0]],
                         bot.move(self.world, [0, 0]))
    
    def test_move_up(self):
        bot = Robot(world=self.world)
        self.assertEqual([[0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0],
                          [1, 0, 0, 0, 0]], 
                         bot.move(self.world, [-1, 0]))
        
    def test_move_down(self):
        bot = Robot(world=self.world)
        self.assertEqual([[0, 0, 0, 0, 0],
                          [1, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0]], 
                         bot.move(self.world, [1, 0]))
        
    def test_move_left(self):
        bot = Robot(world=self.world)
        self.assertEqual([[0, 0, 0, 0, 1],
                          [0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0]], 
                         bot.move(self.world, [0, -1]))
        
    def test_move_right(self):
        bot = Robot(world=self.world)
        self.assertEqual([[0, 1, 0, 0, 0],
                          [0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0]], 
                         bot.move(self.world, [0, 1]))

    def test_move_up_left(self):
        bot = Robot(world=self.world)
        self.assertEqual([[0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 1]], 
                         bot.move(self.world, [-1, -1]))

    def test_move_down_right(self):
        bot = Robot(world=self.world)
        self.assertEqual([[0, 0, 0, 0, 0],
                          [0, 1, 0, 0, 0],
                          [0, 0, 0, 0, 0]], 
                         bot.move(self.world, [1, 1]))

    def test_multiple_motions(self):
        bot = Robot(world=self.world)
        self.assertEqual(self.world, 
                         bot.move(self.world, 
                                  [[1, 0], [0, 1], [-1, 0], [0, -1]]))




class LectureTests(testutil.PatchedTestCase):
    def test_sense(self):
        expected = [0.1111, 0.3333, 0.3333, 0.1111, 0.1111]
        n = 5
        p = [1 / n ] * n
        self.assertAlmostEqual(expected, lt.sense(p, R), places=4)

    def test_sense_all(self):
        expected = [0.2000, 0.2000, 0.2000, 0.2000, 0.2000]
        n = 5
        p = [1 / n ] * n
        self.assertAlmostEqual(expected, lt.sense_all(p, [R, G]))

    def test_move(self):
        xs = [1, 0, 0, 0, 0]
        self.assertAlmostEqual([0, 1, 0, 0, 0], lt.move(xs, 1), places=0)
        self.assertAlmostEqual([0, 0, 1, 0, 0], lt.move(xs, 2), places=0)
        self.assertAlmostEqual([0, 0, 0, 1, 0], lt.move(xs, 3), places=0)
        self.assertAlmostEqual([0, 0, 0, 0, 1], lt.move(xs, 4), places=0)
        self.assertAlmostEqual([1, 0, 0, 0, 0], lt.move(xs, 5), places=0)
    
    def test_move1(self):
        expected = [0.0000, 0.1000, 0.8000, 0.1000, 0.0000]
        p = [0, 1, 0, 0, 0]
        self.assertAlmostEqual(expected, lt.move1(p, 1), places=4)
        
        expected = [0.2000, 0.2000, 0.2000, 0.2000, 0.2000]
        p = [0.2, 0.2, 0.2, 0.2, 0.2] 
        self.assertAlmostEqual(expected, lt.move1(p, 2), places=4)
        
    def test_xmove(self):
        expected = [0.0000, 0.1000, 0.8000, 0.1000, 0.0000]
        p = [0, 1, 0, 0, 0]
        U = 1
        p = lt.xmove(p, U, 1, 1, 0.8, 0.1, 0.1)
        self.assertAlmostEqual(expected, p, places=4)

    def test_move_limit_after_200_iterations(self):
        expected = [0.2000, 0.2000, 0.2000, 0.2000, 0.2000]
        p = [0, 1, 0, 0, 0]
        U = 1
        for i in range(200):
            p = lt.xmove(p, U, 1, 0, 0.8, 0.1, 0.1)
        self.assertAlmostEqual(expected, p, places=4)
        
    def test_localize(self):
        n = 5
        p = [1 / n ] * n
        
        expected = [0.2116, 0.1516, 0.0811, 0.1684, 0.3874]
        result = lt.localize(p, [R, G], [1, 1])
        self.assertAlmostEqual(expected, result, places=4)

        expected = [0.0788, 0.0753, 0.2247, 0.4329, 0.1882] 
        result = lt.localize(p, [R, R], [1, 1])
        self.assertAlmostEqual(expected, result, places=4)

if __name__ == "__main__":
    unittest.main()