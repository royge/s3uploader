import os
import boto3


def s3_upload(filepath):
    region = None
    access_key = None
    secret_key = None
    bucket_name = None

    try:
        region = os.environ['AWS_REGION']
        access_key = os.environ['AWS_ACCESS_KEY_ID']
        secret_key = os.environ['AWS_SECRET_ACCESS_KEY']
        bucket_name = os.environ['AWS_S3_BUCKET_NAME']
    except Exception as ex:
        raise ex

    s3 = boto3.client(
        's3',
        region_name=region,
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key
    )

    # Uploads the given file using a managed uploader, which will split up large
    # files automatically and upload parts in parallel.
    s3.upload_file(
        filepath,
        bucket_name,
        os.path.basename(filepath)
    )
