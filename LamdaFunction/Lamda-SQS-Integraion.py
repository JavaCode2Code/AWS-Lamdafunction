import json

def lambda_handler(event, context):
    # TODO implement
    print('event',event)
    return {
        'statusCode': 200,
        'body': json.dumps('Invoke Lambda With SQS!')
    }