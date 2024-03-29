# Private Terraform Registry

An extensible, self hosted, private terraform registry without the expense of
terraform cloud.

Why would I want a module registry?

## Version Management

You can reference modules using `github.com/georgealton/example?ref=v1.0.0` but
terraform won't be able to perform version management here. Dependabot should be
able to do this too.

## Discoverability

If all your modules are in git repositories they can be hard to discover a
private registry makes them easier to browse and discover

## Adaptability

Centralizing the location of your modules means that they're abstracted away
from the VCS provider.

Terraform 0.11 and above support [Private Module
Registries][module-registry-protocol].

[publishing-private-modules]

## Installation

### Certificate Domain Verification

## OpenAPI

use well known resource arns over imports

- though breaks the dependency graph trade off is open api spec not coupled to
  CloudFormation -- Can supply iac in any format

## Registry Protocol

APIs for Terraform to download modules.

```http
HTTP/1.1 204
Content-Length: 0
X-Terraform-Get: https://api.github.com/repos/hashicorp/terraform-aws-consul/tarball/v0.0.1//*?archive=tar.gz
```

## DynamoDB Data

### Provider vs System

Terraform documentation uses provider and system for a module interchangeably.
I've opted to use provider because that seems more common in terraform
nomenclature.

## Terraform needs the values to be lowercase

### Module Versions (Primary Index)

Provides:

- Get Version
- List Versions

| pk              | sk                                   | data                                     |
| --------------- | ------------------------------------ | ---------------------------------------- |
| `NAMESPACE#foo` | `NAMESPACE#foo`                      |                                          |
| `NAMESPACE#foo` | `NAME#bar#PROVIDER#awsVERSION#1.0.0` | {version: "1.0.0", url: "https://blah/"} |
| `NAMESPACE#foo` | `NAME#bar#PROVIDER#awsVERSION#1.0.1` | {version: "1.0.1", url: "https://blah/"} |
| `NAMESPACE#foo` | `NAME#baz#PROVIDER#awsVERSION#1.0.1` | {version: "1.0.1", url: "https://blah/"} |

## Registry API

Browse and Discover Terraform modules that exist in your registry.

## Authentication

[terraform-cli-registry-auth][https://www.terraform.io/cli/config/config-file#credentials-1]
[https://www.terraform.io/cli/config/config-file#environment-variable-credentials]

```sh
TF_TOKEN_terraform_georgealton_com="_TOKEN_"
```

using the value from the `.terraformrc` or environment variable terraform put
the value into `Authorization: Bearer <value>`

## Module Registration

must follow

[preparing-a-module-repository]

## Events

### app.installed

```json
{
  "namespace": ""
}
```

### app.uninstalled

```json
{
  "namespace": ""
}
```

### module.created

```json
{
  "namespace": "",
  "name": ""
}
```

### module.deleted

```json
{
  "namespace": "",
  "name": ""
}
```

### module.version_released

```json
{
  "namespace": "",
  "name": "",
  "version": "",
  "url": ""
}
```

### module.version_revoked

```json
{
  "namespace": "",
  "name": "",
  "version": ""
}
```

### Domain Integration

- Supply a Certificate
- Generate an ACM certificate

### VCS Integration

## GitHub

- When installed
  - create new namespace from Org name
  - add all PREFIX `terraform-` repositories under `name`
    - allow a custom prefix
- When uninstalled remove
  - namespace and related
- When new terraform repo is added
  - create new name
  - create all versions from tags
- When new tag is added create new version

Resources to connect your private module registry with a GitHub Account or
Organization.

### Storage Backend

Q. Is separate Storage Backend Necessary? Can we rely on VCS access?

- Isolates Registry from VCS
- Adds Complexity to codebase
- Duplicates storage
- Simplifies Access Control?

## S3

[s3-bucket-source]

## ADR

We will store [ADR](./docs/adr/) to record major key architectural decisions
made with this project.

## Using State machine for API

experimented with VTL but became tricky to use with advanced use case, difficult
to extend and modify. It also enables use of the built in JWT authorizer.

switched to SFN instead.

- Easier to build integrations with than VTL
-

### Test

## User Access

Users should be able to browse the registry Don't want to manage Identity, so
should only support federation via SAML/OAUTH from an IdP

<https://www.samltool.com/sp_metadata.php>

##  Docs

[webhooks]: https://webhook.site/41eda23e-69ad-4fc7-8193-d888231a152d
[publishing-private-modules]:
  https://www.terraform.io/cloud-docs/registry/publish-modules#publishing-private-modules-to-the-terraform-cloud-private-registry
[preparing-a-module-repository]:
  https://www.terraform.io/cloud-docs/registry/publish-modules#preparing-a-module-repository
[module-registry-protocol]:
  https://www.terraform.io/internals/module-registry-protocol
[registry-api]: https://www.terraform.io/registry/api-docs
[s3-bucket-source]: https://www.terraform.io/language/modules/sources#s3-bucket
[module-structure]: https://www.terraform.io/language/modules/develop/structure
