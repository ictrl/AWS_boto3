
import boto3
Bucket_name = "Samrat.online"


s3 = boto3.client('s3')
s3.create_bucket(Bucket=Bucket_name)
