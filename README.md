# AWS Lambda Deployment

[![Deploy AWS Lambda](https://github.com/matthewntsiful/aws-lambda-deployment/actions/workflows/lambda.yml/badge.svg)](https://github.com/matthewntsiful/aws-lambda-deployment/actions/workflows/lambda.yml)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.x-blue)](https://www.python.org/)
[![AWS Lambda](https://img.shields.io/badge/AWS-Lambda-orange.svg)](https://aws.amazon.com/lambda/)
[![Serverless](https://img.shields.io/badge/serverless-ready-brightgreen.svg)](https://aws.amazon.com/lambda/)
[![Maintenance](https://img.shields.io/badge/maintained-yes-green.svg)](https://github.com/Matthieu/aws-lambda-deployment/commits/main)

## Table of Contents

- [Overview](#overview)
- [DevOps Architecture](#devops-architecture)
- [CI/CD Pipeline](#cicd-pipeline)
- [Infrastructure Requirements](#infrastructure-requirements)
- [Deployment Strategy](#deployment-strategy)
- [Security & Secrets Management](#security--secrets-management)
- [Monitoring & Observability](#monitoring--observability)
- [Automated Testing](#automated-testing)
- [Troubleshooting](#troubleshooting)
- [Best Practices](#best-practices)

## Overview

A production-ready DevOps template implementing Infrastructure as Code (IaC) principles for AWS Lambda deployments. This project showcases modern CI/CD practices, automated testing, and secure deployment strategies for serverless applications.

## DevOps Architecture

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Developer     │───▶│  GitHub Actions  │───▶│   AWS Lambda    │
│   Push/PR       │    │   CI/CD Pipeline │    │   Production    │
└─────────────────┘    └──────────────────┘    └─────────────────┘
                              │
                              ▼
                       ┌──────────────────┐
                       │  Security Scan   │
                       │  Dependency Mgmt │
                       │  Automated Tests │
                       └──────────────────┘
```

**Key DevOps Principles:**
- **Continuous Integration**: Automated builds and testing on every commit
- **Continuous Deployment**: Zero-downtime deployments to AWS Lambda
- **Infrastructure as Code**: Version-controlled deployment configurations
- **Security by Design**: Encrypted secrets and least-privilege access
- **Observability**: Built-in logging and monitoring capabilities

## Infrastructure Requirements

### AWS Infrastructure
- AWS Account with Lambda execution permissions
- IAM Role with appropriate Lambda deployment policies
- CloudWatch Logs group for function monitoring

### CI/CD Infrastructure
- GitHub repository with Actions enabled
- Encrypted repository secrets configuration
- Branch protection rules (recommended)

### Required Secrets
```bash
# AWS Credentials (use IAM roles in production)
AWS_ACCESS_KEY_ID=<your-access-key>
AWS_SECRET_ACCESS_KEY=<your-secret-key>
AWS_REGION=<deployment-region>
LAMBDA_FUNCTION_NAME=<target-function-name>
```

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

## CI/CD Pipeline

The GitHub Actions workflow implements a robust deployment pipeline:

### Pipeline Stages

1. **Source Control Integration**
   - Triggered on push to `main` branch
   - Pull request validation
   - Dependabot integration for security updates

2. **Build & Package**
   - Python environment setup
   - Dependency installation with `pip`
   - Lambda deployment package creation

3. **Security & Compliance**
   - AWS credential validation
   - Secrets management via GitHub Secrets
   - Dependency vulnerability scanning

4. **Deployment**
   - Zero-downtime Lambda function updates
   - Rollback capabilities
   - Environment-specific deployments

### Workflow Configuration
```yaml
# Deployment triggers
on:
  push:
    branches: [main]
    paths-ignore: [README.md]
  pull_request:
    branches: [main]
```

## Deployment Strategy

### Initial Setup
1. **Repository Configuration**
   ```bash
   git clone https://github.com/matthewntsiful/aws-lambda-deployment.git
   cd aws-lambda-deployment
   ```

2. **Environment Configuration**
   - Configure GitHub repository secrets
   - Set up AWS IAM permissions
   - Create target Lambda function in AWS

3. **Pipeline Activation**
   ```bash
   git add .
   git commit -m "feat: initial deployment setup"
   git push origin main
   ```

### Deployment Process
- **Automated**: Push to `main` triggers deployment
- **Manual**: Use GitHub Actions "Run workflow" button
- **Rollback**: Revert commit and push to trigger rollback

## Security & Secrets Management

### Security Best Practices
- **Encrypted Secrets**: All sensitive data stored in GitHub Secrets
- **Least Privilege**: IAM roles with minimal required permissions
- **Audit Trail**: All deployments logged and traceable
- **Dependency Scanning**: Automated vulnerability detection

### Secrets Configuration
```bash
# GitHub Repository Settings > Secrets and Variables > Actions
gh secret set AWS_ACCESS_KEY_ID --body "<your-key>"
gh secret set AWS_SECRET_ACCESS_KEY --body "<your-secret>"
gh secret set AWS_REGION --body "us-east-1"
gh secret set LAMBDA_FUNCTION_NAME --body "my-lambda-function"
```

## Monitoring & Observability

### Built-in Monitoring
- **GitHub Actions**: Pipeline execution logs and metrics
- **AWS CloudWatch**: Lambda function logs and performance metrics
- **Deployment Status**: Real-time badge status in README

### Testing & Validation
```bash
# Local testing
aws lambda invoke \
  --function-name <FUNCTION_NAME> \
  --payload '{"name": "DevOps"}' \
  response.json && cat response.json

# Expected output
{"statusCode": 200, "body": "{\"message\": \"Hello, DevOps!\"}"}
```

## Automated Testing

### Test Strategy
- **Unit Tests**: Function logic validation
- **Integration Tests**: AWS service integration
- **Deployment Tests**: Post-deployment validation

### Test Execution
```bash
# Run tests locally
python -m pytest tests/

# CI/CD automated testing
# Tests run automatically on every push/PR
```

## Troubleshooting

### Common Issues

| Issue | Cause | Solution |
|-------|-------|----------|
| Deployment fails | Invalid AWS credentials | Verify secrets configuration |
| Function not found | Incorrect function name | Check `LAMBDA_FUNCTION_NAME` secret |
| Permission denied | Insufficient IAM permissions | Update IAM role policies |
| Package too large | Dependencies exceed limit | Optimize dependencies or use layers |

### Debug Commands
```bash
# Check workflow logs
gh run list --workflow=lambda.yml

# Validate AWS credentials
aws sts get-caller-identity

# Test Lambda function
aws lambda get-function --function-name <FUNCTION_NAME>
```

## Best Practices

### DevOps Excellence
- **Version Control**: Tag releases for rollback capability
- **Environment Separation**: Use different AWS accounts/regions
- **Monitoring**: Set up CloudWatch alarms for function health
- **Documentation**: Keep deployment procedures updated

### Security Hardening
- **Rotate Credentials**: Regular AWS key rotation
- **Network Security**: VPC configuration for sensitive workloads
- **Compliance**: Regular security audits and dependency updates

### Performance Optimization
- **Cold Start Reduction**: Optimize function initialization
- **Memory Tuning**: Right-size Lambda memory allocation
- **Concurrent Execution**: Configure appropriate concurrency limits

---

## Contributing

Contributions welcome! Please read our DevOps guidelines:
- Follow conventional commit messages
- Ensure all CI/CD checks pass
- Update documentation for infrastructure changes

## License

MIT License - see [LICENSE](LICENSE) for details.

---

**Built with DevOps best practices** 🚀
