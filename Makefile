BUILD_DIR := .build

TEMPLATE := template.yaml
BUILT_TEMPLATE := packaged.yaml
PARAMETERS_FILE := parameters.json

BUCKET ?= cf-templates-1491x2vk47ot9-eu-west-1
STACK_NAME ?= private-terraform-registry

.PHONY: clean deploy acceptance_test undeploy

${BUILD_DIR}:
	mkdir -p ${BUILD_DIR}

${BUILD_DIR}/${BUILT_TEMPLATE}: | ${BUILD_DIR}
	aws cloudformation package --template "${TEMPLATE}" --s3-bucket "${BUCKET}" --output-template-file "$@"

deploy: ${BUILD_DIR}/${BUILT_TEMPLATE}
	aws cloudformation deploy \
		--template-file "$^" \
		--stack-name "${STACK_NAME}" \
		--capabilities 'CAPABILITY_NAMED_IAM' \
		--no-fail-on-empty-changeset \
		--parameter-overrides "file://${PARAMETERS_FILE}"

undeploy:
	aws cloudformation delete-stack --stack-name "${STACK_NAME}"
	aws cloudformation wait stack-delete-complete --stack-name "${STACK_NAME}"

clean: undeploy
	rm -r ${BUILD_DIR}

acceptance_test: deploy
	pytest
