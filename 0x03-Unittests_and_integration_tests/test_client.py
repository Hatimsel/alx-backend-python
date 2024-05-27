#!/usr/bin/env python3
"""Testing client.GithubOrgClient class"""
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from parameterized import parameterized
import mock
import unittest
from unittest.mock import patch, MagicMock
from parameterized import parameterized, parameterized_class


class TestGithubOrgClient(unittest.TestCase):
    """Testing GithubOrgClient class"""
    @parameterized.expand([
        ('google',),
        ('abc',)
        ])
    @patch('client.get_json', return_value={})
    def test_org(self, org_name, mock_get):
        """Testing that GithubOrgClient.org returns
        the correct value
        """
        ORG_URL = f"https://api.github.com/orgs/{org_name}"

        instance = GithubOrgClient(org_name)
        instance.org

        mock_get.assert_called_once_with(ORG_URL)

    def test_public_repos_url(self):
        """"Testing GithubOrgClient._public_repos_url"""
        with patch('client.GithubOrgClient.org',
                   new_callable=mock.PropertyMock) as mocked_property:
            mocked_property.return_value = {
                'repos_url': 'https://api.github.com/orgs/google/repos'
                }

            instance = GithubOrgClient('google')

            self.assertEqual(instance._public_repos_url,
                             mocked_property.return_value['repos_url'])

    @patch('client.get_json')
    def test_public_repos(self, mock_get):
        """Testing GithubOrgClient.public_repos"""
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=mock.PropertyMock) as mocked_preperty:
            mocked_preperty.return_value = 'https://api.github.com/orgs\
                                            /netflix/repos'

            instance = GithubOrgClient('netflix')
            mock_get.return_value = instance.org
            public_repos = instance._public_repos_url

            self.assertEqual(mocked_preperty.return_value, public_repos)
            mock_get.assert_called_once()
            mocked_preperty.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, mapping, value, expected_result):
        """Testing GithubOrgClient.has_license"""
        self.assertEqual(GithubOrgClient.has_license(mapping, value),
                         expected_result)


@parameterized_class(['org_payload', 'repos_payload',
                      'expected_repos', 'apache2_repos'],
                     TEST_PAYLOAD)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Testing GithubOrgClient.public_repos"""
    @classmethod
    def setUpClass(cls):
        """Setting up our testclass"""
        config = {
            'return_value.json.side_effect': [
                cls.org_payload, cls.repos_payload,
                cls.org_payload, cls.repos_payload
            ]
        }

        cls.get_patcher = patch('requests.get', **config)
        cls.mocked_get = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Testing public_repos"""
        instance = GithubOrgClient('google')
        org_result = instance.org
        public_result = instance.public_repos()

        self.assertEqual(org_result, self.org_payload)
        self.assertEqual(public_result, self.expected_repos)
        self.mocked_get.assert_called()

    def test_public_repos_with_license(self, license="apache-2.0"):
        """Testing public_repos with license"""
        instance = GithubOrgClient('google')
        result = instance.public_repos(license=license)

        self.assertEqual(result, self.apache2_repos)
        self.mocked_get.assert_called()
