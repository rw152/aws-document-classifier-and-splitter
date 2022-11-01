
import boto3
from urllib.parse import urlparse
folder_uri = 's3://logix-docsplitter-training/Training Docs/'
bucket_name = 'logix-docsplitter-training'


s3_resource = boto3.resource('s3')
dynamodb = boto3.client("dynamodb")
folder_name = folder_uri.split(bucket_name + "/", 1)[1]
bucket = s3_resource.Bucket(bucket_name)
s3_client = boto3.client("s3")

count = 0
count_obj = sum(1 for _ in bucket.objects.all())

print(f'neato count {count_obj}')

for obj in bucket.objects.filter(Prefix=folder_name):
    key = obj.key
    # Skip files that are not PDFs, JPEGs, or PNGs
    object_content_type = s3_client.get_object(
        Bucket=bucket_name,
        Key=key
    )['ContentType']
    valid_content_types = {'application/pdf', 'image/jpeg', 'image/png'}

    if object_content_type in valid_content_types:
        count = count + 1

print(f'all done count {count}')
