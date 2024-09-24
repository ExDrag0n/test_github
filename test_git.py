import os
from dotenv import load_dotenv
import requests


def create_repository():
    url = f"https://api.github.com/user/repos"

    headers = {
        "Authorization": f"token {os.getenv('GITHUB_TOKEN')}",
        "Accept": "application/vnd.github.v3+json"
    }

    data = {
        "name": os.getenv('REPO_NAME'),
        "description": "Test repository",
        "private": False,
        "auto_init": True
    }

    response = requests.post(url, json=data, headers=headers)

    return response.status_code == 201


def check_repository_exists():
    url = f"https://api.github.com/repos/{os.getenv('GITHUB_USERNAME')}/{os.getenv('REPO_NAME')}"

    headers = {
        "Authorization": f"token {os.getenv('GITHUB_TOKEN')}",
        "Accept": "application/vnd.github.v3+json"
    }

    response = requests.get(url, headers=headers)

    return response.status_code == 200


def delete_repository():
    url = f"https://api.github.com/repos/{os.getenv('GITHUB_USERNAME')}/{os.getenv('REPO_NAME')}"

    headers = {
        "Authorization": f"token {os.getenv('GITHUB_TOKEN')}",
        "Accept": "application/vnd.github.v3+json"
    }

    response = requests.delete(url, headers=headers)

    return response.status_code == 204


def test_github():
    assert create_repository(), "Failed to create repository"
    assert check_repository_exists(), "Repository does not exist"
    assert delete_repository(), "Failed to delete repository"


if __name__ == "__main__":
    load_dotenv()
    test_github()
    print("All tests passed!")
