from unittest import TestCase
from top_one import top_1


class TopOneTest(TestCase):

    def test_top_one(self):
    	self.assertListEqual(top_1([1, 1, 4, 4, 3]), [1, 4])
    	self.assertListEqual(top_1([1, 1, 1, 2, 3]), [1])
    	self.assertListEqual(top_1([6, 7, 8, 9, 9, 7]), [9])
    	self.assertListEqual(top_1([10, 1, 222, 222, 10]), [10, 222])
    	self.assertListEqual(
    	    top_1([1, 1, 2, 2, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, ]), [6])
    	self.assertListEqual(top_1([0, 0, 0, , 0, 1, 1, 1, 1]), [0, 1])

"""
Mutation Test Output
[*] Start mutation process:
   - targets: top_one
   - tests: test_top_one
[*] 1 tests passed:
   - test_top_one [0.00023 s]
[*] Start mutants generation and execution:
   - [#   1] ASR top_one:21 : 
--------------------------------------------------------------------------------
 17:     f_val = 0
 18:     
 19:     for i in arr:
 20:         if i in values:
~21:             values[i] -= 1
 22:         else:
 23:             values[i] = 1
 24:     
 25:     f_val = max(values.values())
 26:     
--------------------------------------------------------------------------------
[0.00861 s] killed by test_top_one (test_top_one.TopOneTest)
   - [#   2] BCR top_one:31 : 
--------------------------------------------------------------------------------
 27:     for i in values.keys():
 28:         if values[i] == f_val:
 29:             result.append(i)
 30:         else:
~31:             break
 32:     
 33:     return result
--------------------------------------------------------------------------------
[0.00863 s] survived
   - [#   3] COI top_one:20 : 
--------------------------------------------------------------------------------
 16:     result = []
 17:     f_val = 0
 18:     
 19:     for i in arr:
~20:         if (not i in values):
 21:             values[i] += 1
 22:         else:
 23:             values[i] = 1
 24:     
 25:     f_val = max(values.values())
--------------------------------------------------------------------------------
[0.00998 s] killed by test_top_one (test_top_one.TopOneTest)
   - [#   4] COI top_one:20 : 
--------------------------------------------------------------------------------
 16:     result = []
 17:     f_val = 0
 18:     
 19:     for i in arr:
~20:         if i not in values:
 21:             values[i] += 1
 22:         else:
 23:             values[i] = 1
 24:     
 25:     f_val = max(values.values())
--------------------------------------------------------------------------------
[0.00789 s] killed by test_top_one (test_top_one.TopOneTest)
   - [#   5] COI top_one:28 : 
--------------------------------------------------------------------------------
 24:     
 25:     f_val = max(values.values())
 26:     
 27:     for i in values.keys():
~28:         if (not values[i] == f_val):
 29:             result.append(i)
 30:         else:
 31:             continue
 32:     
 33:     return result
--------------------------------------------------------------------------------
[0.00970 s] killed by test_top_one (test_top_one.TopOneTest)
   - [#   6] CRP top_one:17 : 
--------------------------------------------------------------------------------
 13:     values = {}
 14:     
 15:     
 16:     result = []
~17:     f_val = 1
 18:     
 19:     for i in arr:
 20:         if i in values:
 21:             values[i] += 1
 22:         else:
--------------------------------------------------------------------------------
[0.00728 s] survived
   - [#   7] CRP top_one:21 : 
--------------------------------------------------------------------------------
 17:     f_val = 0
 18:     
 19:     for i in arr:
 20:         if i in values:
~21:             values[i] += 2
 22:         else:
 23:             values[i] = 1
 24:     
 25:     f_val = max(values.values())
 26:     
--------------------------------------------------------------------------------
[0.00805 s] survived
   - [#   8] CRP top_one:23 : 
--------------------------------------------------------------------------------
 19:     for i in arr:
 20:         if i in values:
 21:             values[i] += 1
 22:         else:
~23:             values[i] = 2
 24:     
 25:     f_val = max(values.values())
 26:     
 27:     for i in values.keys():
 28:         if values[i] == f_val:
--------------------------------------------------------------------------------
[0.00697 s] survived
   - [#   9] ROR top_one:28 : 
--------------------------------------------------------------------------------
 24:     
 25:     f_val = max(values.values())
 26:     
 27:     for i in values.keys():
~28:         if values[i] != f_val:
 29:             result.append(i)
 30:         else:
 31:             continue
 32:     
 33:     return result
--------------------------------------------------------------------------------
[0.00841 s] killed by test_top_one (test_top_one.TopOneTest)
[*] Mutation score [0.17594 s]: 55.6%
   - all: 9
   - killed: 5 (55.6%)
   - survived: 4 (44.4%)
   - incompetent: 0 (0.0%)
   - timeout: 0 (0.0%)
