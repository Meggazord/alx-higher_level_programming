#!/usr/bin/python3

"""unittest testing of max_integer function"""

import sys
sys.path.append(
    '/Users/Megahed/alx/projects/alx-higher_level_programming/0x07-python-test_driven_development')
max_integer = __import__('6-max_integer').max_integer
import unittest


class TestMaxInteger(unittest.TestCase):
    """Unit tests for max_integer function"""

    def test_max_at_end(self):
        """max_integer at the end"""
        result = max_integer([1, 2, 3, 4])
        self.assertEqual(result, 4)

    def test_max_at_beg(self):
        """max_integer at the beginning"""
        result = max_integer([4, 2, 3, 1])
        self.assertEqual(result, 4)

    def test_max_in_mid(self):
        """max_integer in the middle"""
        result = max_integer([1, 3, 4, 2])
        self.assertEqual(result, 4)

    def test_one_number(self):
        """function only takes one number"""
        result = max_integer([3])
        self.assertEqual(result, 3)

    def test_takes_None(self):
        """function takes None"""
        result = max_integer()
        self.assertEqual(result, None)

    def test_empty_list(self):
        """function is empty"""
        result = max_integer()
        self.assertEqual(result, None)

    def test_takes_one_negative(self):
        """function takes one negative number"""
        result = max_integer([1, 3, -4, 2])
        self.assertEqual(result, 3)

    def test_takes_all_negative(self):
        """function takes all negative numbers"""
        result = max_integer([-1, -3, -4, -2])
        self.assertEqual(result, -1)


if __name__ == "__main__":
    unittest.main()
