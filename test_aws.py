import os
import tempfile
import unittest

import boto3, botocore
from moto import mock_s3

from aws import s3_upload

class TestAWS(unittest.TestCase):
    @mock_s3
    def test_s3_upload(self):
        tmp_file = tempfile.mkstemp('.json')
        bucket_name = 'my-bucket'

        s3 = boto3.client('s3')
        s3.create_bucket(Bucket=bucket_name)

        # Should raise exception because no environment variables defined yet.
        with self.assertRaises(Exception) as context:
            s3_upload(bucket_name, tmp_file[1])

        # Set environment variables
        os.environ['AWS_REGION'] = 'us-east-1'
        os.environ['AWS_ACCESS_KEY_ID'] = 'access'
        os.environ['AWS_SECRET_ACCESS_KEY'] = 'secret'
        os.environ['AWS_S3_BUCKET_NAME'] = 'my-bucket'

        # Should be successful
        s3_upload(tmp_file[1])

        s3 = boto3.resource('s3')

        # Verify if file is successfully uploaded.
        try:
            s3.Object(os.environ['AWS_S3_BUCKET_NAME'],
                      os.path.basename(tmp_file[1])).load()
        except botocore.exceptions.ClientError as e:
            self.fail('Object not found')
        else:
            self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
