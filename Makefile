BUILD_DIR := .build

TEMPLATE := template.yaml
BUILT_TEMPLATE = packaged.yaml
BUCKET := cf-templates-1491x2vk47ot9-eu-west-1
STACK := private-terraform-registry
PARAMETERS_FILE := parameters.json

.PHONY: clean deploy test

${BUILD_DIR}/$(BUILT_TEMPLATE):
	mkdir -p "${BUILD_DIR}"
	aws cloudformation package --template "${TEMPLATE}" --s3-bucket "${BUCKET}" --output-template-file "$@"

deploy: ${BUILD_DIR}/$(BUILT_TEMPLATE)
	aws cloudformation deploy --template-file "$^" --stack-name "${STACK}" --capabilities 'CAPABILITY_NAMED_IAM' --no-fail-on-empty-changeset --parameter-overrides "file://${PARAMETERS_FILE}"

clean:
	rm -r ${BUILD_DIR}
	aws cloudformation delete-stack --stack-name "${STACK}"
	aws cloudformation wait stack-delete-complete --stack-name "${STACK}"

test: deploy
	./integration_test.sh
