import unittest
from exercise import *


class TestFunctions(unittest.TestCase):
    def test_neighbors_distance_1(self):
        G = {
            1: [2, 4],
            2: [3],
            4: [5],
            5: [2, 6],
            7: [1]
        }
        
        expected_result = {2, 4}
        actual_result = neighbors(G, 1, 1)
        
        self.assertSetEqual(expected_result, actual_result)
        
    def test_neighbors_distance_2(self):
        G = {
            1: [2, 4],
            2: [3],
            4: [5],
            5: [2, 6],
            7: [1]
        }
        
        expected_result = {2, 3, 4, 5}
        actual_result = neighbors(G, 1, 2)
        
        self.assertSetEqual(expected_result, actual_result)
