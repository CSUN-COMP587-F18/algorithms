from unittest import TestCase
from add_bitwise_operator import add_bitwise
from find_difference import find_difference
from count_ones import count_ones_recur, count_ones_iter
from find_missing_number import find_missing_number , find_missing_number2
from flip_bit_longest_sequence import flip_bit_longest_seq
from has_alternative_bit import has_alternative_bit, has_alternative_bit_fast
from insert_bit  import insert_one_bit , insert_mult_bits
from power_of_two import is_power_of_two
from remove_bit import remove_bit
from reverse_bits import reverse_bits
from single_number import single_number
from single_number2 import single_number2
from single_number3 import single_number3
from subsets import subsets
from swap_pair import swap_pair



'''
[0.00846 s] killed by test_mul (test_mutation_bit.AddBitwiseMutationTest)
[*] Mutation score [5.10911 s]: 100.0%
   - all: 5
   - killed: 4 (80.0%)
   - survived: 0 (0.0%)
   - incompetent: 0 (0.0%)
   - timeout: 1 (20.0%)
'''
class AddBitwiseMutationTest(TestCase):
    def test_mul(self):
        self.assertEqual(add_bitwise(2, 3), 5)
"""==========================================================================="""
'''
[*] Mutation score [15.36466 s]: 100.0%
   - all: 15
   - killed: 12 (80.0%)
   - survived: 0 (0.0%)
   - incompetent: 0 (0.0%)
   - timeout: 3 (20.0%)
'''
class CountOnesRecursiveMutationTest(TestCase):
    def test_count_r(self):
        self.assertEqual(count_ones_recur(11), 3)

class CountOnesIterativeMutationTest(TestCase):
    def test_count_it(self):
        self.assertEqual(count_ones_iter(11), 3)

"""==========================================================================="""
'''
[0.00861 s] killed by test_remove (test_mutation_bit.RemoveMutationTest)
[*] Mutation score [0.18681 s]: 100.0%
   - all: 10
   - killed: 10 (100.0%)
   - survived: 0 (0.0%)
   - incompetent: 0 (0.0%)
   - timeout: 0 (0.0%)
'''
class RemoveMutationTest(TestCase):
    def test_remove(self):
        self.assertEqual(remove_bit(21, 2), 9)
        self.assertEqual(remove_bit(21, 4), 5)
        self.assertEqual(remove_bit(21, 0), 10)
"""==========================================================================="""
'''
[0.00919 s] killed by test_single3 (test_mutation_bit.SingleNumber3MutationTest)
[*] Mutation score [0.23736 s]: 100.0%
   - all: 11
   - killed: 11 (100.0%)
   - survived: 0 (0.0%)
   - incompetent: 0 (0.0%)
   - timeout: 0 (0.0%)
'''

class SingleNumber3MutationTest(TestCase):
    def test_single3(self):
        self.assertEqual(single_number3([1, 2, 1, 3, 2, 5]), [3,5])

"""==========================================================================="""
'''
[0.01029 s] killed by test_single (test_mutation_bit.SingleNumberMutationTest)
[*] Mutation score [0.05646 s]: 100.0%
   - all: 2
   - killed: 2 (100.0%)
   - survived: 0 (0.0%)
   - incompetent: 0 (0.0%)
   - timeout: 0 (0.0%)
'''
class SingleNumberMutationTest(TestCase):
    def test_single(self):
        self.assertEqual(single_number([1,1,2,3,3,4,4,5,5]), 2)
        self.assertEqual(single_number([1,1,2,2,3,3,4,4,5,5]), 0)


"""==========================================================================="""
'''
[0.00962 s] killed by test_reverse (test_mutation_bit.ReverseBitMutationTest)
[*] Mutation score [5.26122 s]: 100.0%
   - all: 15
   - killed: 14 (93.3%)
   - survived: 0 (0.0%)
   - incompetent: 0 (0.0%)
   - timeout: 1 (6.7%)
'''
class ReverseBitMutationTest(TestCase):
    def test_reverse(self):
        self.assertEqual(reverse_bits(43261596), 964176192)
       
