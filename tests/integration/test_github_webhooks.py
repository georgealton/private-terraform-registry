from urllib.parse import urljoin
from pathlib import Path

import requests

DEFAULT_HEADERS = {"Content-Type": "application/json"}
EVENT_DATA = Path("data/github/events")


def prepare_post(request, parameters, event_filename, event_type):
    host = f"{parameters['DomainName']}.{parameters['ParentDomain']}"
    endpoint = "webhooks/github"
    url = urljoin(f"https://{host}", endpoint)
    data_path = request.path.parent / EVENT_DATA / event_filename
    data = data_path.read_bytes()
    github_event_header = {"X-GITHUB-EVENT": event_type}
    headers = DEFAULT_HEADERS | github_event_header
    return url, data, headers


class TestGitHubWebHooks:
    def test_app_installed(self, parameters, request):
        filename = "body-app-installation.json"
        url, data, headers = prepare_post(request, parameters, filename, "repository")
        response = requests.post(url, data=data, headers=headers, timeout=30)
        assert response.status_code == 202

    def test_repository_tag_added(self, parameters, request):
        filename = "body-tag-added.json"
        url, data, headers = prepare_post(request, parameters, filename, "repository")
        response = requests.post(url, data=data, headers=headers, timeout=30)
        assert response.status_code == 202

    def test_repository_created(self, parameters, request):
        filename = "body-repository-created.json"
        url, data, headers = prepare_post(request, parameters, filename, "repository")
        response = requests.post(url, data=data, headers=headers, timeout=30)
        assert response.status_code == 202

    def test_repository_deleted(self, parameters, request):
        filename = "body-repository-deleted.json"
        url, data, headers = prepare_post(request, parameters, filename, "repository")
        response = requests.post(url, data=data, headers=headers, timeout=30)
        assert response.status_code == 202
