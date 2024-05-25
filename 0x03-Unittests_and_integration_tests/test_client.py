#!/usr/bin/env python3
"""Testing client.GithubOrgClient class"""
import requests
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


@parameterized_class(('org_payload', 'repos_payload',
                      'expected_repos', 'apache2_repos'), [
                          (TEST_PAYLOAD[0][0], TEST_PAYLOAD[0][1],
                           TEST_PAYLOAD[0][2], TEST_PAYLOAD[0][3])
                      ])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Testing GithubOrgClient.public_repos"""
    @classmethod
    def setUpClass(cls):
        cls.get_patcher = patch('utils.requests.get')
        mocked_get = cls.get_patcher.start()

        # def side_effect(url):
        #     if url == 'url_for_org_payload':
        #         return cls.org_payload
        #     elif url == 'url_for_repos_payload':
        #         return cls.repos_payload
        #     elif url == 'url_for_expected_repos':
        #         return cls.expected_repos
        #     elif url == 'url_for_apache2_repos':
        #         return cls.apache2_repos
        #     else:
        #         raise ValueError(f'Unexpected URL: {url}')

        # mocked_get.side_effect = side_effect
        response_mock = MagicMock()

        response_mock.json.side_effect = [
            (cls.org_payload, cls.repos_payload,
             cls.expected_payload, cls.apache2_repos)
             ]

        mocked_get.return_value = response_mock

        instance = GithubOrgClient('google')
        result = instance.public_repos()

        cls.assertEqual(result, mocked_get.return_value)

    @classmethod
    def tearDownClass(cls):
        cls.get_patcher.stop()

    # def test_public_repos_with_org_payload(self):
    #     """Testing public_repos with org payload"""
    #     instance = GithubOrgClient('google')
    #     result = instance.public_repos()

    #     self.assertEqual(result, self.org_payload)

    # def test_public_repos_with_repos_payload(self):
    #     """Testing public_repos with repos payload"""
    #     instance = GithubOrgClient('google')
    #     result = instance.public_repos()

    #     self.assertEqual(result, self.repos_payload)

    # def test_public_repos_with_expected_repos(self):
    #     """Testing public_repos with expected_repos"""
    #     instance = GithubOrgClient('google')
    #     result = instance.public_repos()

    #     self.assertEqual(result, self.expected_repos)

    # def test_public_repos_with_apache2_repos(self):
    #     """Testing public_repos with apache2_repos"""
    #     instance = GithubOrgClient('google')
    #     result = instance.public_repos()

    #     self.assertEqual(result, self.apache2_repos)
