import unittest

import q08

class SearchTest(unittest.TestCase):
    def test_q_08(self):
        self.assertEqual([11, 4, 5], q08.search())
        
if __name__ == "__main__":
    unittest.main()
        