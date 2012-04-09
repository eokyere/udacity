import unittest
from lecture import hash_string

class TestHomework(unittest.TestCase):
    def test_split_string(self):
        self.assertEqual(10, hash_string('au', 12))
        self.assertEqual(11, hash_string('udacity', 12))
        self.assertEqual(0, hash_string('', 12))
        
if __name__ == "__main__":
    unittest.main()