#!/usr/bin/env python3
"""Parameterize a unit test"""
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized

access_nested_map = __import__('utils').access_nested_map
get_json = __import__('utils').get_json
memoize = __import__('utils').memoize


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

    @parameterized.expand([
        ({}, ["a"]),
        ({"a": 1}, ["a", "b"])
        ])
    def test_access_nested_map_exception(self, nested_map, keys):
        """Testing access_nested_map method raising exception"""
        with self.assertRaises(KeyError):
            access_nested_map(access_nested_map(nested_map, keys))


class TestGetJson(unittest.TestCase):
    """TestGetJson class"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
        ])
    @patch('requests.get')
    def test_get_json(self, url, payload, mock_get):
        """Testing get_json method"""
        mock_response = Mock()
        mock_response.json.return_value = payload

        mock_get.return_value = mock_response

        get_data = get_json(url)

        mock_get.assert_called_once_with(url)
        self.assertEqual(get_data, payload)


class TestClass:

    def a_method(self):
        return 42

    @memoize
    def a_property(self):
        return self.a_method()


class TestMemoize(unittest.TestCase):
    """Testing memoization"""
    def test_memoize(self):
        """Testing Memoize"""
        with patch('test_utils.TestClass.a_method',
                   return_value=42) as mocked_method:
            instance = TestClass()
            call_one = instance.a_property
            call_two = instance.a_property

            self.assertEqual(call_one, 42)
            self.assertEqual(call_one, call_two)

            mocked_method.assert_called_once()
