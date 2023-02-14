import json

from pathlib import Path

import boto3
import pytest
import docker
import requests


@pytest.fixture()
def github_organization(request):
    """This uses a Private API -- gitHub doesn't allow creation of orgs. this has"""
    request.add_marker(pytest.mark.interactive)

    organization_name = "georgealton-test-org-5"
    user_session = ""
    gh_session = ""
    authenticity_token = ""
    billing_email = ""

    url = "https://github.com/organizations"
    cookies = {
        "__Host-user_session_same_site": user_session,
        "user_session": user_session,
        "_gh_sess": gh_session,
        "logged_in": "yes",
    }

    data = {
        "authenticity_token": authenticity_token,
        "organization[plan]": "free",
        "org_exists": "false",
        "organization[profile_name]": organization_name,
        "organization[login]": organization_name,
        "organization[billing_email]": billing_email,
        "terms_of_service_type": "standard",
        "organization[company_name]": "",
        "agreed_to_terms": "yes",
    }

    response = requests.post(url, data=data, cookies=cookies)


@pytest.fixture()
def docker_client():
    yield docker.from_env()


@pytest.fixture()
def terraform(docker_client):
    image = "hashicorp/terraform"
    container = docker_client.containers.run(image, detach=True)
    yield container
    container.remove(force=True)


def db_connection():
    table = "..."
    dynamodb = boto3.resource("dynamodb")
    yield dynamodb.Table(table)


def provisioner(table):
    items = Path("data/dynamodb/items.jsonl")
    with items.open() as items_file:
        with table.batch_writer() as batch:
            for json_line in items_file:
                item = json.loads(json_line)
                batch.put_item(Item=item)
    yield
