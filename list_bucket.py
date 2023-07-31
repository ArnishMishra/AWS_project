import boto3
from botocore.exceptions import ClientError

def list_bucket_name(aws_region):
    bucket_list=[]
    try:
        s3 = boto3.client("s3", region_name=aws_region)
        response=s3.list_buckets()
        for bucket in response['Buckets']:
            if s3.head_bucket(Bucket=bucket['Name'])['ResponseMetadata']['HTTPHeaders']['x-amz-bucket-region']== aws_region:
            # if s3.get_bucket_location(Bucket=bucket['Name'])['LocationConstraint']== aws_region:
                bucket_list.append(bucket['Name'])
            # bucket_list.append(bucket['Name'])

        return  bucket_list

    except ClientError as error:
        return error.response
        