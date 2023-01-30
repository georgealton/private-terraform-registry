import requests

BASE_URL = "https://terraform.georgealton.com"


class TestListModuleVersions:
    def test_returns_a_list_of_versions(self):
        url = f"{BASE_URL}/terraform/modules/v1/A/B/C/versions"
        response = requests.get(url)
        assert response.status_code == 200

    def test_returns_404_when_there_are_no_module_versions(self):
        url = f"{BASE_URL}/terraform/modules/v1/X/X/X/versions"
        response = requests.get(url, timeout=30)
        response_data = response.json()
        assert response.status_code == 404
        assert response_data == {"errors": ["Not Found"]}


class TestDownloadModuleVersion:
    def test_returns_x_terraform_get_header(self):
        url = f"{BASE_URL}/terraform/modules/v1/A/B/C/1.0.0/download"
        response = requests.get(url)
        assert response.status_code == 200
        assert response.headers["X-TERRAFORM-GET"] == ""

    def test_returns_404_error_when_module_version_does_not_exist(self):
        url = f"{BASE_URL}/terraform/modules/v1/A/B/C/0.0.0/download"
        response = requests.get(url)
        assert response.status_code == 200
