import boto3
import time
import random
from boto3.dynamodb.conditions import Key, Attr


data = 0

dynamodb = boto3.resource(
    'dynamodb', 
    region_name='us-east-1',

)

table = dynamodb.Table('SensorLocations')

print ("-----------------------------------------------------")
print ("Insert data: {}".format(data))
print ("-----------------------------------------------------")

try:
    response = table.put_item(
        Item={
            'id': random.randint(0,9),
            'date': str(data),
            'name': 'Marcos',
            'lastname': 'Tzuc'
        }
    )
    print("Datos insertados exitosamente:", response)
except Exception as e:
    print("Error al insertar datos:", e)

time.sleep(1)
data = data + 1

response = table.query(
    KeyConditionExpression = Key('id').eq(7) & Key('date').eq('5') # , FilterExpression = Attr('date').eq('Marcos')
)


print ("----------------------")