import boto3
Bucket_name = "samrat.online"
bucket = boto3.resource('s3').Bucket(Bucket_name )

for key in bucket.objects.all():
    key.delete()
bucket.delete()


