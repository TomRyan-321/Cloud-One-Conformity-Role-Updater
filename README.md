# Cloud-One-Conformity-Role-Updater

## About

Simple Python based Lambda function to keep your Cloud Conformity roles up to date whenever there is a new version available. 

The template deploys a lambda function running on the Python 3.7 runtime with a scheduled event triggering the function once daily to check if the template deployed matches the latest available from the official template url. If a new version is available the function will automatically update the existing CloudConformity stack to the latest version.

## Installation

Deploy the cloudformation template in the same region you have deployed the CloudConformtiy role template (default and recommended region: us-east-1).
