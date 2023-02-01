#!/usr/bin/python3

import unittest

max_integer = __import__("6-max_integer").max_integer


"""This is my testing module"""


class MaxIntegerTest(unittest.TestCase):
    """This is a testing class"""

    def test_max_positive(self):
        self.assertEqual(5, max_integer([1, 2, 3, 4, 5]))

    def test_max_negatve(self):
        self.assertEqual(-1, max_integer([-11, -1,  -2, -3, -4, -5]))

    def test_max_beginning(self):
        self.assertEqual(5, max_integer([5, 1, 3, 4, 2]))

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_single_item(self):
        self.assertEqual(6, max_integer([6]))
