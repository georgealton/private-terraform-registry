from mimetypes import types_map
from http import HTTPStatus
from urllib.parse import urljoin

import requests

CONTENT_TYPE = types_map[".json"]


class TestServiceDiscovery:
    def test_returns_modules_url(self, host):
        path = ".well-known/terraform.json"
        url = urljoin(f"https://{host}", path)
        response = requests.get(url, timeout=30)
        body = response.json()
        assert response.status_code == HTTPStatus.OK
        assert response.headers["Content-Type"] == CONTENT_TYPE
        assert body["modules.v1"] == urljoin(f"https://{host}", "terraform/modules/v1/")


class TestListModuleVersions:
    def test_returns_a_list_of_versions(self, host):
        MODULES_V1_URL = urljoin(f"https://{host}", "terraform/modules/v1/")
        path = "a/b/c/versions"
        url = urljoin(MODULES_V1_URL, path)
        response = requests.get(url, timeout=30)
        body = response.json()
        assert response.status_code == HTTPStatus.OK
        assert response.headers["Content-Type"] == CONTENT_TYPE
        assert body == {"modules": [{"versions": [{"version": "1.0.0"}]}]}

    def test_returns_404_when_there_are_no_module_versions(self, host):
        MODULES_V1_URL = urljoin(f"https://{host}", "terraform/modules/v1/")
        path = "x/x/x/versions"
        url = urljoin(MODULES_V1_URL, path)
        response = requests.get(url, timeout=30)
        response_data = response.json()
        assert response.status_code == HTTPStatus.NOT_FOUND
        assert response_data == {"errors": ["Not Found"]}


class TestDownloadModuleVersion:
    def test_returns_x_terraform_get_header(self, host):
        MODULES_V1_URL = urljoin(f"https://{host}", "terraform/modules/v1/")
        path = "a/b/c/1.0.0/download"
        url = urljoin(MODULES_V1_URL, path)
        response = requests.get(url, timeout=30)
        assert response.status_code == HTTPStatus.NO_CONTENT
        assert response.headers["X-TERRAFORM-GET"] == "http://localhost:8000/src.tgz"
        assert response.headers["Content-Length"] == "0"

    def test_returns_404_error_when_module_version_does_not_exist(self, host):
        MODULES_V1_URL = urljoin(f"https://{host}", "terraform/modules/v1/")
        path = "a/b/c/0.0.0/download"
        url = urljoin(MODULES_V1_URL, path)
        response = requests.get(url, timeout=30)
        assert response.status_code == HTTPStatus.NOT_FOUND
        assert response.headers["Content-Type"] == CONTENT_TYPE
