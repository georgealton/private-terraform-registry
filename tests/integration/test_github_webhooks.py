from pathlib import Path
from urllib.parse import urljoin

import pytest
import requests

BASE_URL = "https://terraform.georgealton.com"
default_headers = {
    "Content-Type": "application/json",
}


class TestGitHubWebHooks:
    def test_app_installed(self, request):
        path = "webhooks/github"
        url = urljoin(BASE_URL, path)
        data = request.path.parent / "data/github/events/body-app-installation.json"
        github_event_header = {"X-GITHUB-EVENT": "repository"}
        headers = default_headers | github_event_header
        response = requests.post(
            url, data=data.read_text(), headers=headers, timeout=30
        )
        assert response.status_code == 202

    def test_repository_tag_added(self, request):
        path = "webhooks/github"
        url = urljoin(BASE_URL, path)
        data = request.path.parent / "data/github/events/body-tag-added.json"
        github_event_header = {"X-GITHUB-EVENT": "repository"}
        headers = default_headers | github_event_header
        response = requests.post(
            url, data=data.read_text(), headers=headers, timeout=30
        )
        assert response.status_code == 202

    def test_repository_created(self, request):
        path = "webhooks/github"
        url = urljoin(BASE_URL, path)
        data = request.path.parent / "data/github/events/body-repository-created.json"
        github_event_header = {"X-GITHUB-EVENT": "repository"}
        headers = default_headers | github_event_header
        response = requests.post(
            url, data=data.read_text(), headers=headers, timeout=30
        )
        assert response.status_code == 202

    def test_repository_deleted(self, request):
        path = "webhooks/github"
        url = urljoin(BASE_URL, path)
        data = request.path.parent / "data/github/events/body-repository-deleted.json"
        github_event_header = {"X-GITHUB-EVENT": "repository"}
        headers = default_headers | github_event_header
        response = requests.post(
            url, data=data.read_text(), headers=headers, timeout=30
        )
        assert response.status_code == 202
