#!/usr/bin/env python3
"""Testing client.GithubOrgClient class"""
from client import GithubOrgClient
from parameterized import parameterized
import mock
import unittest
from unittest.mock import patch
from parameterized import parameterized


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
