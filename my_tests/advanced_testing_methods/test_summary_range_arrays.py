"Basically returns the summary of the ranges of the values in the array"

from algorithms.arrays import summarize_ranges

import unittest

class TestRangeSummary(unittest.TestCase):

    def test_summarize(self):

        self.assertListEqual(summarize_ranges([0,1,2]),
                             [(0, 2)])
        self.assertListEqual(summarize_ranges([-4, -3, -2, -1, 0,1,2,3,4]),
                             [(-4, 4)])
        self.assertListEqual(summarize_ranges([0, 1, 2, 4, 5, 7]),
                             [(0, 2), (4, 5), (7, 7)])
        self.assertListEqual(summarize_ranges([1,1,1,1,1,2,3]),
                             [(1,3)])
        self.assertListEqual(summarize_ranges([0,0,0,0,0,0,0,0]),
                             [(0, 0)])
        self.assertListEqual(summarize_ranges([-1,1,-1,1]),
                             [(-1, 1)])
        self.assertListEqual(summarize_ranges([0, 1, 2, 4, 5, 7,8,9]),
                             [(0, 2), (4, 5), (7, 8),(9,9)])
                             

if __name__ == '__main__':

    unittest.main()