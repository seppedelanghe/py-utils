import boto3, tempfile, logging
from botocore.exceptions import ClientError


'''
    Class to make the basic S3 actions easy in python
'''
class S3MediaHandler:
    def __init__(self, bucket, access_key, secret_key, base_path = None):
        self.base_path = base_path
        self.bucket = bucket
        self.s3 = boto3.client(
            's3',
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key
        )

        self.check()

    def check(self):
        buckets = self.list_buckets()
        exists = False
        for b in buckets['Buckets']:
            if b['Name'] == self.bucket:
                exists = True

        if not exists:
            self.create_bucket()

    def list_buckets(self):
        response = self.s3.list_buckets()
        return response

    def create_bucket(self):
        try:
            self.s3.create_bucket(Bucket=self.bucket)
        except ClientError as e:
            logging.error(e)
            return False
        return True

    def upload_local_file(self, path: str, object_name: str):
        try:
            response = self.s3.upload_file(path, self.bucket, object_name)
            return True
        except ClientError as e:
            logging.error(e)
            return False

    def upload_fileobj(self, file, newname: str):
        try:
            response = self.s3.upload_fileobj(file, self.bucket, newname)
            return True

        except ClientError as e:
            logging.error(e)
            return False

    def get_file(self, location):
        file = tempfile.TemporaryFile('wb')
        self.s3.download_fileobj(self.bucket, location, file)

        return file

    def download_file(self, location, to: str):
        with open(to, 'wb') as dest:
            self.s3.download_fileobj(self.bucket, location, dest)

    def create_presigned_url(self, location: str, expiration: int = 3600):
        try:
            params = {
                'Bucket': self.bucket,
                'Key': location
            }
            response = self.s3.generate_presigned_url('get_object', Params=params, ExpiresIn=expiration)
            print(response)

        except ClientError as e:
            logging.error(e)
            return None

        return response
