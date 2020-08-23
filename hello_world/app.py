import json
import boto3
import os
from datetime import datetime

def lambda_handler(event, context):
    try:
        event_body = json.loads(event["body"])
        dynamodb = boto3.resource("dynamodb")

        table = dynamodb.Table("Demo")
        table.put_item(
            Item={
                "Key": event_body["test"],
                "CreateDate": datetime.utcnow().isoformat()
            }
        )

        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "hello world",
            }),
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({
                "message": e.args
            }),
    }