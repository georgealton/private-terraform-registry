from pathlib import Path
from urllib.parse import urljoin

import pytest
import requests

BASE_URL = "https://terraform.georgealton.com"
default_headers = {
    "Content-Type": "application/json",
}


@pytest.mark.xfail(reason="Not Implemented")
class TestGitHubWebHooks:
    def test_repository_tag_added(self):
        url = urljoin(BASE_URL, "webhooks/github")
        data = Path("./data/github/events/body-tag-added.json")
        github_event_header = {"X-GITHUB-EVENT": "repository"}
        headers = default_headers | github_event_header
        response = requests.post(url, data=data.read_text(), headers=headers)
        assert response.status_code == 204

    def test_repository_created(self):
        url = urljoin(BASE_URL, "webhooks/github")
        data = Path("./data/github/events/body-repository-created.json")
        github_event_header = {"X-GITHUB-EVENT": "repository"}
        headers = default_headers | github_event_header
        response = requests.post(url, data=data.read_text(), headers=headers)
        assert response.status_code == 204

    def test_repository_deleted(self):
        url = urljoin(BASE_URL, "webhooks/github")
        data = Path("./data/github/events/body-repository-deleted.json")
        github_event_header = {"X-GITHUB-EVENT": "repository"}
        headers = default_headers | github_event_header
        response = requests.post(url, data=data.read_text(), headers=headers)
        assert response.status_code == 204

    def test_app_installed(self):
        url = urljoin(BASE_URL, "webhooks/github")
        data = Path("./data/github/events/body-app-installed.json")
        github_event_header = {"X-GITHUB-EVENT": "repository"}
        headers = default_headers | github_event_header
        response = requests.post(url, data=data.read_text(), headers=headers)
        assert response.status_code == 204
