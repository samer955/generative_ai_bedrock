# Integration of Amazon Bedrock in a simple application using python.

## Setup AWS CLI
In order to call the AWS Bedrock API from your application, you need first to login into your `AWS CLI`.
Install the AWS CLI, open a terminal and run `aws configure`. Provide `Access Key ID` and `Secret Access Key` (you find them in your personal area in your AWS Account) as follow:

```
$ aws configure
AWS Access Key ID [None]: THISXISXANYEXAMPLEYKEY
AWS Secret Access Key [None]: yhyzybbbbthisIsAnExampleSecretKey
Default region name [None]: us-east-1
Default output format [None]: json
```

### Subscription/Activation to AWS Bedrock
In order to use the AWS Service Bedrock you need to activate the service and enable the Model_AI provided.
See https://us-east-1.console.aws.amazon.com/bedrock/home?region=us-east-1#/ and https://us-east-1.console.aws.amazon.com/bedrock/home?region=us-east-1#/overview

### Starting the App
pre: if you dont have it already, install python and boto3 (the AWS SDK for Python to create, configure, and manage AWS services).
The Command to install it is: `pip install boto3`
 
1. Clone the Repository
2. Navigate inside the folder
3. Open your terminal
4. Run `python generate_test.py`
5. Provide a question and wait for an answer in your terminal.


![plot](./generate_text_screenshot.png)
