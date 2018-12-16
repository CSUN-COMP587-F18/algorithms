from arrays import *
import pytest
import coverage

def test_delete():
    ans = delete_nth([1,2,3,1,2,1,2,3], 2)
    assert ans == [1,2,3,1,2,3]

def test_delete_naive():
    ans = delete_nth_naive([], 1)
    assert ans == []
"""================================================================"""

def test_flatten():
    input = flatten([1,1,2,[3]], None)
    assert input == [1,1,2,3]

"""================================================================"""
def test_limit():
    lim = limit([1,2,3,4,5], None, 3)
    assert lim == [1,2,3]

def test_limit_empty():
    lim = limit([], None, 3)
    assert lim == []
"""================================================================"""
def test_longest_non_repeat_v1():
    non = longest_non_repeat_v1("abcabcbb")
    assert non == 3

def test_longest_non_repeat_v2_empty():
    non = longest_non_repeat_v2("")
    assert non == 0
"""================================================================"""

def test_max_ones_index():
   maxi = max_ones_index([1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1])
   assert maxi == 3

def test_max_ones_index_empty():
   maxi = max_ones_index([])
   assert maxi == -1

"""================================================================"""
def test_missing_ranges():
   miss = missing_ranges([3, 5],1,10)
   assert miss == [(1, 2), (4, 4), (6, 10)]

def test_missing_ranges_empty():
   miss = missing_ranges([],0,0)
   assert miss == [(0, 0)]

"""================================================================"""

def test_move_zeroes():
   move = move_zeros([ 1, 0, 1, 2, 0, 1, 3, "a"])
   assert move == [ 1, 1, 2, 1, 3, "a", 0, 0]

def test_move_zeroes_empty():
   move = move_zeros([])
   assert move == []
"""================================================================"""

def test_n_sum():
   n = n_sum(4, [1, 0, -1, 0, -2, 2],0)
   assert n == [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]

def test_n_sum_empty():
   n = n_sum(4, [],0)
   assert n == []
"""================================================================"""

def test_plus_one_v1():
   plus = plus_one_v1([6])
   assert plus == [7]
 
def test_plus_one_v2():
   plus = plus_one_v2([4])
   assert plus == [5]

def test_plus_one_v3():
   plus = plus_one_v3([3,4,8])
   assert plus == [3,4,9]
"""================================================================"""

def test_rotate_v1():
   rot = rotate_v1([1,2,3,4,5,6,7], 3)
   assert rot == [5,6,7,1,2,3,4]

def test_rotate_v2():
   rot = rotate_v2([1,2,3,4,5,6,7], 3)
   assert rot == [5,6,7,1,2,3,4]

def test_rotate_v3():
   rot = rotate_v3([1], 3)
   assert rot == [1]

"""================================================================"""

def test_summarize_ranges():
   ranges = summarize_ranges([0, 1, 2, 4, 5, 7])
   assert ranges == [(0, 2), (4, 5), (7, 7)]

def test_summarize_ranges_empty():
   ranges = summarize_ranges([])
   assert ranges == []
"""================================================================"""

def test_three_sum():
   three = three_sum([-1, 0, 1, 2, -1, -4])
   assert three =={
                     (-1, 0, 1),
                     (-1, -1, 2)
                  }
"""================================================================"""

def test_top_1():
   top = top_1([1, 1, 2, 2, 3, 4])
   assert top == [1, 2]

"""================================================================"""
def test_trimmean():
   trim = trimmean([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],20)
   assert trim == 5.5
"""================================================================"""

def test_two_sum():
   top = two_sum([2, 7, 11, 15],9)
   assert top == (0, 1)
"""================================================================"""

def test_garage():
   steps, cars = garage([1, 2, 3, 0, 4],[0, 3, 2, 1, 4]) 
   assert steps == 4
   assert  cars  == [[0, 2, 3, 1, 4],
                     [2, 0, 3, 1, 4],
                     [2, 3, 0, 1, 4],
                     [0, 3, 2, 1, 4]]
"""================================================================"""

def test_merge_intervals():
   interval_input = [[1,4],[2,6],[10,14],[17,20]]
   inputs = merge_intervals(interval_input)
   assert inputs == [[1,6],[10,14],[17,20]]
"""================================================================"""
