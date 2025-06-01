import unittest
from unittest.mock import patch, Mock
import requests
import sys
import os

sys.path.append(os.path.abspath("../script-for-workflow"))
import pyscript

class TestGitHubScript(unittest.TestCase):

    @patch("pyscript.requests.get")
    def test_fetch_commits_success(self, mock_get):
        mock_response = Mock()
        mock_response.raise_for_status = Mock()
        mock_response.json.return_value = [{
            "sha": "abc123",
            "commit": {
                "author": {
                    "name": "John Doe",
                    "date": "2023-06-01T00:00:00Z"
                },
                "message": "Initial commit"
            }
        }]
        mock_get.return_value = mock_response

        pyscript.fetch_commits_and_print_specific_commit_detail()

    @patch("pyscript.requests.get")
    def test_fetch_commits_empty(self, mock_get):
        mock_response = Mock()
        mock_response.raise_for_status = Mock()
        mock_response.json.return_value = []
        mock_get.return_value = mock_response

        pyscript.fetch_commits_and_print_specific_commit_detail()

    @patch("pyscript.requests.get")
    def test_fetch_commits_error(self, mock_get):
        mock_get.side_effect = requests.exceptions.ConnectionError
        pyscript.fetch_commits_and_print_specific_commit_detail()

    @patch("pyscript.requests.get")
    def test_fetch_issues_success(self, mock_get):
        mock_response = Mock()
        mock_response.raise_for_status = Mock()
        mock_response.json.side_effect = [
            [{"number": 1, "title": "Issue A", "state": "open"}],
            []  # End pagination
        ]
        mock_get.return_value = mock_response

        pyscript.fetch_all_issues_with_status()

    @patch("pyscript.requests.get")
    def test_fetch_issues_with_pull_request_skipped(self, mock_get):
        mock_response = Mock()
        mock_response.raise_for_status = Mock()
        mock_response.json.side_effect = [
            [{"number": 1, "title": "PR disguised as issue", "state": "open", "pull_request": {}}],
            []  # End pagination
        ]
        mock_get.return_value = mock_response

        pyscript.fetch_all_issues_with_status()

    @patch("pyscript.requests.get")
    def test_fetch_issues_error(self, mock_get):
        mock_get.side_effect = requests.exceptions.Timeout
        pyscript.fetch_all_issues_with_status()

    @patch("pyscript.requests.get")
    def test_fetch_pull_requests_success(self, mock_get):
        mock_response = Mock()
        mock_response.raise_for_status = Mock()
        mock_response.json.side_effect = [
            [{"number": 10, "title": "Fix bug", "state": "closed"}],
            []  # End pagination
        ]
        mock_get.return_value = mock_response

        pyscript.fetch_pull_requests()

    @patch("pyscript.requests.get")
    def test_fetch_pull_requests_error(self, mock_get):
        mock_get.side_effect = requests.exceptions.HTTPError("Bad Request")
        pyscript.fetch_pull_requests()

if __name__ == "__main__":
    unittest.main()