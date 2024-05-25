#!/usr/bin/env python3
""" testing utils mudule"""

import requests
from parameterized import parameterized
from utils import (access_nested_map, get_json, memoize)
import unittest
from unittest.mock import patch


class TestAccessNestedMap(unittest.TestCase):
    """
    the TestAccessNestedMap.test_access_nested_map
    method to test that the method returns what it
    is supposed to.

    Decorate the method with @parameterized.expand
    to test the function for following inputs:
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        the TestAccessNestedMap.test_access_nested_map
        method to test that the method returns what it
        is supposed to.

        Decorate the method with @parameterized.expand
        to test the function for following inputs:
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b')
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """
        the TestAccessNestedMap.test_access_nested_map
        method to test that the method returns what it
        is supposed to.

        Decorate the method with @parameterized.expand
        to test the function for following inputs:
        """
        with self.assertRaises(KeyError) as e:
            access_nested_map(nested_map, path)
        self.assertEqual(f"KeyError('{expected}')", repr(e.exception))


class TestGetJson(unittest.TestCase):
    """ Testing Get Json class"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """
        the TestAccessNestedMap.test_access_nested_map
        method to test that the method returns what it
        is supposed to.

        Decorate the method with @parameterized.expand
        to test the function for following inputs:
        """
        config = {'return_value.json.return_value': test_payload}
        patcher = patch('requests.get', **config)
        mock = patcher.start()
        self.assertEqual(get_json(test_url), test_payload)
        mock.assert_called_once()
        patcher.stop()


class TestMemoize(unittest.TestCase):
    """ Testing Memoize class"""

    def test_memoize(self):
        """
        the TestAccessNestedMap.test_access_nested_map
        method to test that the method returns what it
        is supposed to.

        Decorate the method with @parameterized.expand
        to test the function for following inputs:
        """

        class TestClass:
            """
            the TestAccessNestedMap.test_access_nested_map
            method to test that the method returns what it
            is supposed to.

            Decorate the method with @parameterized.expand
            to test the function for following inputs:
            """

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock:
            test_cls = TestClass()
            test_cls.a_property()
            test_cls.a_property()
            mock.assert_called_once()
