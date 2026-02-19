from datetime import datetime
from models.Sensor import Sensor
from apis.Bitso import Bitso
from apis.Telegram import Telegram
import random
from Helpers import *

def create_data(book_info):
    now = datetime.now()
    data = {
        'name': str(random.randint(1, 100)),
        'location': book_info['last'],
        'updated_at': now,
        'created_at': now
    }
    sensor.create(data)

sensor = Sensor()
bitso = Bitso()

if __name__ == "__main__" :
    book_info = bitso.get_book_info("btc_usdt")
    last_price = sensor.last()

    percentage = calculate_percentage(book_info['last'], last_price['location'])

    print(f"Last price: {to_currency(last_price['location'])}")
    print(f"Current price: {to_currency(book_info['last'])}")
    print(f"Percentage: {to_percentage(percentage)}")

    if percentage > 1:
        Telegram().send_message(f"Current Bitcoin price: {to_currency(book_info['last'])} the change is: {to_percentage(percentage)}")