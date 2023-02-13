import json

from pathlib import Path

import boto3
import pytest
import docker


@pytest.fixture()
def docker_client():
    yield docker.from_env()


@pytest.fixture()
def terraform(docker_client):
    container = docker_client.containers.run(
        "hashicorp/terraform",
        detach=True,
    )
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
