import s3fs
from dotenv import load_dotenv
import os

load_dotenv()

def upload_to_s3(local_file_path, s3_bucket, s3_key, aws_endpoint, aws_access_key_id, aws_secret_access_key):
    fs = s3fs.S3FileSystem(
        key=aws_access_key_id,
        secret=aws_secret_access_key,
        client_kwargs={'endpoint_url': aws_endpoint}
    )

    with open(local_file_path, 'rb') as local_file:
        with fs.open(f'{s3_bucket}/{s3_key}', 'wb') as s3_file:
            s3_file.write(local_file.read())

    print(f'File uploaded to s3 mkuu using endpoint and creds://{s3_bucket}/{s3_key}')

local_file_path = './mkuuKeey.pem'
s3_bucket = 'mkuu'
s3_key = 's3/keys/mkuuKeeyEnd.pem'
aws_endpoint = os.getenv('AWS_ENDPOINT')
aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')

upload_to_s3(local_file_path, s3_bucket, s3_key, aws_endpoint, aws_access_key_id, aws_secret_access_key)
