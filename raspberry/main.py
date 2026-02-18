from models.Sensor import *
from datetime import datetime
from services.BitsoService import *
import time
import random

if __name__ == "__main__" :
    database = DataBase()
    sensor = Sensor()
    bitso = Bitso()

    while True:
        book_info = bitso.get_book_info("btc_mxn")

        now = datetime.now()

        data = {
            'name': str(random.randint(1, 100)),
            'location': book_info['last'],
            'update_at': now,
            'created_at': now
        }

        sensor.create(data)
        
        result = sensor.find(20)

        print(result)

        time.sleep(30)