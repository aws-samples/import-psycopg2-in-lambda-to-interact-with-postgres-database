#!/usr/bin/env python3

import aws_cdk as cdk
from Constructs.aws_lambda_stack import LambdaStack

# Variables
aws_acccount = "AWS_ACCOUNT_ID"
region = "AWS_REGION"

app = cdk.App()

LambdaStack(
    app,
    "AWSLambdaPyscopg2",
    env=cdk.Environment(account=aws_acccount, region=region),
    tags={"Project": "AWS Lambda function with pyscopg2 library"},
)

app.synth()
