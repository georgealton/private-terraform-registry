import json

from pathlib import Path

import boto3
import pytest
import requests


@pytest.fixture()
def parameters(request):
    parameters_file = request.path.parent.parent.parent / "parameters.json"
    param_data = json.loads(parameters_file.read_text())
    return {
        parameter["ParameterKey"]: parameter["ParameterValue"]
        for parameter in param_data
    }


@pytest.fixture
def host(parameters):
    yield f"{parameters['DomainName']}.{parameters['ParentDomain']}"


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
