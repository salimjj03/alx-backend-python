#!/usr/bin/env python3
""" testing client module """

from parameterized import parameterized, parameterized_class
import json
from fixtures import TEST_PAYLOAD
from client import GithubOrgClient
from unittest.mock import patch, PropertyMock, Mock
import unittest


class TestGithubOrgClient(unittest.TestCase):
    """
    This method should test that GithubOrgClient.org returns the correct value.
    """

    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.get_json')
    def test_org(self, input, mock):
        """Test that GithubOrgClient.org returns the correct value"""
        cls_test = GithubOrgClient(input)
        cls_test.org()
        mock.assert_called_once_with(f'https://api.github.com/orgs/{input}')

    def test_public_repos_url(self):
        """
        This method should test that GithubOrgClient.org returns
        the correct value.
        """

        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock:
            load = {"repos_url": "World"}
            mock.return_value = load
            cls_test = GithubOrgClient('test')
            result = cls_test._public_repos_url
            self.assertEqual(result, load["repos_url"])

    @patch('client.get_json')
    def test_public_repos(self, mock_json):
        """
        This method should test that GithubOrgClient.org returns the
        correct value.
        """
        load_json = [{"name": "Google"}, {"name": "Twitter"}]
        mock_json.return_value = load_json

        with patch('client.GithubOrgClient._public_repos_url',
                   n_callable=PropertyMock) as public_mock:

            public_mock.return_value = "hello/world"
            cls_test = GithubOrgClient('test')
            result = cls_test.public_repos()

            check = [i["name"] for i in load_json]
            self.assertEqual(result, check)

            public_mock.assert_called_once()
            mock_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """
        This method should test that GithubOrgClient.org returns
        the correct value.
        """
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    This method should test that GithubOrgClient.org
    returns the correct value.
    """
    @classmethod
    def setUpClass(cls):
        """
        This method should test that GithubOrgClient.org returns
        the correct value.
        """

        config = {'return_value.json.side_effect':
                  [
                      cls.org_payload, cls.repos_payload,
                      cls.org_payload, cls.repos_payload
                  ]
                  }
        cls.get_patcher = patch('requests.get', **config)

        cls.mock = cls.get_patcher.start()

    def test_public_repos(self):
        """
        This method should test that GithubOrgClient.org
        returns the correct value.
        """

        cls_test = GithubOrgClient("google")

        self.assertEqual(cls_test.org, self.org_payload)
        self.assertEqual(cls_test.repos_payload, self.repos_payload)
        self.assertEqual(cls_test.public_repos(), self.expected_repos)
        self.assertEqual(cls_test.public_repos("XLICENSE"), [])
        self.mock.assert_called()

    def test_public_repos_with_license(self):
        """
        This method should test that GithubOrgClient.org
        returns the correct value.
        """

        test_class = GithubOrgClient("google")

        self.assertEqual(test_class.public_repos(), self.expected_repos)
        self.assertEqual(test_class.public_repos("XLICENSE"), [])
        self.assertEqual(test_class.public_repos(
            "apache-2.0"), self.apache2_repos)
        self.mock.assert_called()

    @classmethod
    def tearDownClass(cls):
        """
        This method should test that GithubOrgClient.org
        returns the correct value.
        """

        cls.get_patcher.stop()
