# Private Terraform Registry

Terraform 0.11 and above support [Private Module Registries][module-registry-protocol].

## Registry Protocol

APIs for Terraform to download modules.

```http
HTTP/1.1 204 No Content
Content-Length: 0
X-Terraform-Get: https://api.github.com/repos/hashicorp/terraform-aws-consul/tarball/v0.0.1//*?archive=tar.gz

```

## DynamoDB Data

Example

| pk                                  | sk              |
| ----------------------------------- | --------------- |
| `NAMESPACE#foo#NAME#bar#SYSTEM#aws` | `VERSION#1.0.0` |
| `NAMESPACE#foo#NAME#bar#SYSTEM#aws` | `VERSION#1.0.1` |
| `NAMESPACE#foo#NAME#baz#SYSTEM#aws` | `VERSION#1.0.1` |

## Registry API

Browse and Discover Terraform modules that exist in your registry.

## GitHub Integration

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
