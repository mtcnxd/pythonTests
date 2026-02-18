from DataBase import *
from models.Sensor import *
from datetime import datetime
import time
import random

if __name__ == "__main__" :
    database = DataBase()
    sensor = Sensor()

    while True:
        now = datetime.now()

        data = {
            'name': str(random.randint(1, 100)),
            'location': 'vergel',
            'update_at': now,
            'created_at': now
        }

        keys = data.keys()
        print(tuple(keys))

        sensor.create(data)
        
        result = sensor.find(69)

        print(data)

        time.sleep(5)