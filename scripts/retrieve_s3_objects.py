# Retrieve the list of existing buckets
import boto3
import pandas as pd
from settings.aws_config import aws_s3_access_key, aws_s3_secret_access_key


def retrieve_s3_objects(bucket, filter):
    s3_client = boto3.resource(
                    's3',
                    aws_access_key_id=aws_s3_access_key,
                    aws_secret_access_key=aws_s3_secret_access_key
                )
    bucket = s3_client.Bucket(bucket)

    # Output the object names
    bucket_obj = bucket.objects.filter(Prefix=filter)
    print('Existing S3 objects:')
    for obj in bucket_obj:
        print(obj)


if __name__ == "__main__":

    bucket = "data-analysis-with-nba"
    filter = "nba"
    retrieve_s3_objects(bucket, filter)
