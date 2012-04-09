import unittest
import homework as hw

class TestHomework(unittest.TestCase):
    def test_split_string(self):
        out = ['This', 'is', 'a', 'test', 'of', 'the', 'string',
               'separation', 'code']
        source = 'This is a test-of the,string separation-code'
        splitlist = [' ', ',', '-']
        self.assertEqual(out, hw.split_string(source, splitlist))

        out = ['After', 'the', 'flood', 'all', 'the', 'colors', 'came', 'out']
        source = 'After  the flood  ...  all the colors came out'
        splitlist = [' ', ',', '-', '.']
        self.assertEqual(out, hw.split_string(source, splitlist))

if __name__ == "__main__":
    unittest.main()