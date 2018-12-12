from algorithms.bit import (add_bitwise_operator,
                            find_difference
                            )
import pytest
import coverage


def test_add_bitwise():
    total = add_bitwise_operator(2, 3)
    assert total == 5


@pytest.mark.skip(reason="wanted to try the skip feature")
def test_with_negative():
    total = add_bitwise_operator(-4, -4)
    assert total == -8


@pytest.mark.parametrize('arg1, arg2, expected', [(-3, -5, -8)])
def test_add_bitwise_with_negative(arg1, arg2, expected):
    assert add_bitwise_operator(arg1, arg2) == expected


@pytest.mark.parametrize('arg1, arg2, expected', [(-4, 8, 4)])
def test_add_bitwise_with_both(arg1, arg2, expected):
    assert add_bitwise_operator(arg1, arg2) == expected


@pytest.mark.parametrize('arg1, arg2, expected', [(-4, 8, 4), (0, 0, 0), (0, -3, -3), (10, -30, -20)])
def test_add_bitwise_with_multiple_parameters(arg1, arg2, expected):
    assert add_bitwise_operator(arg1, arg2) == expected


"""================================================================================"""
"""
For example:
Input:
s = "abcd"
t = "abecd"
Output: 'e'  """


def test_difference():
    missing = find_difference("abcd", "abcde")
    assert missing == 'e'


def test_difference_same_chars():
    missing = find_difference("aaaa", "aaaaa")
    assert missing == 'a'


def test_difference_one():
    missing = find_difference("qwer", "qwery")
    assert missing == 'y'


def test_difference_allsame():
    missing = find_difference("aaaabbb", "aaaabbbb")
    assert missing == 'b'


def test_difference_two():
    missing = find_difference("abcd,", "abcd,,")
    assert missing == ','
