import json
from pathlib import Path

import boto3


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
