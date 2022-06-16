#!/bin/bash

aws cloudformation package \
    --template template.yaml \
    --s3-bucket cf-templates-1491x2vk47ot9-eu-west-1 \
    --output-template-file packaged-template.json

aws cloudformation deploy \
    --template-file packaged-template.json \
    --stack-name private-terraform-registry \
    --capabilities CAPABILITY_NAMED_IAM \
    --no-fail-on-empty-changeset

BASE_URL=https://i69k0wcgvg.execute-api.eu-west-1.amazonaws.com/main

###
echo "When we list versions for a module"
echo "    The api returns a list of versions"
http "${BASE_URL}/terraform/modules/v1/A/B/C/versions"
echo "    The api returns 404 when there are no versions"
http "${BASE_URL}/terraform/modules/v1/X/X/X/versions"
####

####
echo "When we request to download a version of a modules"
echo "   The API returns the X-TERRAFORM-GET header"
http "${BASE_URL}/terraform/modules/v1/A/B/C/1.0.0/download"
echo "   The API returns a 404 and errors if the version does not exist"
http "${BASE_URL}/terraform/modules/v1/A/B/C/0.0.0/download"
####

http "${BASE_URL}/webhooks/github" "X-GITHUB-EVENT:repository" "CONTENT-TYPE:application/json" '@data/github-repository-created.json'
http "${BASE_URL}/webhooks/github" "X-GITHUB-EVENT:installation" "CONTENT-TYPE:application/json" '@data/github-app-installation.json'
