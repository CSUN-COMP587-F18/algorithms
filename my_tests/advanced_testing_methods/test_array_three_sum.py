"""
Given an array S of n integers, are there elements a, b, c in S
such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.
Note: The solution set must not contain duplicate triplets.
For example, given array S = [-1, 0, 1, 2, -1, -4],
A solution set is:
{
  (-1, 0, 1),
  (-1, -1, 2)
}
"""
from arrays import three_sum
import unittest

class TestDuplicateTriplets(unittest.TestCase):

    def test_duplicate_triplets(self):

        self.assertSetEqual(three_sum([-1, 0, 1, 2, -1, -4]),
                            {(-1, 0, 1), (-1, -1, 2)})

        self.assertSetEqual(three_sum([-1, 1, 0, 2,-2,0]),
                            {(-1, 1, 0),(2,-2,0) })
        self.assertSetEqual(three_sum([1, 2, -3, 0,1,0]),
                            {(1, 2, -3) })
        self.assertSetEqual(three_sum([-6, 0, -6, 7,-1,-6]),
                            {(7, -1, -6) })
        self.assertSetEqual(three_sum([-100, 100, 0, 2,2,-4]),
                            {(-100, 100, 0),(2,2,-4) })
        self.assertSetEqual(three_sum([-1, 1, -1, 2,-2,2]),
                            {(-1, -1, 2) })
        self.assertSetEqual(three_sum([0, 0, 0, 8,-8,0]),
                            {(0, 0, 0),(8,-8,0) })
        self.assertSetEqual(three_sum([-3, -1, 4, 2,-4,0,1,9]),
                            {(-3, -1, 4),(-4,4,0),(1,-1,0),(-3,1,2) })
        