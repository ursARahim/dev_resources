import requests

OWNER = "ursARahim"
REPO = "dev_resources"

GITHUB_API_URL = f"https://api.github.com/repos/{OWNER}/{REPO}/commits"

def fetch_commits():
    try:
        response = requests.get(GITHUB_API_URL)
        response.raise_for_status()
        commits = response.json()
        
        if commits:
            latest_commit = commits[0]
            sha = latest_commit['sha']
            author = latest_commit['commit']['author']['name']
            message = latest_commit['commit']['message']
            date = latest_commit['commit']['author']['date']
            
            print(f"SHA: {sha}")
            print(f"Author: {author}")
            print(f"Message: {message}")
            print(f"Date: {date}")
        else:
            print("No commits found.")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching commits: {e}")
        
if __name__ == "__main__":
    fetch_commits()
            