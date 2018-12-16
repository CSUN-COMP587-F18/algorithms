from unittest import TestCase
from delete_nth import delete_nth_naive, delete_nth
from flatten import flatten, flatten_iter
from limit import limit
from longest_non_repeat import longest_non_repeat_v1,longest_non_repeat_v2
from max_ones_index import max_ones_index
from missing_ranges import missing_ranges
from move_zeros import move_zeros
from n_sum import n_sum
from plus_one import plus_one_v1, plus_one_v2, plus_one_v3
from rotate import rotate_v1, rotate_v2, rotate_v3
from summarize_ranges import summarize_ranges
from three_sum import three_sum
from top_1 import top_1
from two_sum import two_sum
from trimmean import trimmean

from array import*

'''
[0.00794 s] killed by test_delete_nth (test_mutation_array.DeleteNthMutationTest)
[*] Mutation score [0.16896 s]: 100.0%
   - all: 8
   - killed: 8 (100.0%)
   - survived: 0 (0.0%)
   - incompetent: 0 (0.0%)
   - timeout: 0 (0.0%)
'''

class DeleteNthMutationTest(TestCase):
    def test_delete_nth(self):
        self.assertListEqual(delete_nth([1,2,3,1,2,1,2,3],2), [1,2,3,1,2,3])


class DeleteNthNaiveMutationTest(TestCase):
    def test_delete_nth_naive(self):
        self.assertListEqual(delete_nth_naive([1,2,3,1,2,1,2,3],2), [1,2,3,1,2,3])

"""====================================================================================="""

'''

[0.00961 s] killed by test_two_sum (test_mutation_array.TwoSumMutationTest)
[*] Mutation score [0.10419 s]: 100.0%
   - all: 3
   - killed: 3 (100.0%)
   - survived: 0 (0.0%)
   - incompetent: 0 (0.0%)
   - timeout: 0 (0.0%)
'''

class TwoSumMutationTest(TestCase):
    def test_two_sum(self):
        self.assertEqual(two_sum([2, 7, 11, 15],9), (0, 1))
"""====================================================================================="""

'''
[0.00882 s] killed by test_move_zeros (test_mutation_array.MoveZerosMutationTest)
[*] Mutation score [0.17368 s]: 100.0%
   - all: 9
   - killed: 6 (66.7%)
   - survived: 0 (0.0%)
   - incompetent: 3 (33.3%)
   - timeout: 0 (0.0%)
'''
class MoveZerosMutationTest(TestCase):
    def test_move_zeros(self):
        self.assertListEqual(move_zeros([1, 0, 1, 2, 0, 1, 3, "a"]),[1, 1, 2, 1, 3, "a", 0, 0])


class MoveZerosEmptyMutationTest(TestCase):
    def test_move_zeros_empty(self):
        self.assertListEqual(move_zeros([]),[])

"""====================================================================================="""
'''
[0.01020 s] killed by test_plus_one_v1 (test_mutation_array.PlusONeV1MutationTest)
[*] Mutation score [11.36243 s]: 90.8%
   - all: 65
   - killed: 57 (87.7%)
   - survived: 6 (9.2%)
   - incompetent: 0 (0.0%)
   - timeout: 2 (3.1%)
'''

class PlusONeV1MutationTest(TestCase):
    def test_plus_one_v1(self):
        self.assertListEqual(plus_one_v1([6]),[7])
        self.assertListEqual(plus_one_v1([0]),[1])
        self.assertListEqual(plus_one_v1([1, 0, 9]), [1, 1, 0])


class PlusONeV2MutationTest(TestCase):
    def test_plus_one_v2(self):
        self.assertListEqual(plus_one_v2([4]),[5])
        self.assertListEqual(plus_one_v2([0]),[1])
        self.assertListEqual(plus_one_v2([1, 0, 9]), [1, 1, 0])

class PlusONeV3MutationTest(TestCase):
    def test_plus_one_v3(self):
        self.assertListEqual(plus_one_v3([3,4,8]),[3,4,9])
        self.assertListEqual(plus_one_v3([0]),[1])
        self.assertListEqual(plus_one_v3([1, 0, 9]), [1, 1, 0])

"""====================================================================================="""

'''
[0.01008 s] killed by test_summarize (test_mutation_array.SummarizeRangesMutationTest)
[*] Mutation score [15.52528 s]: 88.0%
   - all: 25
   - killed: 19 (76.0%)
   - survived: 3 (12.0%)
   - incompetent: 0 (0.0%)
   - timeout: 3 (12.0%)
'''

