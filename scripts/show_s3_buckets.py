# Retrieve the list of existing buckets
import boto3
from settings.aws_config import aws_s3_access_key, aws_s3_secret_access_key


def show_s3_buckets():
    s3_client = boto3.client(
                    's3',
                    aws_access_key_id=aws_s3_access_key,
                    aws_secret_access_key=aws_s3_secret_access_key
                    # aws_session_token=SESSION_TOKEN     # (it is required for temporary bucket creation)
                )
    response = s3_client.list_buckets()

    # Output the bucket names
    print('Existing buckets:')
    for bucket in response['Buckets']:
        print(f'  {bucket["Name"]}')


if __name__ == "__main__":

    show_s3_buckets()

