clean:
	rm packaged-template
	aws cloudformation delete-stack --stack-name private-terraform-registry
	aws cloudformation wait stack-delete-complete --stack-name private-terraform-registry

deploy:
	./deploy.sh

test: deploy
	./integration_test.sh
