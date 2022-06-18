#!/bin/sh

aws cloudformation package \
    --template 'template.yaml' \
    --s3-bucket 'cf-templates-1491x2vk47ot9-eu-west-1' \
    --output-template-file 'packaged-template.json'

aws cloudformation deploy \
    --template-file 'packaged-template.json' \
    --stack-name 'private-terraform-registry' \
    --capabilities 'CAPABILITY_NAMED_IAM' \
    --disable-rollback \
    --no-fail-on-empty-changeset \
    --parameter-overrides 'file://parameters.json'

BASE_URL='https://terraform.georgealton.com'

###
echo "When we list versions for a module"
echo "The api returns a list of versions"
http --follow "${BASE_URL}/terraform/modules/v1/A/B/C/versions"
echo "The api returns 404 when there are no versions"
http --follow "${BASE_URL}/terraform/modules/v1/X/X/X/versions"
####

####
echo "When we request to download a version of a modules"
echo "The API returns the X-TERRAFORM-GET header"
http --follow "${BASE_URL}/terraform/modules/v1/A/B/C/1.0.0/download"
echo "The API returns a 404 and errors if the version does not exist"
http --follow "${BASE_URL}/terraform/modules/v1/A/B/C/0.0.0/download"
####

http --follow "${BASE_URL}/webhooks/github" "X-GITHUB-EVENT:repository" "CONTENT-TYPE:application/json" '@data/github/tag-added.json'
# http --follow "${BASE_URL}/webhooks/github" "X-GITHUB-EVENT:repository" "CONTENT-TYPE:application/json" '@data/github-repository-created.json'
# http --follow "${BASE_URL}/webhooks/github" "X-GITHUB-EVENT:installation" "CONTENT-TYPE:application/json" '@data/github-app-installation.json'