"""==========================================================================="""

'''
[0.00846 s] killed by test_is_power (test_mutation_bit.IsPowerOfTwoPositiveMutationTest)
[*] Mutation score [0.15485 s]: 100.0%
   - all: 8
   - killed: 8 (100.0%)
   - survived: 0 (0.0%)
   - incompetent: 0 (0.0%)
   - timeout: 0 (0.0%)
'''
class IsPowerOfTwoPositiveMutationTest(TestCase):
    def test_is_power(self):
        self.assertEqual(is_power_of_two(2), True)
        self.assertEqual(is_power_of_two(3), False)
        self.assertEqual(is_power_of_two(0), False)
        self.assertEqual(is_power_of_two(16), True)
        self.assertEqual(is_power_of_two(4), True)
        self.assertEqual(is_power_of_two(1), True)

"""==========================================================================="""

'''
[0.00899 s] killed by test_find_diff (test_mutation_bit.FindDifferenceMutationTest)
[*] Mutation score [0.08102 s]: 100.0%
   - all: 3
   - killed: 2 (66.7%)
   - survived: 0 (0.0%)
   - incompetent: 1 (33.3%)
   - timeout: 0 (0.0%)
'''
class FindDifferenceMutationTest(TestCase):
    def test_find_diff(self):
        self.assertEqual(find_difference("aa", "aab"), "b")

"""==========================================================================="""

'''
[0.00863 s] killed by test_find_number (test_mutation_bit.FindMissingNumbersMutationTest)
[*] Mutation score [0.28370 s]: 92.9%
   - all: 14
   - killed: 13 (92.9%)
   - survived: 1 (7.1%)
   - incompetent: 0 (0.0%)
   - timeout: 0 (0.0%)
'''

class FindMissingNumbersMutationTest(TestCase):
    def test_find_number(self):
        self.assertEqual(find_missing_number([1]), 0)
        self.assertEqual(find_missing_number([0,1,2,3,4,5,6]), 7)


class FindMissingNummbers2MutationTest(TestCase):
    def test_find_number2(self):
        self.assertEqual(find_missing_number2([1]), 0)
        self.assertEqual(find_missing_number2([0]), 1)
        self.assertEqual(find_missing_number2([2]), -1)
        self.assertEqual(find_missing_number2([-1]), 2)
        self.assertEqual(find_missing_number2([0,1,2,3,4,5,6]), 7)
"""==========================================================================="""
'''
[0.01010 s] killed by test_flip_bit (test_mutation_bit.FlipBitLongestSequenceMutationTest)
[*] Mutation score [5.42960 s]: 85.7%
   - all: 28
   - killed: 23 (82.1%)
   - survived: 4 (14.3%)
   - incompetent: 0 (0.0%)
   - timeout: 1 (3.6%)
'''
class FlipBitLongestSequenceMutationTest(TestCase):
    def test_flip_bit(self):
        self.assertEqual(flip_bit_longest_seq(1705), 4)
        self.assertEqual(flip_bit_longest_seq(0), 1)
        self.assertEqual(flip_bit_longest_seq(1), 2)
        self.assertEqual(flip_bit_longest_seq(4), 2)
"""==========================================================================="""
'''
[0.00802 s] killed by test_has_alt_fast (test_mutation_bit.HasAlternativeBitFastMutationTest)
[*] Mutation score [0.49146 s]: 83.3%
   - all: 30
   - killed: 25 (83.3%)
   - survived: 5 (16.7%)
   - incompetent: 0 (0.0%)
   - timeout: 0 (0.0%)
'''
class HasAlternativeBitMutationTest(TestCase):
    def test_has_alt(self):
        self.assertEqual(has_alternative_bit(5), True)
        self.assertEqual(has_alternative_bit(7), False)
        self.assertEqual(has_alternative_bit(10), True)
        self.assertEqual(has_alternative_bit(11), False)
        self.assertEqual(has_alternative_bit(0), True)

