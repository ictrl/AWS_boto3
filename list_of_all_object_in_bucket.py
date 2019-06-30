#list_of_all_object_in_bucket

from boto3 import client

bucket_name='firstone.saloni'

conn = client('s3')  # again assumes boto.cfg setup, assume AWS S3
for key in conn.list_objects(Bucket=bucket_name)['Contents']:
    print(key['Key'])