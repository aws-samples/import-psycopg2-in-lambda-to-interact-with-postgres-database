#!/bin/bash

#### Script that builds the lambda zip file

# Delete the lambda_deploy folder if exists
rm -rf lambda_deploy

# Create new lambda_deploy folder
mkdir lambda_deploy

# Install psycopg2 libraries in the lambda_deploy folder
pip install -r requirements.txt -t lambda_deploy

# Copy the lambda script into the lambda_deploy folder
cp lambda_code.py lambda_deploy

# Generate the zip file from the lambda_deploy folder
cd lambda_deploy
zip -r9 ../lambda_deploy.zip .
cd ..
rm -rf lambda_deploy