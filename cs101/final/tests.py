import unittest
import final

class TestFinal(unittest.TestCase):
    def test_unique(self):
        self.assertTrue(final.unique(1, 2, 3))
        self.assertFalse(final.unique(1, 0, 1))
        self.assertFalse(final.unique(7, 7, 7))

    def test_remove_prefix(self):
        self.assertEqual('udacity', final.remove_prefix('super-udacity'))
        self.assertEqual('counter-intelligence', 
                         final.remove_prefix('counter-counter-intelligence'))
        self.assertEqual('antigravity', final.remove_prefix('antigravity'))
        
    def test_collatz_steps(self):
        self.assertEqual(0, final.collatz_steps(1))
        self.assertEqual(1, final.collatz_steps(2))
        self.assertEqual(8, final.collatz_steps(6))
        self.assertEqual(25, final.collatz_steps(101))

    def test_list_explode(self):
        self.assertEqual([1, 1, 2, 2, 3, 3], final.explode_list([1, 2, 3], 2))
        self.assertEqual([], final.explode_list([1, 0, 1], 0))
        self.assertEqual(["super", "super", "super", "super", "super"],
                         final.explode_list(["super"], 5))
        
    def test_reverse_inde(self):
        winners_by_year = {
            1930: 'Uruguay', 1934: 'Italy', 1938: 'Italy', 1950: 'Uruguay',
            1954: 'West Germany', 1958: 'Brazil', 1962: 'Brazil', 1966: 'England',
            1970: 'Brazil', 1974: 'West Germany', 1978: 'Argentina',
            1982: 'Italy', 1986: 'Argentina', 1990: 'West Germany', 1994: 'Brazil',
            1998: 'France', 2002: 'Brazil', 2006: 'Italy', 2010: 'Spain' }
        
        wins_by_country = final.reverse_index(winners_by_year)
        
        self.assertEqual([1958, 1962, 1970, 1994, 2002],
                         sorted(wins_by_country['Brazil']))
        self.assertEqual([1966], wins_by_country['England'])

    def test_same_structure(self):
        self.assertTrue(final.same_structure(3, 7))
        self.assertTrue(final.same_structure([1, 0, 1], [2, 1, 2]))
        self.assertFalse(final.same_structure([1, [0], 1], [2, 5, 3]))
        self.assertTrue(final.same_structure([1, [2, [3, [4, 5]]]], 
                                             ['a', ['b', ['c', ['d', 'e']]]]))
        self.assertFalse(final.same_structure([1, [2, [3, [4, 5]]]], 
                                              ['a', ['b', ['c', ['de']]]]))
           

class TestFinalStarred(unittest.TestCase):
    def test_reachability(self):
        graph = {'a': ['b', 'c'], 
                 'b': ['a', 'c'], 
                 'c': ['b', 'd'], 
                 'd': ['a'], 
                 'e': ['a']}
        
        self.assertEqual(['a', 'b', 'c', 'd'],
                          sorted(final.reachable(graph, 'a')))
        self.assertEqual(['a', 'b', 'c', 'd'], 
                         sorted(final.reachable(graph, 'd')))
        self.assertEqual(['a', 'b', 'c', 'd', 'e'], 
                         sorted(final.reachable(graph, 'e')))
        
    def test_edit_distance(self):
        # Delete the 'a'
        self.assertEqual(1, final.edit_distance('audacity', 'udacity'))
        # Delete the 'a', replace the 'u' with 'U'
        self.assertEqual(2, final.edit_distance('audacity', 'Udacity'))
        # One deletion
        self.assertEqual(1, final.edit_distance('pete', 'peter'))
        # Five replacements
        self.assertEqual(5, final.edit_distance('peter', 'sarah'))
        
    def test_multi_lookup(self):

        index, graph = final.crawl_web('http://www.udacity.com/cs101x/final/multi.html')
        
#        for key in sorted(index.keys()):
#            print key, index[key]
#        print
        
        self.assertEqual(['http://www.udacity.com/cs101x/final/a.html',
                          'http://www.udacity.com/cs101x/final/b.html'], 
                         sorted(final.multi_lookup(index, ['Python'])))
        self.assertEqual(['http://www.udacity.com/cs101x/final/a.html'],
                         final.multi_lookup(index, ['Monty', 'Python']))
        self.assertEqual(['http://www.udacity.com/cs101x/final/b.html'],
                         final.multi_lookup(index, 
                                ['Python', 'programming', 'language']))
#        
        self.assertEqual(['http://www.udacity.com/cs101x/final/a.html',
                          'http://www.udacity.com/cs101x/final/b.html'],
                         sorted(final.multi_lookup(index, 
                                                   ['Thomas', 'Jefferson'])))
#        
        self.assertEqual(['http://www.udacity.com/cs101x/final/a.html'],
                         final.multi_lookup(index, 
                                            ['most', 'powerful', 'weapon']))
        

if __name__ == "__main__":
    unittest.main()