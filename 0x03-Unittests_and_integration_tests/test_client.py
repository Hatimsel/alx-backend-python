#!/usr/bin/python3
"""Testing client.GithubOrgClient class"""
from client import GithubOrgClient
import unittest
from unittest.mock import Mock, patch
from utils import get_json
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """Testing GithubOrgClient class"""
    @parameterized.expand([
        'google',
        'abc'
        ])
    @patch('utils.get_json')
    def test_org(self, org_name, mock_get):
        """Testing that GithubOrgClient.org returns
        the correct value
        """
        ORG_URL = f"https://api.github.com/orgs/{org_name}"

        instance = GithubOrgClient(org_name)
        instance.org

        mock_get.assert_called_once_with(ORG_URL)
