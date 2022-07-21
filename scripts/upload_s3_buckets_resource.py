import boto3
import os
import logging
from botocore.exceptions import ClientError
from settings.aws_config import aws_s3_access_key, aws_s3_secret_access_key


def upload_file(file_dir, bucket, object_name=None):
    """
    Upload a file to an S3 bucket

    :param file_dir: File directory to upload
    :param bucket: Bucket to upload to
    :return: True if file was uploaded, else False

    """
    if object_name is None:
        object_name = os.path.basename(file_dir)

    # Upload the file
    s3_client = boto3.resource('s3',
                             aws_access_key_id=aws_s3_access_key,
                             aws_secret_access_key=aws_s3_secret_access_key)
    try:
        for file in os.listdir(file_dir):
            # print(file)
            if '.csv' in file:
                upload_file_key = object_name + '/' + str(file)
                s3_client.Bucket(bucket).upload_file(file_dir + '/' + file, upload_file_key)
    except ClientError as e:
        logging.error(e)
        return False
    return True


if __name__ == '__main__':
    file_dir = "/Users/santanusarma/Dropbox/Jagriti/Programming/data_engineering_prep/data_engineering_interview_prep/data/testdatas3/2022-01-03"
    bucket = "udemy-xetra-pds-2"

    upload_file(file_dir=file_dir, bucket=bucket)
