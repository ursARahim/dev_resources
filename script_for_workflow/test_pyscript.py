import unittest
from unittest.mock import patch, Mock
from io import StringIO
import requests

import pyscript

class TestGitHubScript(unittest.TestCase):

    @patch("pyscript.requests.get")
    @patch('sys.stdout', new_callable=StringIO)
    def test_fetch_commits_success(self, mock_stdout, mock_get):
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

        output = mock_stdout.getvalue()
        self.assertIn("Latest Commit:", output)
        self.assertIn("SHA: abc123", output)
        self.assertIn("Author: John Doe", output)
        self.assertIn("Message: Initial commit", output)
        self.assertIn("Date: 2023-06-01T00:00:00Z", output)

    @patch("pyscript.requests.get")
    @patch('sys.stdout', new_callable=StringIO)
    def test_fetch_commits_empty(self, mock_stdout, mock_get):
        mock_response = Mock()
        mock_response.raise_for_status = Mock()
        mock_response.json.return_value = []
        mock_get.return_value = mock_response

        pyscript.fetch_commits_and_print_specific_commit_detail()

        output = mock_stdout.getvalue()
        self.assertIn("No commits found.", output)

    @patch("pyscript.requests.get")
    @patch('sys.stdout', new_callable=StringIO)
    def test_fetch_commits_error(self, mock_stdout, mock_get):
        mock_get.side_effect = requests.exceptions.ConnectionError("Connection failed")

        pyscript.fetch_commits_and_print_specific_commit_detail()

        output = mock_stdout.getvalue()
        self.assertIn("An error occurred while fetching commits:", output)

    @patch("pyscript.requests.get")
    @patch('sys.stdout', new_callable=StringIO)
    def test_fetch_issues_success(self, mock_stdout, mock_get):
        mock_response = Mock()
        mock_response.raise_for_status = Mock()
        mock_response.json.side_effect = [
            [{"number": 1, "title": "Issue A", "state": "open"}],
            []  # End pagination
        ]
        mock_get.return_value = mock_response

        pyscript.fetch_all_issues_with_status()

        output = mock_stdout.getvalue()
        self.assertIn("All Issues:", output)
        self.assertIn("Issue #1: Issue A [open]", output)

    @patch("pyscript.requests.get")
    @patch('sys.stdout', new_callable=StringIO)
    def test_fetch_issues_with_pull_request_skipped(self, mock_stdout, mock_get):
        mock_response = Mock()
        mock_response.raise_for_status = Mock()
        mock_response.json.side_effect = [
            [
                {"number": 1, "title": "PR disguised as issue", "state": "open", "pull_request": {}},
                {"number": 2, "title": "Real issue", "state": "closed"}
            ],
            []  # End pagination
        ]
        mock_get.return_value = mock_response

        pyscript.fetch_all_issues_with_status()

        output = mock_stdout.getvalue()
        self.assertIn("All Issues:", output)
        self.assertIn("Issue #2: Real issue [closed]", output)
        self.assertNotIn("PR disguised as issue", output)

    @patch("pyscript.requests.get")
    @patch('sys.stdout', new_callable=StringIO)
    def test_fetch_issues_multiple_pages(self, mock_stdout, mock_get):
        mock_response = Mock()
        mock_response.raise_for_status = Mock()
        mock_response.json.side_effect = [
            [{"number": 1, "title": "Issue A", "state": "open"}],
            [{"number": 2, "title": "Issue B", "state": "closed"}],
            []  # End pagination
        ]
        mock_get.return_value = mock_response

        pyscript.fetch_all_issues_with_status()

        output = mock_stdout.getvalue()
        self.assertIn("Issue #1: Issue A [open]", output)
        self.assertIn("Issue #2: Issue B [closed]", output)

    @patch("pyscript.requests.get")
    @patch('sys.stdout', new_callable=StringIO)
    def test_fetch_issues_error(self, mock_stdout, mock_get):
        mock_get.side_effect = requests.exceptions.Timeout("Request timeout")

        pyscript.fetch_all_issues_with_status()

        output = mock_stdout.getvalue()
        self.assertIn("An error occurred while fetching issues:", output)

    @patch("pyscript.requests.get")
    @patch('sys.stdout', new_callable=StringIO)
    def test_fetch_pull_requests_success(self, mock_stdout, mock_get):
        mock_response = Mock()
        mock_response.raise_for_status = Mock()
        mock_response.json.side_effect = [
            [{"number": 10, "title": "Fix bug", "state": "closed"}],
            []  # End pagination
        ]
        mock_get.return_value = mock_response

        pyscript.fetch_pull_requests()

        output = mock_stdout.getvalue()
        self.assertIn("All Pull Requests:", output)
        self.assertIn("PR #10: Fix bug [closed]", output)

    @patch("pyscript.requests.get")
    @patch('sys.stdout', new_callable=StringIO)
    def test_fetch_pull_requests_multiple_pages(self, mock_stdout, mock_get):
        mock_response = Mock()
        mock_response.raise_for_status = Mock()
        mock_response.json.side_effect = [
            [{"number": 10, "title": "Fix bug", "state": "closed"}],
            [{"number": 11, "title": "Add feature", "state": "open"}],
            []  # End pagination
        ]
        mock_get.return_value = mock_response

        pyscript.fetch_pull_requests()

        output = mock_stdout.getvalue()
        self.assertIn("PR #10: Fix bug [closed]", output)
        self.assertIn("PR #11: Add feature [open]", output)

    @patch("pyscript.requests.get")
    @patch('sys.stdout', new_callable=StringIO)
    def test_fetch_pull_requests_error(self, mock_stdout, mock_get):
        mock_get.side_effect = requests.exceptions.HTTPError("Bad Request")

        pyscript.fetch_pull_requests()

        output = mock_stdout.getvalue()
        self.assertIn("An error occurred while fetching pull requests:", output)

    @patch("pyscript.fetch_commits_and_print_specific_commit_detail")
    @patch("pyscript.fetch_all_issues_with_status")
    @patch("pyscript.fetch_pull_requests")
    def test_main_function(self, mock_pr, mock_issues, mock_commits):
        pyscript.main()

        mock_commits.assert_called_once()
        mock_issues.assert_called_once()
        mock_pr.assert_called_once()


if __name__ == "__main__":
    unittest.main()