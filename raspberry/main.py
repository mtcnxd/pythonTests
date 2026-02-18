from DataBase import *
import time
from datetime import datetime

if __name__ == "__main__" :
    database = DataBase()

    while True:
        now = datetime.now()
        database.query("INSERT INTO sensors (name, location, update_at, created_at) VALUES (%s,%s,%s,%s)", ('marcos', 'tzuc', now, now))

        result = database.select("SELECT * FROM sensors")

        print(result)

        time.sleep(1)