import boto3
import json
import cx_Oracle
import pandas as pd

# Function to get database credentials from AWS Secrets Manager
def get_db_credentials(secret_name, region_name):
    session = boto3.session.Session()
    client = session.client(service_name='secretsmanager', region_name=region_name)
    response = client.get_secret_value(SecretId=secret_name)
    secret = json.loads(response['SecretString'])
    return secret

# Retrieve your database credentials
secret_name = 'your_secret_name_here'
region_name = 'your_region_name_here'
db_credentials = get_db_credentials(secret_name, region_name)

# Prepare DSN (Data Source Name) for Oracle connection
dsn = cx_Oracle.makedsn(db_credentials['host'], db_credentials['port'], service_name=db_credentials['dbname'])

# Connect to the Oracle database
connection = cx_Oracle.connect(user=db_credentials['username'],
                               password=db_credentials['password'],
                               dsn=dsn)
cursor = connection.cursor()

# Read your SQL file and execute the query
sql_file_path = 'your_sql_file.sql'
with open(sql_file_path, 'r') as file:
    sql_query = file.read().strip()

# Execute the SQL query
cursor.execute(sql_query)

# If it's a SELECT statement, convert the result to a Pandas DataFrame
if sql_query.lower().startswith("select"):
    result = cursor.fetchall()
    columns = [col[0] for col in cursor.description]
    df = pd.DataFrame(result, columns=columns)
    print(df)  # Display the DataFrame
else:
    connection.commit()  # For INSERT/UPDATE/DELETE, commit the changes

# Clean up
cursor.close()
connection.close()
