import json
import boto3
s3_client=boto3.client("s3")

def write_data_to_s3():
    s3_client.put_object(
        Body = "data",
        Bucket = "bucket_name",
        key= "object_to_be_created"
    )





def lambda_handler(event, context):
    # TODO implement
    print(event)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
