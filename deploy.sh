#!/bin/sh

# Build
TEMPLATE='template.yaml'
BUCKET='cf-templates-1491x2vk47ot9-eu-west-1'
STACK='private-terraform-registry'
OUTPUT_TEMAPLTE='packaged-template'


aws cloudformation package \
    --template "$TEMPLATE" \
    --s3-bucket "$BUCKET" \
    --output-template-file "$OUTPUT_TEMAPLTE"

aws cloudformation deploy \
    --template-file "$OUTPUT_TEMAPLTE" \
    --stack-name "$STACK" \
    --capabilities 'CAPABILITY_NAMED_IAM' \
    --disable-rollback \
    --no-fail-on-empty-changeset \
    --parameter-overrides 'file://parameters.json'

# Integration Test
BASE_URL="https://terraform.georgealton.com"
###
echo "When we list versions for a module"
echo "The api returns a list of versions"
http --ignore-stdin \
    --timeout 5 \
    --follow \
    "${BASE_URL}/terraform/modules/v1/A/B/C/versions"
echo "The api returns 404 when there are no versions"
http --ignore-stdin \
    --timeout 5 \
    --follow \
    "${BASE_URL}/terraform/modules/v1/X/X/X/versions"
####

####
echo "When we request to download a version of a modules"
echo "The API returns the X-TERRAFORM-GET header"
http --ignore-stdin \
    --timeout 5 \
    --follow \
    "${BASE_URL}/terraform/modules/v1/A/B/C/1.0.0/download"

echo "The API returns a 404 and errors if the version does not exist"
http --ignore-stdin \
    --timeout 5 \
    --follow \
    "${BASE_URL}/terraform/modules/v1/A/B/C/0.0.0/download"
####

http --ignore-stdin \
    --timeout 5 \
    --follow \
    "${BASE_URL}/webhooks/github" \
    "X-GITHUB-EVENT:repository" "CONTENT-TYPE:application/json" '@data/github/events/tag-added.json'
# http --follow "${BASE_URL}/webhooks/github" "X-GITHUB-EVENT:repository" "CONTENT-TYPE:application/json" '@data/github-repository-created.json'
# http --follow "${BASE_URL}/webhooks/github" "X-GITHUB-EVENT:installation" "CONTENT-TYPE:application/json" '@data/github-app-installation.json'
