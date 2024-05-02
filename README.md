# APIsec|SCAN - Github Action: Free! Dynamic API Security Testing

APIsec|Scan - Github Action is a free, self-service CI/CD tool created by the founders of [APIsec University](https://www.apisecuniversity.com/) that provides immediate analysis of APIs and insight into security issues and vulnerabilities by dynamically testing APIs. They created APIsec U to offer high quality API security courses accessible to anyone. The incredible success of the courses led to many other offerings, including monthly webinars, private API security workshops, and [APISEC|CON](https://conf.apisecuniversity.com/). It became clear that people could use a simple, effective API testing utility to analyze spec files, identify vulnerabilities, and provide other useful insight.

The **Dynamic API security testing** performs live calls to your API and analyzes the responses. With this action you can:

- Summarize server configurations and identify potential security issues
- Analyze Response Headers
- Identify Authentication Gaps
- Look for potential security vulnerabilities

With this tool integrated into your CI/CD process, you can detect security vulnerabilities, especially those identified as being part of the [OWASP API Security Top 10](https://apisecurity.io/owasp-api-security-top-10/owasp-api-security-top-10-project/), before they affect your customers.

![](https://img.shields.io/badge/WARNING-Not_suitable_for_production-blue) The CI/CD action generates live traffic to the API configured for security scanning. While the tool does not generate any data that it tries to persist using the APIs, the extra traffic can lead to unintended consequences.

## How to use this action?

##### To use this action, all you need is an OpenAPI specification and an API to test!

Below are the parameters you configure to customize the behavior of the Dynamic Testing.

### `base_url` - ![](https://img.shields.io/badge/Required-red)

The primary URL of the API you are trying to test. For example: https://myawesomeapi.com

NOTE: If your OpenAPI specification contains a fixed base path other than `/` please include that as part of the base url. For example, if all your APIs are hosted under a base path of `v1` AND the paths in your OpenAPI specification do not contain this path, set this parameter to `https://myawesomeapi.com/v1`

### `specification_path` - ![](https://img.shields.io/badge/Required-red)

The name of the OpenAPI specification along with the relative path in the github repository.
If the OpenAPI specification file, for example, `openapi.json`, is in the root of the repository, set this parameter to `openapi.json`. If it is nested under a different directory, specify the complete path set it to `<directory-name>/openapi.json`.

NOTE: The action accepts JSON and YAML representations of the OpenAPI specification.

### `apisecu_token` - ![](https://img.shields.io/badge/Required-red)

The token obtained from apisec university to configure the action. Visit `https://www.apisecuniversity.com/api-tools-and-resources/cicd` to obtain a token.

### `enable_info` - ![](https://img.shields.io/badge/Optional-blue)

By default, this action presents results for all severities, which includes ERROR, WARN and INFO. Set this parameter to `False` to trim the results to only ERROR and WARN.

### `fail_on_error_threshold` - ![](https://img.shields.io/badge/Optional-blue)

By default, this action does not fail if security vulnerabilities are detected. To fail this action, for example, to stop a deploy workflow on the occurrence of vulnerabilities classified as ERRORS, set this parameter to valid threshold eg. `2`. If the number of vulnerabilities with severity ERROR match of exceed this threshold, the action will fail and notify the owners of the repository.

## Integrate this action

You can use this action on an existing Github Workflow or create a new one exclusively to run APIsec|SCAN.

For example, to run scans as a standalone workflow, you can the following defintion:

```
name: "APIsec|SCAN - Dynamic API Security Testing"

on:
  workflow_dispatch:
  push:
    branches: ["main"]

jobs:
  test_scan:
    permissions:
      contents: read # to checkout repository code
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
      - name: APISec|SCAN Testing
        uses: apisec-university/free-API-security-test-action@beta
        with:
          base_url: "<your-base-url-goes-here>"
          specification_path: "<your-openapi-specification-file-goes-here>"
          apisecu_token: "<your-token-provided-by-apisec-university-goes-here>"
```

## Limitations

This is a free to use version from the suite of APIsec suite of testing tools. To use this tool effectively ensure:

1. Your APIs are reachable from the Github Hosted Runner this action is executed on.
   - If using the Public Hosted Runners, no additional configuration is needed as long as the hosted runner can communicate with your APIs
   - If using the Private Hosted Runners, ensure that is uses Ubuntu as the Operating system and has Docker installed in addition to having access to your APIs.

## Support

Please feel free to open new Issues on this Github repository. The owners are active maintainers and will be more than happy to assist you.

## Learn More

To learn more about APIsec visit https://www.apisec.ai

## Terms and Conditions of usage

Please visit https://www.apisec.ai/terms-and-conditions for terms and conditions of usage.
