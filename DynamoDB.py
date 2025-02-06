import boto3
import time
import random
import math
import datetime
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource(
    'dynamodb', 
    region_name='us-east-1',
    aws_access_key_id='AKIAS7FQORI46RDHT5EF',
    aws_secret_access_key='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'
)

def scan_table(table):
    response = table.scan()
    data = response.get('Items', [])

    while 'LastEvaluatedKey' in response:
        response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
        data.extend(response.get('Items', []))

    return data

table = dynamodb.Table('SensorValues')

try:
    for i in range(1, 10):
        print ("-----------------------------------------------------")
        print (f"Insert data: {i}")

        response = table.put_item(Item = {
            "sensor": 'temperature',
            "value": i,
            "created_at": str(datetime.datetime.now())
        })

        print("Insert success:", response)
        time.sleep(0.5)

except Exception as e:
    print(f"Write Error: {e}")

time.sleep(1)

try:
    items = scan_table(table)
    #response = table.query(
    #    KeyConditionExpression = Key('sensor').eq(10)
    #    # KeyConditionExpression = Key('sensor').eq(7) & Key('sensor').eq('5') # , FilterExpression = Attr('date').eq('Marcos')
    #)
    
except Exception as e:
    print(f"Read Error: {e}")


for item in items:
    print ("-----------------------------------------------------")
    print (f"Sensor: {item['sensor']} Value: {str(item['value'])}")