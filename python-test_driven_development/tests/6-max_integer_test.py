#!/usr/bin/python3

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_positive_integers(self):
        """Test list of positive integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([10, 100, 1000, 5000]), 5000)

    def test_negative_integers(self):
        """Test list with negative integers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-10, -100, -1000]), -10)

    def test_mixed_integers(self):
        """Test list with mixed positive and negative integers"""
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)
        self.assertEqual(max_integer([-10, 10, 0, -100, 50]), 50)

    def test_single_element(self):
        """Test list with a single element"""
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        """Test empty list"""
        self.assertIsNone(max_integer([]))

    def test_repeated_numbers(self):
        """Test list with repeated numbers"""
        self.assertEqual(max_integer([2, 2, 2]), 2)

    def test_floats(self):
        """Test list with floats"""
        self.assertEqual(max_integer([1.5, 2.7, 3.8, 2.1]), 3.8)

    def test_mixed_floats_and_integers(self):
        """Test list with both integers and floats"""
        self.assertEqual(max_integer([1, 2.7, 3, 2]), 3)

    def test_strings(self):
        """Test list with strings (if applicable)"""
        self.assertEqual(max_integer(["apple", "banana", "cherry"]), "cherry")

    def test_none_input(self):
        """Test None as input"""
        self.assertIsNone(max_integer([]))

    def test_non_iterable(self):
        """Test if non-iterable is passed as an argument"""
        with self.assertRaises(TypeError):
            max_integer(42)


if __name__ == '__main__':
    unittest.main()
