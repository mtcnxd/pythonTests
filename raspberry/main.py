from datetime import datetime
from models.Sensor import Sensor
from apis.Bitso import Bitso
from apis.Telegram import Telegram
import time
import random


database = DataBase()
sensor = Sensor()
bitso = Bitso()

if __name__ == "__main__" :
    book_info = bitso.get_book_info("btc_mxn")

    now = datetime.now()

    data = {
        'name': str(random.randint(1, 100)),
        'location': book_info['last'],
        'updated_at': now,
        'created_at': now
    }

    sensor.create(data)
    
    result = sensor.find(20)

    Telegram().send_message(f"El precio actual de btc_mxn es: {book_info['last']}")

    print(result)