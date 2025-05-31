import requests

OWNER = "ursARahim"
REPO = "dev_resources"
BASE_URL = f"https://api.github.com/repos/{OWNER}/{REPO}"
PER_PAGE = 100

def fetch_commits_and_print_specific_commit_detail():
    try:
        url = f"{BASE_URL}/commits"
        response = requests.get(url)
        response.raise_for_status()
        commits = response.json()
        
        if commits:
            latest_commit = commits[0]
            sha = latest_commit['sha']
            author = latest_commit['commit']['author']['name']
            message = latest_commit['commit']['message']
            date = latest_commit['commit']['author']['date']
            
            print("Latest Commit:")
            print(f"SHA: {sha}")
            print(f"Author: {author}")
            print(f"Message: {message}")
            print(f"Date: {date}")
        else:
            print("No commits found.")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching commits: {e}")

def fetch_all_issues_with_status():
    try:
        print("\nAll Issues:")
        page = 1
        while True:
            url = f"{BASE_URL}/issues"
            response = requests.get(url, params={"state": "all", "per_page": PER_PAGE, "page": page})
            response.raise_for_status()
            issues = response.json()

            if not issues:
                break

            for issue in issues:
                if 'pull_request' in issue:
                    continue
                number = issue['number']
                title = issue['title']
                state = issue['state']
                print(f"Issue #{number}: {title} [{state}]")

            page += 1

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching issues: {e}")

def fetch_pull_requests():
    try:
        print("\nAll Pull Requests:")
        page = 1
        while True:
            url = f"{BASE_URL}/pulls"
            response = requests.get(url, params={"state": "all", "per_page": PER_PAGE, "page": page})
            response.raise_for_status()
            pull_requests = response.json()

            if not pull_requests:
                break

            for pr in pull_requests:
                number = pr['number']
                title = pr['title']
                state = pr['state']
                print(f"PR #{number}: {title} [{state}]")

            page += 1

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching pull requests: {e}")

if __name__ == "__main__":
    fetch_commits_and_print_specific_commit_detail()
    fetch_all_issues_with_status()
    fetch_pull_requests()
