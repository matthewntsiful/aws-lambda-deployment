# AWS Lambda Deployment

[![Deploy AWS Lambda](https://github.com/matthewntsiful/aws-lambda-deployment/actions/workflows/lambda.yml/badge.svg)](https://github.com/matthewntsiful/aws-lambda-deployment/actions/workflows/lambda.yml)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.x-blue)](https://www.python.org/)
[![AWS Lambda](https://img.shields.io/badge/AWS-Lambda-orange.svg)](https://aws.amazon.com/lambda/)
[![Serverless](https://img.shields.io/badge/serverless-ready-brightgreen.svg)](https://aws.amazon.com/lambda/)
[![Maintenance](https://img.shields.io/badge/maintained-yes-green.svg)](https://github.com/Matthieu/aws-lambda-deployment/commits/main)

## Table of Contents

- [Overview](#overview)
- [Motivation](#motivation)
- [Prerequisites](#prerequisites)
- [Project Structure](#project-structure)
- [Lambda Function Details](#lambda-function-details)
- [GitHub Actions Workflow](#github-actions-workflow)
- [Setup & Usage](#setup--usage)
- [Testing the Lambda Function](#testing-the-lambda-function)
- [Troubleshooting](#troubleshooting)
- [License](#license)
- [Automated Dependency Updates](#automated-dependency-updates)

## Overview

This project demonstrates a fully automated CI/CD pipeline for deploying an AWS Lambda function using GitHub Actions. It is designed for serverless workloads and rapid iteration.

## Motivation

Automating Lambda deployments reduces manual errors, speeds up development, and ensures consistent releases. This template helps you:

- Package and deploy Python Lambda functions
- Use GitHub Actions for CI/CD
- Integrate with AWS securely using GitHub secrets

## Prerequisites

- AWS account with permissions to update Lambda functions
- AWS CLI configured (for manual testing)
- GitHub repository with the following secrets set:
  - `AWS_ACCESS_KEY_ID`
  - `AWS_SECRET_ACCESS_KEY`
  - `AWS_REGION`
  - `LAMBDA_FUNCTION_NAME`

## Project Structure

```text
aws-lambda-deployment/
├── LICENSE
├── README.md
├── package/
│   └── lamda_function.py
└── .github/
    └── workflows/
        └── lamda.yml
```

## Lambda Function Details

The Lambda function is a simple Python handler that greets the user. You can extend it for your use case.

```python
import json

def lambda_handler(event, context):
    """
    AWS Lambda handler function.
    Parameters:
    - event (dict): The event data passed to the function.
    - context (object): Lambda context object.
    Returns:
    - dict: Response containing status code and body.
    """
    print("Received event:", json.dumps(event))
    name = event.get('name', 'World')
    message = f"Hello, {name}!"
    return {
        'statusCode': 200,
        'body': json.dumps({'message': message})
    }
```

## GitHub Actions Workflow

The workflow (`.github/workflows/lamda.yml`) performs the following steps:

- Checks out the code
- Sets up Python
- Installs dependencies (e.g., boto3)
- Packages the Lambda function into a zip file
- Configures AWS credentials using repository secrets
- Deploys the zip to AWS Lambda using the AWS CLI

## Setup & Usage

1. **Fork or clone this repository.**
2. **Set up GitHub secrets** as described in [Prerequisites](#prerequisites).
3. **Edit your Lambda function** in `package/lamda_function.py` as needed.
4. **Push changes to the `main` branch**. The workflow will run automatically and deploy your function.

## Testing the Lambda Function

You can test your Lambda function via the AWS Console or AWS CLI:

```bash
aws lambda invoke \
  --function-name <YOUR_FUNCTION_NAME> \
  --payload '{"name": "Alice"}' \
  response.json
cat response.json
```

Expected output:

```json
{"statusCode": 200, "body": "{\"message\": \"Hello, Alice!\"}"}
```

## Troubleshooting

- **Workflow fails at AWS CLI step:** Check that your AWS credentials and region are correct and have sufficient permissions.
- **Lambda not updating:** Ensure the function name in your secrets matches the actual Lambda function.
- **Dependencies not found:** Add any required packages to the `pip install` step in the workflow.

## Automated Dependency Updates

This repository uses [Dependabot](https://docs.github.com/en/code-security/supply-chain-security/keeping-your-dependencies-updated-automatically/about-dependabot-version-updates) to keep dependencies up to date automatically.

Dependabot is configured to monitor:

- **GitHub Actions workflows**: Checks for updates to GitHub Actions used in your workflows every week.
- **Python (pip) dependencies**: Checks for updates to Python packages in the `/package/` directory every week.

Configuration is managed in [`.github/dependabot.yml`](.github/dependabot.yml):

```yaml
version: 2
updates:
  - package-ecosystem: "github-actions"
    directory: "/"
    schedule:
      interval: "weekly"
    open-pull-requests-limit: 5
    commit-message:
      prefix: "chore"
      include: "scope"
  - package-ecosystem: "pip"
    directory: "/package/"
    schedule:
      interval: "weekly"
    open-pull-requests-limit: 5
    commit-message:
      prefix: "chore"
      include: "scope"
```

When updates are available, Dependabot will automatically open pull requests to keep your dependencies secure and up to date.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
