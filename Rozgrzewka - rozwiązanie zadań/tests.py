import unittest
from exercise import *


class TestFunctions(unittest.TestCase):
    def test_f_default_arg_immutable(self):
        self.assertEqual(f_default_arg_immutable(), 0)
        self.assertEqual(f_default_arg_immutable(1), 1)
 
    def test_f_default_arg_mutable(self):
        self.assertListEqual(f_default_arg_mutable(1), [1])
        self.assertListEqual(f_default_arg_mutable(1), [1])
        self.assertListEqual(f_default_arg_mutable(2, [1]), [1, 2])
        self.assertListEqual(f_default_arg_mutable(4, [1, 2, 3]), [1, 2, 3])
 
    def test_f_indexing_and_slicing(self):
        self.assertTupleEqual(f_indexing_and_slicing([1, 2, 3]), (1, 3, [1, 2]))
 
    def test_f_str_formatting(self):
        self.assertEqual(f_str_formatting([0.356, 1, 0.2]), "0.36 - 1.00 - 0.20")
 
    def test_f_swap(self):
        array = [1, 2, 3]
        f_swap(array)
        self.assertListEqual(array, [3, 2, 1])
 
    def test_f_shallow_copy(self):
        array_in = [1, 2, 3]
        array_out = f_shallow_copy(array_in)
        self.assertIsNot(array_in, array_out)
        self.assertListEqual(array_in, array_out)
 
    def test_f_lambda(self):
        f = f_lambda()
        self.assertEqual(f(1), 2)
 
    def test_f_logic(self):
        self.assertTrue(f_logic(3, False, True))
        self.assertTrue(f_logic(1, True, False))
        self.assertFalse(f_logic(1, False, True))
        self.assertFalse(f_logic(1, False, False))
        self.assertFalse(f_logic(1, True, True))
        self.assertFalse(f_logic(4, True, True))
 
    def test_f_list_creation(self):
        self.assertListEqual(f_list_creation(3), [1, 1, 1])
 
    def test_f_comprehensions(self):
        self.assertTupleEqual(f_comprehensions({0: 0, 1: 1, 2: 4, 4: 5, 9: 6}),
                              (42, {1, 2, 4}))
 
    def test_point(self):
        self.assertTrue(issubclass(Point, tuple))
        self.assertTrue(hasattr(Point, 'x'))
        self.assertTrue(hasattr(Point, 'y'))
        Point(x=0.1, y=0.5)
