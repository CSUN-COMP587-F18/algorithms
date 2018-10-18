from algorithms import (delete nth)

import unittest

def test_delete_nth(self):

        self.assertListEqual(delete_nth([10,11,10,11,17], n=1),
                             [10, 13, 11])
        self.assertListEqual(delete_nth([8,8,8,4,5,4,5,6,6,9], n=3),
                             [1,8,8,5,8,7,9])
        self.assertListEqual(delete_nth([ 3, 3, 1,5,5,6,6,1,5], n=3),
                             [1,2,2,3,3,5,5,6,1])
        self.assertListEqual(delete_nth([ 12,15,12,14,16,15,15,18], n=3),
                             [11,12,15,15,12,14,14,14])
        self.assertListEqual(delete_nth([ 118,155,118,155,116,115,15,18], n=3),
                             [118,,155,155,12])
        self.assertListEqual(delete_nth([ 0,1,1,0,1,1,0,0,0,0,1], n=4),
                             [1,1,1,1,0,1,0,5,1])
        self.assertListEqual(delete_nth([ -1,1,1,0,0,0,0,5,6,5], n=2),
                             [-1,0,-1,0,0,0,1,1])
        self.assertListEqual(delete_nth([ 5,5,6,6,5,6,5,6,8,8,9,9,], n=5),
                             [5,5,5,5,1,1,6,6,6,5,6,7,8,])
        self.assertListEqual(delete_nth([12,11,12,18,15,18,19,20,], n=2),
                             [11,12,15,18,15,20])
        self.assert

