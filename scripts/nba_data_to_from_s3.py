# Import libraries
import boto3
import pandas as pd
from io import StringIO, BytesIO      # StringIO buffer for csv, BytesIO buffer for parquet
from datetime import datetime, timedelta
from settings.aws_config import aws_s3_access_key, aws_s3_secret_access_key


# Access nba data from aws s3 bucket to pandas dataframe
bucket = "data-analysis-with-nba"
s3_client = boto3.resource(
                    's3',
                    aws_access_key_id=aws_s3_access_key,
                    aws_secret_access_key=aws_s3_secret_access_key
                )
bucket = s3_client.Bucket(bucket)

# get s3 objects and combined them
bucket_obj1 = bucket.objects.filter(Prefix="nba1")
bucket_obj2 = bucket.objects.filter(Prefix="nba2")
objects = [obj for obj in bucket_obj1] + [obj for obj in bucket_obj2]

# Get the columns for pandas dataframe
csv_obj = bucket.Object(key=objects[0].key).get().get('Body').read().decode('utf-8')
data = StringIO(csv_obj)
df = pd.read_csv(data, delimiter=',')
# df.columns

# create a dataframe
# nba_df = pd.DataFrame(columns=df.columns)
# for obj in objects:
#     csv_obj = bucket.Object(key=obj.key).get().get('Body').read().decode('utf-8')
#     data = StringIO(csv_obj)
#     df = pd.read_csv(data, delimiter=',')
#     nba_df = nba_df.append(df, ignore_index=True)

# print(nba_df.head())


# csv to df using function
def csv_to_df(filename):
    csv_obj = bucket.Object(key=filename).get().get('Body').read().decode('utf-8')
    data = StringIO(csv_obj)
    df = pd.read_csv(data, delimiter=',')
    return df


df_all = pd.concat([csv_to_df(obj.key) for obj in objects], ignore_index=True)
print(df_all.head())


# Data processing and cleaning as per requiremnets
# create a new dataframe with selected columns
# new_columns = ['Name', 'Team', 'Age', 'Height', 'Weight']
# nba_df1 = nba_df.loc[:, new_columns]

# print(nba_df1.head())


# Write processed data to aws S3 target bucket in parquet format
# key = 'nba_report_' + datetime.today().strftime("%Y%m%d_%H%M%S") + '.parquet'


# out_buffer = BytesIO()
# nba_df1.to_parquet(out_buffer, index=False)
# bucket_target = s3_client.Bucket('data-analysis-with-nba-target')
# bucket_target.put_object(Body=out_buffer.getvalue(), Key=key)
#
# # Reading the uploaded file
# for obj in bucket_target.objects.all():
#     print(obj.key)


# prq_obj = bucket_target.Object(key='nba_report_20220720_192435.parquet').get().get('Body').read()
# data = BytesIO(prq_obj)
# df_report = pd.read_parquet(data)
# print(df_report)
