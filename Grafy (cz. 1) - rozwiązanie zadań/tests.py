import unittest
from exercise import *


class TestFunctions(unittest.TestCase):
    def test_adjmat_to_adjlist(self):
        A = [
                [0, 1, 0],
                [0, 0, 1],
                [1, 2, 0]
            ]
        expected_result = {
            1: [2],
            2: [3],
            3: [1, 2, 2]
        }
        
        actual_result = adjmat_to_adjlist(A)
        self.assertDictEqual(expected_result, actual_result)
        
    def test_dfs_iterative(self):
        G = {
            1: [2, 3, 5],
            2: [1, 4, 6],
            3: [1, 7],
            4: [2],
            5: [1, 6],
            6: [2, 5],
            7: [3]
        }
        expected_result = [1, 2, 4, 6, 5, 3, 7]
        
        actual_result = dfs_iterative(G, 1)
        self.assertListEqual(expected_result, actual_result)
        
    def test_dfs_recursive(self):
        G = {
            1: [2, 3, 5],
            2: [1, 4, 6],
            3: [1, 7],
            4: [2],
            5: [1, 6],
            6: [2, 5],
            7: [3]
        }
        expected_result = [1, 2, 4, 6, 5, 3, 7]
        
        actual_result = dfs_recursive(G, 1)
        self.assertListEqual(expected_result, actual_result)
        
    def test_is_acyclic(self):
        G = {1: [2, 3], 3: [4]}
        self.assertTrue(is_acyclic(G))