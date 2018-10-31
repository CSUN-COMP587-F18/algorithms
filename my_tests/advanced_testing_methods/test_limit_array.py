
from arrays import limit
import unittest

class TestLimit(unittest.TestCase):

    def test_limit_with_minLim_none(self):
        self.assertListEqual(limit([1, 2, 3, 4, 5], None, 4), [1,2, 3, 4])
        self.assertListEqual(limit([1, 2, 3, 4, 5,6], None,2), [1,2])
        self.assertListEqual(limit([1, 2, 3, 4, 5,6,7], None, 6), [1, 2, 3, 4,5,6])
        self.assertListEqual(limit([1, 2, 3, 4, 5,6,7], None, 1), [1])
        self.assertListEqual(limit([1, 2, 3, 4, 5,6,7], None, 7), [1, 2, 3, 4,5,6,7])
        self.assertListEqual(limit([1, 2, 3, 4, 5,6,7], None, 3), [1, 2])
   
    def test_limit_with_maxLim_none(self):
        self.assertListEqual(limit([1, 2, 3, 4, 5], 1, None), [1,2, 3, 4,5])
        self.assertListEqual(limit([1, 2, 3, 4, 5,6], 3,None), [3,4],5,6)
        self.assertListEqual(limit([1, 2, 3, 4, 5,6,7], 6, None), [6,7])
        self.assertListEqual(limit([1, 2, 3, 4, 5,6,7], 3, None), [3,4,5,6,7])
        self.assertListEqual(limit([1, 2, 3, 4, 5,6,7,8,9], 6, None), [6,7,8,9])
        self.assertListEqual(limit([1, 2, 3, 4, 5,6,7], 2, None), [ 2,3,4,5,6,7])

    def test_limit_with_both_maxandminLim(self):
        self.assertListEqual(limit([1, 2, 3, 4, 5], 1, 4), [1,2, 3, 4])
        self.assertListEqual(limit([1, 2, 3, 4, 5,6], 2,4), [2,3,4])
        self.assertListEqual(limit([1, 2, 3, 4, 5,6,7], 1, 6), [1, 2, 3, 4,5,6])
        self.assertListEqual(limit([1, 2, 3, 4, 5,6,7], 4, 7), [4,5,6,7])
        self.assertListEqual(limit([1, 2, 3, 4, 5,6,7], 2, 3), [ 2, 3])
        self.assertListEqual(limit([1, 2, 3, 4, 5,6,7], None, None), [1,2,3,4,5,6,7])