class HasAlternativeBitFastMutationTest(TestCase):
    def test_has_alt_fast(self):
        self.assertEqual(has_alternative_bit_fast(5), True)
        self.assertEqual(has_alternative_bit_fast(7), False)
        self.assertEqual(has_alternative_bit_fast(10), True)
        self.assertEqual(has_alternative_bit_fast(11), False)
        self.assertEqual(has_alternative_bit_fast(0), True)

"""==========================================================================="""
'''
[0.00842 s] killed by test_insert_bit (test_mutation_bit.InsertMultipleBitMutationTest)
[*] Mutation score [0.39997 s]: 87.0%
   - all: 23
   - killed: 20 (87.0%)
   - survived: 3 (13.0%)
   - incompetent: 0 (0.0%)
   - timeout: 0 (0.0%)
'''

class InsertOneBitMutationTest(TestCase):
    def test_insert_bit(self):
        self.assertEqual(insert_one_bit(21, 1, 2), 45)
        self.assertEqual(insert_one_bit(21, 0 ,2), 41)
        self.assertEqual(insert_one_bit(21, 1, 5), 53)
        self.assertEqual(insert_one_bit(21, 1, 0), 43)
        self.assertEqual(insert_mult_bits(5, 7, 3, 1), 47)
        self.assertEqual(insert_mult_bits(101, 7 ,3, 0), 815)
        self.assertEqual(insert_mult_bits(101, 7, 3, 3), 829)

class InsertMultipleBitMutationTest(TestCase):
    def test_insert_bit(self):
        self.assertEqual(insert_mult_bits(5, 7, 3, 1), 47)
        self.assertEqual(insert_mult_bits(101, 7 ,3, 0), 815)
        self.assertEqual(insert_mult_bits(101, 7, 3, 3), 829)
"""==========================================================================="""

'''
[0.00946 s] killed by test_single2 (test_mutation_bit.SingleNumber2MutationTest)
[*] Mutation score [0.18077 s]: 87.5%
   - all: 8
   - killed: 7 (87.5%)
   - survived: 1 (12.5%)
   - incompetent: 0 (0.0%)
   - timeout: 0 (0.0%)
'''

class SingleNumber2MutationTest(TestCase):
    def test_single2(self):
        self.assertEqual(single_number2([1,1,1,2,3,3,3,4,4,4,5,5,5]), 2)
        self.assertEqual(single_number2([1,1,1,2,2,2,3,3,3,4,4,4,5,5,5]), 0)
        self.assertEqual(single_number2([1,1,1,1]), 1)

"""==========================================================================="""
'''
[0.00859 s] killed by test_swap (test_mutation_bit.SwapPairMutationTest)
[*] Mutation score [0.28292 s]: 86.7%
   - all: 15
   - killed: 13 (86.7%)
   - survived: 2 (13.3%)
   - incompetent: 0 (0.0%)
   - timeout: 0 (0.0%)
'''

class SwapPairMutationTest(TestCase):
    def test_swap(self):
        self.assertEqual(swap_pair(10), 5)
        self.assertEqual(swap_pair(5), 10)
        self.assertEqual(swap_pair(4), 8)
        self.assertEqual(swap_pair(1), 2)
"""==========================================================================="""
'''
[0.00878 s] killed by test_subset (test_mutation_bit.SubsetsMutationTest)
[*] Mutation score [0.17616 s]: 57.1%
   - all: 7
   - killed: 4 (57.1%)
   - survived: 3 (42.9%)
   - incompetent: 0 (0.0%)
   - timeout: 0 (0.0%)
'''
class SubsetsMutationTest(TestCase):
    def test_subset(self):
        self.assertEqual(subsets([1,2,3]), {
                                  (1, 2),
                                  (1, 3),
                                  (1,),
                                  (2,),
                                  (3,),
                                  (1, 2, 3),
                                  (),
                                  (2, 3)})
        self.assertEqual(subsets([1]),{(),(1,)})



"""==========================================================================="""





