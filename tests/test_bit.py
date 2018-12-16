from bit import *
from collections import deque
import pytest
import coverage


def test_add_bitwise():
    total = add_bitwise_operator(2, 3)
    assert total == 5

def test_add_bitwise_with_negative():
    total = add_bitwise_operator(-4, -9)
    assert total == -13

"""==========================================================================="""

def test_binary_gap():
    ans = binary_gap(22)
    assert ans == 2

def test_binary_gap_with_zero():
    ans = binary_gap(0)
    assert ans == 0
"""==========================================================================="""

def test_count_flips_to_convert_int():
    count = count_flips_to_convert(29,15)
    assert count == 2

def test_count_flips_to_convert_binary():
    count = count_flips_to_convert(11101, 1111)
    assert count == 7
"""==========================================================================="""

def test_count_ones_recursive():
    num = count_ones_recur(8)
    assert num == 1

def test_count_ones_recursive_zero():
    num = count_ones_recur(0)
    assert num == 0

def test_count_ones_iterative():
    num = count_ones_iter(8)
    assert num == 1

def test_count_ones_iterative_zero():
    num = count_ones_iter(0)
    assert num == 0
"""==========================================================================="""
def test_find_difference():
   diff = find_difference("abcd" , "abcde")
   assert diff == 'e'

def test_find_difference_reduced():
   diff = find_difference("" , "b")
   assert diff == 'b'
"""==========================================================================="""

def test_flip_bit_longest_sequence_int():
    num = flip_bit_longest_seq(4)
    assert num == 2


def test_flip_bit_longest_sequence_binary():
    num = flip_bit_longest_seq(10001111)
    assert num == 5

"""==========================================================================="""

def test_has_alternative_bit():
    alt = has_alternative_bit(5)
    assert alt == True

def test_has_alternative_bit_faster():
    alt = has_alternative_bit_fast(0)
    assert alt == True

"""==========================================================================="""

def test_insert_bit():
    insert  = insert_one_bit(21,1,2)
    assert insert == 45

def test_insert_bit_multiple():
    insert  = insert_mult_bits(101,7,3,3)
    assert insert == 829

"""==========================================================================="""
def test_power_of_two():
    insert  = is_power_of_two(8)
    assert insert == True

def test_power_of_two_negative():
    insert  = is_power_of_two(-8)
    assert insert == False

"""==========================================================================="""
def test_remove_bit():
    insert  = remove_bit(21,2)
    assert insert == 9

"""==========================================================================="""
def test_reverse_bit():
    insert  = reverse_bits(43261596)
    assert insert == 964176192

"""==========================================================================="""
def test_single_number():
    ret  = single_number([1,1,2,3,3])
    assert ret == 2

def test_single_number_all_pairs():
    ret  = single_number([1,1,2,2,3,3,4,4,5,5])
    assert ret == 0
"""==========================================================================="""
def test_single_number2():
    ret  = single_number2([1,1,1,2,3,3,3,4,4,4,5,5,5])
    assert ret == 2

def test_single_number2_all_pairs():
    ret  = single_number2([1,1,1,2,2,2,3,3,3,4,4,4,5,5,5])
    assert ret == 0

"""==========================================================================="""
def test_single_number3():
    ret  = single_number3([1, 2, 1, 3, 2, 5])
    assert ret ==  [3, 5]

def test_single_number3_all_same_pairs():
    ret  = single_number3([1, 1, 1, 2, 2, 2])
    assert ret ==  [1, 2]
"""==========================================================================="""
def test_subset():
    sub  = subsets([1, 2, 3])
    assert sub ==  {
    (1, 2),
    (1, 3),
    (1,),
    (2,),
    (3,),
    (1, 2, 3),
    (),
    (2, 3)
}

def test_subset_empty_set():
    sub  = subsets([])
    assert sub == {()}
"""==========================================================================="""

def test_swap_pair():
    swap  = swap_pair(22)
    assert swap == 41

def test_swap_pair_binary():
    swap  = swap_pair(1010)
    assert swap == 1009
"""==========================================================================="""