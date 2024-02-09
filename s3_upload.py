import boto3
import pandas as pd

# Your AWS Access Key and Secret Key
aws_access_key_id = 'YOUR_ACCESS_KEY_ID'
aws_secret_access_key = 'YOUR_SECRET_ACCESS_KEY'

# Create an S3 client
s3_client = boto3.client(
    's3',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    # If you're using a specific region, you can specify it here
    region_name='YOUR_REGION_NAME'
)

# The name of your S3 bucket
bucket_name = 'your-bucket-name'

# The path to your local file
local_file_path = 'path/to/your/file.parquet'

# The path where you want to store your file in S3
s3_file_path = 'path/in/s3/bucket/file.parquet'

# Upload the file
s3_client.upload_file(local_file_path, bucket_name, s3_file_path)

print(f"File {local_file_path} uploaded to {s3_file_path} in bucket {bucket_name}.")
