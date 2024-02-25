import pandas as pd
import pyarrow.dataset as ds

option 1
# Specify your S3 bucket and folder path
bucket_name = 'your-bucket-name'
folder_path = 'path/to/your/folder'
s3_path = f's3://{bucket_name}/{folder_path}'

# Use pyarrow's dataset function to read multiple Parquet files as a single dataset
dataset = ds.dataset(s3_path, format='parquet')

# Convert the dataset to a Pandas DataFrame
final_dataframe = dataset.to_table().to_pandas()

option 2
# # Specify your S3 bucket and folder path
# bucket_name = 'your-bucket-name'
# folder_path = 'path/to/your/folder'

# # Use a wildcard to specify that you want to read all Parquet files in the folder
# s3_path = f's3://{bucket_name}/{folder_path}/*.parquet'

# # Read all Parquet files into a single DataFrame
# final_dataframe = pd.read_parquet(s3_path)
