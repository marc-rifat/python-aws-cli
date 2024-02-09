import boto3

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

# The S3 key for your file
s3_file_key = 'path/in/s3/bucket/file.parquet'

# Delete the file
s3_client.delete_object(Bucket=bucket_name, Key=s3_file_key)

print(f"File {s3_file_key} deleted from bucket {bucket_name}.")
