import boto3
import json

# Initialize a boto3 client
lambda_client = boto3.client('lambda')

# Define the Lambda function name
function_name = 'YourLambdaFunctionName'

# Define the payload you want to send to your Lambda function
payload = {
    # Your payload here
    'key': 'value'
}

# Convert payload to JSON
json_payload = json.dumps(payload)

# Invoke the Lambda function
response = lambda_client.invoke(
    FunctionName=function_name,
    InvocationType='RequestResponse',  # Use 'Event' for asynchronous execution
    Payload=json_payload,
)

# Read the Lambda function response
response_payload = response['Payload'].read()

# Optionally, convert the response payload to a Python dictionary
response_data = json.loads(response_payload)

print(response_data)
