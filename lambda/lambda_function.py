import json

def lambda_handler(event, context):
    print("S3 Event Received")

    for record in event["Records"]:
        bucket = record["s3"]["bucket"]["name"]
        key = record["s3"]["object"]["key"]

        print(f"Bucket: {bucket}")
        print(f"File: {key}")

    return {
        "statusCode": 200,
        "body": json.dumps("Success")
    }
