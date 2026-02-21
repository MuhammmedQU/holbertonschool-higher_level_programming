#!/usr/bin/python3
"""Unittest for max_integer function"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer"""

    def test_ordered_list(self):
        """Max at the end"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Max in the middle"""
        self.assertEqual(max_integer([3, 1, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Max at the beginning"""
        self.assertEqual(max_integer([9, 3, 2, 1]), 9)

    def test_negative_numbers(self):
        """Negative numbers"""
        self.assertEqual(max_integer([-5, -2, -8, -1]), -1)

    def test_single_element(self):
        """Single element list"""
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        """Empty list returns None"""
        self.assertIsNone(max_integer([]))

    def test_all_equal(self):
        """All elements equal"""
        self.assertEqual(max_integer([5, 5, 5]), 5)

    def test_float_numbers(self):
        """Float numbers"""
        self.assertEqual(max_integer([1.2, 3.5, 2.1]), 3.5)


if __name__ == "__main__":
    unittest.main()
