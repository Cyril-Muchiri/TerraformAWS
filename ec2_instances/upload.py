import s3fs

def upload_to_s3(local_file_path, s3_bucket, s3_key):
    fs = s3fs.S3FileSystem()

    with open(local_file_path, 'rb') as local_file:
        with fs.open(f'{s3_bucket}/{s3_key}', 'wb') as s3_file:
            s3_file.write(local_file.read())

    print(f'File uploaded to s3://{s3_bucket}/{s3_key}')

local_file_path = './mkuuKeey.pem'
s3_bucket = 'mkuu'
s3_key = '/s3/keys/mkuuKeey.pem'

upload_to_s3(local_file_path, s3_bucket, s3_key)
