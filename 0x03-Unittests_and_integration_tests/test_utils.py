#!/usr/bin/env python3
"""Parameterize a unit test"""
import unittest
from parameterized import parameterized

access_nested_map = __import__('utils').access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Testing utils"""
    @parameterized.expand([
        ({"a": 1}, ["a"], 1),
        ({"a": {"b": 2}}, ["a"], {"b": 2}),
        ({"a": {"b": 2}}, ["a", "b"], 2)
        ])
    def test_access_nested_map(self, nested_map, key, expected_res):
        """Testing access_nested_map method"""
        self.assertEqual(access_nested_map(nested_map, key), expected_res)
