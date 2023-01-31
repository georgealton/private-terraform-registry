from mimetypes import types_map
from http import HTTPStatus
import requests

BASE_URL = "https://terraform.georgealton.com"
CONTENT_TYPE = types_map[".json"]


class TestServiceDiscovery:
    def test_returns_modules_url(self):
        url = f"{BASE_URL}/.well-known/terraform.json"
        response = requests.get(url)
        body = response.json()
        assert response.status_code == HTTPStatus.OK
        assert response.headers["Content-Type"] == CONTENT_TYPE
        assert body["modules.v1"] == f"{BASE_URL}/terraform/modules/v1/"}


class TestListModuleVersions:
    def test_returns_a_list_of_versions(self):
        url = f"{BASE_URL}/terraform/modules/v1/A/B/C/versions"
        response = requests.get(url)
        assert response.status_code == HTTPStatus.OK
        assert response.headers["Content-Type"] == CONTENT_TYPE

    def test_returns_404_when_there_are_no_module_versions(self):
        url = f"{BASE_URL}/terraform/modules/v1/X/X/X/versions"
        response = requests.get(url)
        response_data = response.json()
        assert response.status_code == HTTPStatus.NOT_FOUND
        assert response_data == {"errors": ["Not Found"]}


class TestDownloadModuleVersion:
    def test_returns_x_terraform_get_header(self):
        url = f"{BASE_URL}/terraform/modules/v1/A/B/C/1.0.0/download"
        response = requests.get(url)
        assert response.status_code == HTTPStatus.NO_CONTENT
        assert response.headers["X-TERRAFORM-GET"] == ""
        assert response.headers["Content-Length"] == "0"

    def test_returns_404_error_when_module_version_does_not_exist(self):
        url = f"{BASE_URL}/terraform/modules/v1/A/B/C/0.0.0/download"
        response = requests.get(url)
        assert response.status_code == HTTPStatus.NOT_FOUND
        assert response.headers["Content-Type"] == CONTENT_TYPE
