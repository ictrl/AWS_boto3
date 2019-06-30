import boto3
s3 = boto3.resource("s3")
obj = s3.Object("firstone.saloni", "HiBaby!.png")
obj.delete()