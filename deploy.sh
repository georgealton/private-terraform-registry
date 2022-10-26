#!/bin/sh

TEMPLATE='template.yaml'
BUCKET='cf-templates-1491x2vk47ot9-eu-west-1'
OUTPUT_TEMPLATE='packaged-template'
aws cloudformation package \
    --template "$TEMPLATE" \
    --s3-bucket "$BUCKET" \
    --output-template-file "$OUTPUT_TEMPLATE"

STACK='private-terraform-registry'
PARAMETERS_FILE='parameters.json'
aws cloudformation deploy \
    --template-file "$OUTPUT_TEMPLATE" \
    --stack-name "$STACK" \
    --capabilities 'CAPABILITY_NAMED_IAM' \
    --no-fail-on-empty-changeset \
    --parameter-overrides "file://${PARAMETERS_FILE}"
