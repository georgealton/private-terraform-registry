from urllib.parse import urljoin
from pathlib import Path
from typing import Any

import pytest
import requests

DEFAULT_HEADERS = {"Content-Type": "application/json"}
EVENT_DATA = Path("data/github/events")


def prepare_post(request, parameters, event_filename, event_type) -> tuple[str, dict[str, Any], dict[str, str]]:
    host = f"{parameters['DomainName']}.{parameters['ParentDomain']}"
    endpoint = "webhooks/github"
    url = urljoin(f"https://{host}", endpoint)
    data_path = request.path.parent / EVENT_DATA / event_filename
    data = data_path.read_bytes()
    github_event_header = {"X-GITHUB-EVENT": event_type}
    headers = DEFAULT_HEADERS | github_event_header
    return url, data, headers


class TestGitHubWebHooks:
    @pytest.mark.parametrize('filename', [
        "body-repository-deleted.json",
        "body-repository-created.json",
        "body-tag-added.json",
        "body-app-installation.json",
    ])
    def test_app_installed(self, parameters, request, filename):
        url, data, headers = prepare_post(request, parameters, filename, "repository")
        response = requests.post(url, data=data, headers=headers, timeout=30)
        assert response.status_code == 202
