import unittest
import homework as hw

class TestHomework(unittest.TestCase):
    def test_q4(self):
        self.assertEqual('0.2998', '%.4f' % hw.q4())
        
    def test_q6(self):
        self.assertEqual('udacious', hw.q6())
        
    def test_q7(self):
        self.assertEqual(10, hw.q7('hehehehohohoooo'))
        self.assertEqual(-1, hw.q7('heheh'))
        
    def test_q8(self):
        self.assertEqual(14, hw.q8('zip files are zipped'))
        self.assertEqual(-1, hw.q8('zip files are compressed'))
        self.assertEqual(11, hw.q8('zippperzi pzipzipzip'))
    
    def test_q9(self):
        self.assertEqual('3', hw.q9(3.14159))
        self.assertEqual('28', hw.q9(27.63))

    def test_hours_in_weeks(self):
        self.assertEqual(24 * 7, hw.hours_in_weeks(1))
        self.assertEqual(24 * 14, hw.hours_in_weeks(2))

if __name__ == "__main__":
    unittest.main()