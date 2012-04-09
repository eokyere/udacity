import unittest
from final import build_road, plan

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


class FinalPlanningTests(PatchedTestCase):
    def test_fast_left_lane(self):
        # Test Case 1 (FAST left lane)
        road = build_road(8, [100, 10, 1])
        lane_change_cost = 1.0 / 1000.0
        init = [len(road) - 1, 0]
        goal = [len(road) - 1, len(road[0]) - 1]
        cost = 1.244
        
        self.assertAlmostEqual(cost, plan(road=road, 
                                          lane_change_cost=lane_change_cost,
                                          goal=goal,
                                          init=init), 3)
    
    def test_realistic_road(self):
        # Test Case 2 (more realistic road)
        road = build_road(14, [80, 60, 40, 20])
        lane_change_cost = 1.0 / 100.0
        init = [len(road) - 1, 0]
        goal = [len(road) - 1, len(road[0]) - 1]
        cost = 0.293333333333
        
        self.assertAlmostEqual(cost, plan(road=road, 
                                          lane_change_cost=lane_change_cost,
                                          goal=goal,
                                          init=init), 10)

    def test_obstacles_included(self):
        # Test Case 3 (Obstacles included)
        road = [[50, 50, 50, 50, 50, 40, 0, 40, 50, 50, 50, 50, 50, 50, 50], # left lane: 50 km/h
                [40, 40, 40, 40, 40, 30, 20, 30, 40, 40, 40, 40, 40, 40, 40],
                [30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30]] # right lane: 30 km/h
        lane_change_cost = 1.0 / 500.0
        init = [len(road) - 1, 0]
        goal = [len(road) - 1, len(road[0]) - 1]
        cost = 0.355333333333
        
        self.assertAlmostEqual(cost, plan(road=road, 
                                          lane_change_cost=lane_change_cost,
                                          goal=goal,
                                          init=init), 10)

    def test_slalom(self):
        # Test Case 4 (Slalom)
        road = [[50, 50, 50, 50, 50, 40,  0, 40, 50, 50,  0, 50, 50, 50, 50], # left lane: 50 km/h
                [40, 40, 40, 40,  0, 30, 20, 30,  0, 40, 40, 40, 40, 40, 40],
                [30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30]] # right lane: 30 km/h
        lane_change_cost = 1.0 / 65.0
        init = [len(road) - 1, 0]
        goal = [len(road) - 1, len(road[0]) - 1]
        cost = 0.450641025641
        
        self.assertAlmostEqual(cost, plan(road=road, 
                                          lane_change_cost=lane_change_cost,
                                          goal=goal,
                                          init=init), 10)

if __name__ == "__main__":
    unittest.main()
