import logging
import boto3
from botocore.exceptions import ClientError
from settings.aws_config import aws_s3_access_key, aws_s3_secret_access_key


def create_bucket(bucket_name, region=None):
    """Create an S3 bucket in a specified region

    If a region is not specified, the bucket is created in the S3 default
    region (us-east-1).

    :param bucket_name: Bucket to create
    :param region: String region to create bucket in, e.g., 'us-west-2'
    :return: True if bucket created, else False
    """

    # Create bucket
    try:
        if region is None:
            # s3_client = boto3.client('s3')
            s3_client = boto3.client(
                's3',
                aws_access_key_id=aws_s3_access_key,
                aws_secret_access_key=aws_s3_secret_access_key
                # aws_session_token=SESSION_TOKEN     # (it is required for temporary bucket creation)
            )
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client = boto3.client(
                's3',
                aws_access_key_id=aws_s3_access_key,
                aws_secret_access_key=aws_s3_secret_access_key,
                region_name=region
            )
            # location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name)
            # s3_client.create_bucket(Bucket=bucket_name,
            #                         CreateBucketConfiguration={'LocationConstraint': region})
    except ClientError as e:
        logging.error(e)
        return False
    return True


if __name__ == "__main__":

    # bucket_name = "data-analysis-with-nba"
    bucket_name = "data-analysis-with-nba-target"
    region = "us-east-1"

    response = create_bucket(bucket_name=bucket_name, region=region)
    print(response)


