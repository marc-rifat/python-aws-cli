import boto3
import pandas as pd
import io

# AWS credentials and S3 details
aws_access_key_id = 'YOUR_ACCESS_KEY_ID'
aws_secret_access_key = 'YOUR_SECRET_ACCESS_KEY'
region_name = 'YOUR_REGION_NAME'
bucket_name = 'your-bucket-name'
s3_file_key = 'path/in/s3/bucket/your-file.parquet'

# Setting up S3 access
s3_client = boto3.client(
    's3',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=region_name
)

# Reading the Parquet file directly into a DataFrame
s3_uri = f"s3://{bucket_name}/{s3_file_key}"
df = pd.read_parquet(s3_uri, storage_options={
    "key": aws_access_key_id,
    "secret": aws_secret_access_key
})

# Modify the DataFrame here
# Example: Add a new column with default values
df['new_column'] = 'default value'

# Write the updated DataFrame back to the same S3 location
df.to_parquet(s3_uri, index=False, storage_options={
    "key": aws_access_key_id,
    "secret": aws_secret_access_key
})

print(f"File {s3_file_key} in bucket {bucket_name} has been updated.")
