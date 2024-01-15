#!/usr/bin/python3

"""unittest testing of max_integer function"""

import sys
sys.path.append(
    '/Users/Megahed/alx/projects/alx-higher_level_programming/0x07-python-test_driven_development')
max_integer = __import__('6-max_integer').max_integer
import unittest


class TestMaxInteger(unittest.TestCase):
    """Unit tests for max_integer function"""

    def test_basic_functionality(self):
        """basic functionality test of max_integer"""
        result = max_integer([1, 2, 3, 4])
        self.assertEqual(result, 4)

    def test_basic_functionality_2(self):
        """variation # 2 of basic functionalyt testing of max_integer"""
        result = max_integer([1, 3, 4, 2])
        self.assertEqual(result, 4)


if __name__ == "__main__":
    unittest.main()