class SummarizeRangesMutationTest(TestCase):
    def test_summarize(self):
        self.assertListEqual(summarize_ranges([0, 1, 2, 4, 5, 7]),[(0, 2), (4, 5), (7, 7)])



class SummarizeRangesEmptyMutationTest(TestCase):
    def test_summarize_empty(self):
        self.assertListEqual(summarize_ranges([]),[])

"""====================================================================================="""

'''
[0.00971 s] killed by test_trimmean (test_mutation_array.TrimmeanMutationTest)
[*] Mutation score [0.29086 s]: 84.6%
   - all: 13
   - killed: 11 (84.6%)
   - survived: 2 (15.4%)
   - incompetent: 0 (0.0%)
   - timeout: 0 (0.0%)
'''

class TrimmeanMutationTest(TestCase):
    def test_trimmean(self):
        self.assertEqual(trimmean([1,2,3,4,5,6,7,8,9,10],20), 5.5)
        self.assertEqual(trimmean([1,2,3,4,5],10), 3.0)
        self.assertEqual(trimmean([0,1],10), 0.5)
        self.assertEqual(trimmean([0],20), 0.0)
        self.assertEqual(trimmean([0,-1],10), -0.5)

"""====================================================================================="""
'''
[0.00965 s] killed by test_missing_ranges_empty (test_mutation_array.MissingRangesEmptyMutationTest)
[*] Mutation score [0.30568 s]: 85.7%
   - all: 14
   - killed: 12 (85.7%)
   - survived: 2 (14.3%)
   - incompetent: 0 (0.0%)
   - timeout: 0 (0.0%)
'''   

class MissingRangesMutationTest(TestCase):
    def test_missing_ranges(self):
        self.assertListEqual(missing_ranges([3, 5], 1,10),[(1, 2), (4, 4), (6, 10)])
        self.assertListEqual(missing_ranges([3, 5, 10, 11, 12, 15, 19], 0,20),[(0, 2), (4, 4), (6, 9),
                              (13, 14), (16, 18), (20, 20)])



class MissingRangesEmptyMutationTest(TestCase):
    def test_missing_ranges_empty(self):
        self.assertListEqual(missing_ranges([], 0,0),[(0, 0)])

"""====================================================================================="""

'''
[0.00850 s] killed by test_max_ones_index (test_mutation_array.MaxOnesIndexMutationTest)
[*] Mutation score [0.34304 s]: 80.0%
   - all: 20
   - killed: 16 (80.0%)
   - survived: 4 (20.0%)
   - incompetent: 0 (0.0%)
   - timeout: 0 (0.0%)
'''

class MaxOnesIndexMutationTest(TestCase):
    def test_max_ones_index(self):
        self.assertEqual(max_ones_index([1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1]), 3)


class MaxOnesIndexEmptyMutationTest(TestCase):
    def test_max_ones_index_empty(self):
        self.assertEqual(max_ones_index([]), -1)
"""====================================================================================="""




'''
[*] Mutation score [11.86403 s]: 70.4%
   - all: 82
   - killed: 55 (67.1%)
   - survived: 24 (29.3%)
   - incompetent: 1 (1.2%)
   - timeout: 2 (2.4%)
'''

class NSumMutationTest(TestCase):
    def test_n_sum(self):
        self.assertListEqual(n_sum(4,[1, 0, -1, 0, -2, 2] ,0),[[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]])
        self.assertListEqual(n_sum(2, [-3, 5, 2, 3, 8, -9], 6), []) 



class NsumEmptyMutationTest(TestCase):
    def test_n_sum_empty(self):
        self.assertListEqual(n_sum(4,[] ,0),[])
        self.assertListEqual(n_sum(0,[] ,0),[])

"""====================================================================================="""

'''
[*] Mutation score [0.84751 s]: 71.4%
   - all: 36
   - killed: 25 (69.4%)
   - survived: 10 (27.8%)
   - incompetent: 1 (2.8%)
   - timeout: 0 (0.0%)
'''
class RotateV1MutationTest(TestCase):
    def test_rotate_v1(self):
        self.assertListEqual(rotate_v1([1, 4], 1),[4,1])
        self.assertListEqual(rotate_v1([1,2,3,4,5,6,7], 3),[5,6,7,1,2,3,4])
        self.assertListEqual(rotate_v1([0], 1),[0])
        self.assertListEqual(rotate_v1([20, 30, 40, 50, 60, 70, 80], 7),
                                       [20, 30, 40, 50, 60, 70, 80])
        self.assertListEqual(rotate_v1([5, 6,7], 1),[7,5,6])


