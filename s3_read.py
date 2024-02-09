import boto3
import pandas as pd
import io

# Your AWS Access Key and Secret Key
aws_access_key_id = 'YOUR_ACCESS_KEY_ID'
aws_secret_access_key = 'YOUR_SECRET_ACCESS_KEY'

# Create an S3 resource
s3 = boto3.resource(
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

bucket = s3.Bucket(bucket_name)
object = bucket.Object(s3_file_key)
response = object.get()
file_content = response['Body'].read()

# Read the Parquet file into a pandas DataFrame
df = pd.read_parquet(io.BytesIO(file_content))

# Now you can work with the DataFrame
print(df.head(10))
