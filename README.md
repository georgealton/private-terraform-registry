# Private Terraform Registry

Terraform 0.11 and above support [Private Module Registries][module-registry-protocol].

https://www.terraform.io/cloud-docs/registry/publish-modules#publishing-private-modules-to-the-terraform-cloud-private-registry

## OpenAPI

use well known / hardcoded resource arns over imports
- though breaks the dependency graph trade off is open api spec not coupled to CloudFormation


## Registry Protocol

APIs for Terraform to download modules.

```http
HTTP/1.1 204 No Content
Content-Length: 0
X-Terraform-Get: https://api.github.com/repos/hashicorp/terraform-aws-consul/tarball/v0.0.1//*?archive=tar.gz

```

## DynamoDB Data

### Module Versions

| pk                                  | sk              | data                                     |
| ----------------------------------- | --------------- | ---------------------------------------- |
| `NAMESPACE#foo#NAME#bar#SYSTEM#aws` | `VERSION#1.0.0` | {version: "1.0.0", url: "https://blah/"} |
| `NAMESPACE#foo#NAME#bar#SYSTEM#aws` | `VERSION#1.0.1` | {version: "1.0.1", url: "https://blah/"} |
| `NAMESPACE#foo#NAME#baz#SYSTEM#aws` | `VERSION#1.0.1` | {version: "1.0.1", url: "https://blah/"} |

## Registry API

Browse and Discover Terraform modules that exist in your registry.

## GitHub Integration

must follow

https://www.terraform.io/cloud-docs/registry/publish-modules#preparing-a-module-repository

- When installed
  - create new namespace from Org name
  - add all `terraform-` repositories under `name`
- When uninstalled remove
  - namespace and related
- When new terraform repo is added
  - create new name
  - create all versions from tags
- When new tag is added create new version

Resources to connect your private module registry with a GitHub Account or Organization.

Test

https://webhook.site/41eda23e-69ad-4fc7-8193-d888231a152d

[module-registry-protocol]: https://www.terraform.io/internals/module-registry-protocol
[registry-api]: https://www.terraform.io/registry/api-docs
