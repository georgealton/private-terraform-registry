#!/bin/bash
aws cloudformation package --template template.yaml --s3-bucket cf-templates-1491x2vk47ot9-eu-west-1 --output-template-file packaged-template.json
aws cloudformation deploy --template-file packaged-template.json --stack-name private-terraform-registry --capabilities CAPABILITY_IAM
curl https://i69k0wcgvg.execute-api.eu-west-1.amazonaws.com/main/terraform/modules/v1/A/B/C/versions | jq
