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
    "X-GITHUB-EVENT:repository" "CONTENT-TYPE:application/json" '@data/github/events/body-tag-added.json'
# http --follow "${BASE_URL}/webhooks/github" "X-GITHUB-EVENT:repository" "CONTENT-TYPE:application/json" '@data/github-repository-created.json'
# http --follow "${BASE_URL}/webhooks/github" "X-GITHUB-EVENT:installation" "CONTENT-TYPE:application/json" '@data/github-app-installation.json'
