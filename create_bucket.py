import boto3
from botocore.exceptions import ClientError,ParamValidationError


def create_buckets(bucket_name):
    client = boto3.client("s3", region_name='ca-central-1')
    location = {'LocationConstraint': 'ca-central-1'}
    try:
        response = client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=location)
       
    except ParamValidationError as error:
        response={
            'Error':{
                'Message':str(error)
                },
            'ResponseMetadata':{
                'HTTPStatusCode':400
             }
        }
    
    except ClientError as error:
        response={
            'Error':{
                'Message':str(error)
                },
            'ResponseMetadata':{
                'HTTPStatusCode':400
             }
        }
        

    return response




def number_of_buckets(bucket_name,num):
    region_name='us-east-2'
    client = boto3.client("s3")
    # location = {'LocationConstraint': 'ca-central-1'}
    

    for i in range(0,num):
        try: 
            if(region_name!='us-east-1'):
                bucket_name=f'{bucket_name}{i}'
            # location = {'LocationConstraint': region[i]}  
            # response = client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={'LocationConstraint': region_name})
                response = client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={'LocationConstraint': region_name})
            else:
                bucket_name=f'{bucket_name}{i}'
                response = client.create_bucket(Bucket=bucket_name)

       
        except ParamValidationError as error:
            response={
            'Error':{
                'Message':str(error)
                },
            'ResponseMetadata':{
                'HTTPStatusCode':400
             }
        }
    
        except ClientError as error:
            response={
            'Error':{
                'Message':str(error)
                },
            'ResponseMetadata':{
                'HTTPStatusCode':400
             }
        }
        

    return response





def create_region_buckets(bucket_name,region_arr):
    
    # region_name='us-east-2'
    client = boto3.client("s3")
    # location = {'LocationConstraint': 'ca-central-1'}
    

    for i in range(0,2):
        try: 
            if(region_arr[f'{i}']!='us-east-1'):
                bucket_name=f'{bucket_name}{i}'
                print(region_arr[f'{i}'])
            # location = {'LocationConstraint': region[i]}  
            # response = client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={'LocationConstraint': region_name})
                response = client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={'LocationConstraint': region_arr[f'{i}']})
            else:
                bucket_name=f'{bucket_name}{i}'
                response = client.create_bucket(Bucket=bucket_name)

       
        except ParamValidationError as error:
            response={
            'Error':{
                'Message':str(error)
                },
            'ResponseMetadata':{
                'HTTPStatusCode':400
             }
        }
    
        except ClientError as error:
            response={
            'Error':{
                'Message':str(error)
                },
            'ResponseMetadata':{
                'HTTPStatusCode':400
             }
        }
        

    return response