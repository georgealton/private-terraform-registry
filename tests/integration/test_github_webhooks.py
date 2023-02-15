from urllib.parse import urljoin
from pathlib import Path

import requests

BASE_URL = "https://terraform.georgealton.com"
DEFAULT_HEADERS = {"Content-Type": "application/json"}
EVENT_DATA = Path("data/github/events")


class TestGitHubWebHooks:
    def test_app_installed(self, request):
        endpoint = "webhooks/github"
        url = urljoin(BASE_URL, endpoint)
        data_path = request.path.parent / EVENT_DATA / "body-app-installation.json"
        data = data_path.read_bytes()
        github_event_header = {"X-GITHUB-EVENT": "repository"}
        headers = DEFAULT_HEADERS | github_event_header

        response = requests.post(url, data=data, headers=headers, timeout=30)

        assert response.status_code == 202

    def test_repository_tag_added(self, request):
        endpoint = "webhooks/github"
        url = urljoin(BASE_URL, endpoint)
        data_path = request.path.parent / EVENT_DATA / "body-tag-added.json"
        data = data_path.read_bytes()
        github_event_header = {"X-GITHUB-EVENT": "repository"}
        headers = DEFAULT_HEADERS | github_event_header

        response = requests.post(url, data=data, headers=headers, timeout=30)

        assert response.status_code == 202

    def test_repository_created(self, request):
        endpoint = "webhooks/github"
        url = urljoin(BASE_URL, endpoint)
        data_path = request.path.parent / EVENT_DATA / "body-repository-created.json"
        data = data_path.read_bytes()
        github_event_header = {"X-GITHUB-EVENT": "repository"}
        headers = DEFAULT_HEADERS | github_event_header

        response = requests.post(url, data=data, headers=headers, timeout=30)

        assert response.status_code == 202

    def test_repository_deleted(self, request):
        endpoint = "webhooks/github"
        url = urljoin(BASE_URL, endpoint)
        data_path = request.path.parent / EVENT_DATA / "body-repository-deleted.json"
        data = data_path.read_bytes()
        github_event_header = {"X-GITHUB-EVENT": "repository"}
        headers = DEFAULT_HEADERS | github_event_header

        response = requests.post(url, data=data, headers=headers, timeout=30)

        assert response.status_code == 202
