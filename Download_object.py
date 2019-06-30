import boto3

bucket_name='firstone.saloni'
OBJECT_NAME="connection.php"
Saveas = OBJECT_NAME
s3 = boto3.client('s3')
s3.download_file(bucket_name, OBJECT_NAME, Saveas )