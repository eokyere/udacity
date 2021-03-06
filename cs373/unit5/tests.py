import unittest

import lecture
import hw2, hw3

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

class SmoothTest(unittest.TestCase):
    def test_smooth(self):
        pass


class HomeworkTest(PatchedTestCase):
    def test_cyclic_path_smoothing(self):
        testpath1 = [[0, 0],
                     [1, 0],
                     [2, 0],
                     [3, 0],
                     [4, 0],
                     [5, 0],
                     [6, 0],
                     [6, 1],
                     [6, 2],
                     [6, 3],
                     [5, 3],
                     [4, 3],
                     [3, 3],
                     [2, 3],
                     [1, 3],
                     [0, 3],
                     [0, 2],
                     [0, 1]]

        answer1 = [[0.5449300156668018, 0.47485226780102946],
                   [1.2230705677535505, 0.2046277687200752],
                   [2.079668890615267, 0.09810778721159963],
                   [3.0000020176660755, 0.07007646364781912],
                   [3.9203348821839112, 0.09810853832382399],
                   [4.7769324511170455, 0.20462917195702085],
                   [5.455071854686622, 0.4748541381544533],
                   [5.697264197153936, 1.1249625336275617],
                   [5.697263485026567, 1.8750401628534337],
                   [5.455069810373743, 2.5251482916876378],
                   [4.776929339068159, 2.795372759575895],
                   [3.92033110541304, 2.9018927284871063],
                   [2.999998066091118, 2.929924058932193],
                   [2.0796652780381826, 2.90189200881968],
                   [1.2230677654766597, 2.7953714133566603],
                   [0.544928391271399, 2.5251464933327794],
                   [0.3027360471605494, 1.875038145804603],
                   [0.302736726373967, 1.1249605602741133]]
        self.assertAlmostEqual(answer1, hw2.smooth(testpath1), places=4)

        testpath2 = [[1, 0], # Move in the shape of a plus sign
                     [2, 0],
                     [2, 1],
                     [3, 1],
                     [3, 2],
                     [2, 2],
                     [2, 3],
                     [1, 3],
                     [1, 2],
                     [0, 2], 
                     [0, 1],
                     [1, 1]]

        answer2 = [[1.239080543767428, 0.5047204351187283],
                   [1.7609243903912781, 0.5047216452560908],
                   [2.0915039821562416, 0.9085017167753027],
                   [2.495281862032503, 1.2390825203587184],
                   [2.4952805300504783, 1.7609262468826048],
                   [2.0915003641706296, 2.0915058211575475],
                   [1.7609195135622062, 2.4952837841027695],
                   [1.2390757942466555, 2.4952826072236918],
                   [0.9084962737918979, 2.091502621431358],
                   [0.5047183914625598, 1.7609219230352355],
                   [0.504719649257698, 1.2390782835562297],
                   [0.9084996902674257, 0.9084987462432871]]
        
        self.assertAlmostEqual(answer2, hw2.smooth(testpath2), 4)
        
    def test_constrained_smoothing(self):
        testpath1=[[0, 0], #fix
              [1, 0],
              [2, 0],
              [3, 0],
              [4, 0],
              [5, 0],
              [6, 0], #fix
              [6, 1],
              [6, 2],
              [6, 3], #fix
              [5, 3],
              [4, 3],
              [3, 3],
              [2, 3],
              [1, 3],
              [0, 3], #fix
              [0, 2],
              [0, 1]]
        testfix1 = [1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0]
        answer1 = [[0, 0],
                   [0.7938620981547201, -0.8311168821106101],
                   [1.8579052986461084, -1.3834788165869276],
                   [3.053905318597796, -1.5745863173084],
                   [4.23141390533387, -1.3784271816058231],
                   [5.250184859723701, -0.8264215958231558],
                   [6, 0],
                   [6.415150091996651, 0.9836951698796843],
                   [6.41942442687092, 2.019512290770163],
                   [6, 3],
                   [5.206131365604606, 3.831104483245191],
                   [4.142082497497067, 4.383455704596517],
                   [2.9460804122779813, 4.5745592975708105],
                   [1.768574219397359, 4.378404668718541],
                   [0.7498089205417316, 3.826409771585794],
                   [0, 3],
                   [-0.4151464728194156, 2.016311854977891],
                   [-0.4194207879552198, 0.9804948340550833]]
        
        self.assertAlmostEqual(answer1, hw3.smooth(testpath1, testfix1), 4)
        
        testpath2 = [[0, 0], # fix
                     [2, 0],
                     [4, 0], # fix
                     [4, 2],
                     [4, 4], # fix
                     [2, 4],
                     [0, 4], # fix
                     [0, 2]]
        testfix2 = [1, 0, 1, 0, 1, 0, 1, 0]
        answer2 = [[0, 0],
                   [2.0116767115496095, -0.7015439080661671],
                   [4, 0],
                   [4.701543905420104, 2.0116768147460418],
                   [4, 4],
                   [1.9883231877640861, 4.701543807525115],
                   [0, 4],
                   [-0.7015438099112995, 1.9883232808252207]]
        
        self.assertAlmostEqual(answer2, hw3.smooth(testpath2, testfix2), 4)

    def test_racetrack_control(self):
        pass

if __name__ == "__main__":
    unittest.main()
        