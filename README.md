# AWS Lambda Deployment

[![CI/CD](https://github.com/Matthieu/Jomacs_DevOps/actions/workflows/lamda.yml/badge.svg)](https://github.com/Matthieu/Jomacs_DevOps/actions/workflows/lamda.yml)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## Overview

This project demonstrates an automated deployment pipeline for an AWS Lambda function using GitHub Actions.

- **Language:** Python
- **CI/CD:** GitHub Actions
- **Cloud:** AWS Lambda

## Lambda Function

The Lambda function (`package/lamda_function.py`) processes incoming events and returns a simple greeting message.

## Workflow

The GitHub Actions workflow (`.github/workflows/lamda.yml`) automates:
- Dependency installation
- Packaging the Lambda function
- Deploying to AWS Lambda

## Usage

1. Update your AWS credentials and Lambda function name in the repository secrets.
2. Push changes to the `main` branch to trigger deployment.

## Project Structure

```
aws-lambda-deployment/
├── LICENSE
├── README.md
├── package/
│   └── lamda_function.py
└── .github/
    └── workflows/
        └── lamda.yml
```

---

