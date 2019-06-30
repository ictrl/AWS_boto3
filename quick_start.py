import boto3
s3 = boto3.resource('s3', 'us-east-1')

# Print out bucket names
for bucket in s3.buckets.all():
    print(bucket.name)

# Upload a new file
data = open('HiBaby!.png', 'rb')
s3.Bucket('firstone.saloni').put_object(Key='HiBaby!.png', Body=data)
