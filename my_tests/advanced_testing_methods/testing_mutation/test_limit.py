from unittest import TestCase
from limit import limit

class LimitTest(TestCase):

    def test_limit(self):
        self.assertListEqual(limit([1, 2, 3, 4, 5], 2, 4), [2, 3, 4])
        self.assertListEqual(limit([1, 2, 3, 4, 5], 2), [2, 3, 4, 5])


"""
Mutation Test Output

[0.00931 s] killed by test_limit (test_limit.LimitTest)
   - [#  16] ROR limit:25 : 
--------------------------------------------------------------------------------
 21:             if i >= min_lim:
 22:                 result.append(i)
 23:     else:
 24:         for i in arr:
~25:             if (i >= min_lim and i < max_lim):
 26:                 result.append(i)
 27:     
 28:     return result
--------------------------------------------------------------------------------
[0.00826 s] killed by test_limit (test_limit.LimitTest)
[*] Mutation score [0.25984 s]: 81.2%
   - all: 16
   - killed: 13 (81.2%)
   - survived: 3 (18.8%)
   - incompetent: 0 (0.0%)
   - timeout: 0 (0.0%)
