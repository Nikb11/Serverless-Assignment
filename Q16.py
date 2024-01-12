#Log Cleaner for S3

import boto3
from datetime import datetime, timedelta

def lambda_handler(event, context):
    bucket_name = 'nikhil-buckets3'
    s3 = boto3.client('s3', region_name='us-east-1')

    current_date = datetime.now() 


    objects = s3.list_objects(Bucket=bucket_name)['Contents']

   
    for obj in objects:
        last_modified = obj['LastModified'].replace(tzinfo=None)
        age = current_date - last_modified

        if age > timedelta(days=90):
            s3.delete_object(Bucket=bucket_name, Key=obj['Key'])

    return 'Log cleaning completed!'
