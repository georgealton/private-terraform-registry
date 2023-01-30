from pathlib import Path

import requests

BASE_URL = "https://terraform.georgealton.com"


class TestGitHubWebHooks:
    def test_repository_tag_added(self):
        url = f"{BASE_URL}/webhooks/github"
        data = Path("./data/github/events/body-tag-added.json")
        headers = {
            "X-GITHUB-EVENT": "repository",
            "Content-Type": "application/json",
        }
        response = requests.post(url, data=data, headers=headers)
        assert response

    def test_repository_created(self):
        url = f"{BASE_URL}/webhooks/github"
        data = Path("./data/github/events/body-repository-created.json")
        headers = {
            "X-GITHUB-EVENT": "repository",
            "Content-Type": "application/json",
        }
        response = requests.post(url, data=data.read_text(), headers=headers)
        assert response

    def test_repository_deleted(self):
        url = f"{BASE_URL}/webhooks/github"
        data = Path("./data/github/events/body-repository-deleted.json")
        headers = {
            "X-GITHUB-EVENT": "repository",
            "Content-Type": "application/json",
        }
        response = requests.post(url, data=data.read_text(), headers=headers)
        assert response

    def test_repository_deleted(self):
        url = f"{BASE_URL}/webhooks/github"
        data = Path("./data/github/events/body-app-installed.json")
        headers = {
            "X-GITHUB-EVENT": "installation",
            "Content-Type": "application/json",
        }
        response = requests.post(url, data=data.read_text(), headers=headers)
        assert response
