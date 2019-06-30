# Upload a new file Method 2, method 1 is in quick start
import boto3

# Create an S3 client
s3 = boto3.client('s3')

filename = 'pic.gif'
bucket_name = 'firstone.saloni'

# Uploads the given file using a managed uploader, which will split up large
# files automatically and upload parts in parallel.
s3.upload_file(filename, bucket_name, filename)