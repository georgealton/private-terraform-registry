#!/bin/bash
aws cloudformation package --template template.yaml --s3-bucket cf-templates-1491x2vk47ot9-eu-west-1 --output-template-file packaged-template.json
aws cloudformation deploy --template-file packaged-template.json --stack-name private-terraform-registry --capabilities CAPABILITY_NAMED_IAM

# When we list versions for a module
#     the api returns a list of versions
curl -q https://i69k0wcgvg.execute-api.eu-west-1.amazonaws.com/main/terraform/modules/v1/A/B/C/versions | jq
# When we request to download a version of a modules
# The API returns terraform protocol
curl -v https://i69k0wcgvg.execute-api.eu-west-1.amazonaws.com/main/terraform/modules/v1/A/B/C/1.0.0/download
# The API returns a 404 and errors if the version does not exist
curl -v https://i69k0wcgvg.execute-api.eu-west-1.amazonaws.com/main/terraform/modules/v1/A/B/C/0.0.0/download