class RotateV2MutationTest(TestCase):
    def test_rotate_v2(self):
        self.assertListEqual(rotate_v2([1], 3),[1])
        self.assertListEqual(rotate_v2([0], 1),[0])
        self.assertListEqual(rotate_v2([20, 30, 40, 50, 60, 70, 80], 7),
                                       [20, 30, 40, 50, 60, 70, 80])

class RotateV3MutationTest(TestCase):
    def test_rotate_v3(self):
        self.assertListEqual(rotate_v3([1], 3),[1])
        self.assertListEqual(rotate_v3([0], 1),[0])
        self.assertListEqual(rotate_v3([20, 30, 40, 50, 60, 70, 80], 7),
                                       [20, 30, 40, 50, 60, 70, 80])
"""====================================================================================="""


'''
[0.01039 s] killed by test_three_sum (test_mutation_array.ThreeSumMutationTest)
[*] Mutation score [11.15286 s]: 68.5%
   - all: 54
   - killed: 35 (64.8%)
   - survived: 17 (31.5%)
   - incompetent: 0 (0.0%)
   - timeout: 2 (3.7%)
'''

class ThreeSumMutationTest(TestCase):
    def test_three_sum(self):
        self.assertEqual(three_sum([-1, 0, 1, 2, -1, -4]),{(-1, 0, 1),(-1, -1, 2)})
      

"""====================================================================================="""

'''				
[0.01110 s] killed by test_top_1 (test_mutation_array.Top1MutationTest)
[*] Mutation score [0.23233 s]: 66.7%
   - all: 9
   - killed: 6 (66.7%)
   - survived: 3 (33.3%)
   - incompetent: 0 (0.0%)
   - timeout: 0 (0.0%)
'''

class Top1MutationTest(TestCase):
    def test_top_1(self):
        self.assertListEqual(top_1([1, 1, 2, 2, 3, 4]), [1, 2])
        self.assertListEqual(top_1([1, 1]), [1])
        self.assertListEqual(top_1([1, 1, -2,-2]), [1, -2])
        self.assertListEqual(top_1([1, 1, 0,0,121,121,121]), [121])
        self.assertListEqual(top_1([0]), [0])
        self.assertListEqual(top_1([111,111,111,1112,1112,1112,0,0,0,1,1,1,]), [111,1112,0,1])
        self.assertListEqual(top_1([-4,-4,1,1,2,2,3,3,-4]), [-4])



"""====================================================================================="""

'''
[0.01056 s] killed by test_top_1 (test_mutation_array.Top1MutationTest)
[*] Mutation score [0.23019 s]: 66.7%
   - all: 9
   - killed: 6 (66.7%)
   - survived: 3 (33.3%)
   - incompetent: 0 (0.0%)
   - timeout: 0 (0.0%)
'''

class LimitMutationTest(TestCase):
    def test_limit(self):
        self.assertListEqual(limit([1,2,3,4,5], None, 3), [1,2,3])
        self.assertListEqual(limit([6, 7, 8, 9, 10], None, 9), [6, 7, 8, 9])
        self.assertListEqual(limit([1, 2, 3, 4, 5], 2), [2, 3, 4, 5])
        self.assertListEqual(limit([0,1,2], 2), [2])



class LimitEmptyMutationTest(TestCase):
    def test_limit_empty(self):
        self.assertListEqual(limit([], None, 3), [])

"""====================================================================================="""

class LongestNonRepeatV1MutationTest(TestCase):
    def test_longest_non_repeat_v1(self):
        self.assertEqual(longest_non_repeat_v1("abcabcbb"), 3)
        self.assertEqual(longest_non_repeat_v1(""), 0)
        self.assertEqual(longest_non_repeat_v1("qqq"), 1)
        self.assertEqual(longest_non_repeat_v1("abad"), 3)
        self.assertEqual(longest_non_repeat_v1("abcdeafa"), 6)

class LongestNonRepeatV2MutationTest(TestCase):
    def test_longest_non_repeat_v1(self):
        self.assertEqual(longest_non_repeat_v2(""), 0)
        self.assertEqual(longest_non_repeat_v2("abcabcbb"), 3)
        self.assertEqual(longest_non_repeat_v2("qqq"), 1)
        self.assertEqual(longest_non_repeat_v2("abad"), 3)
        self.assertEqual(longest_non_repeat_v2("abcdeafa"), 6)



"""====================================================================================="""








