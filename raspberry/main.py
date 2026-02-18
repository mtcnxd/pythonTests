from DataBase import *
import time

if __name__ == "__main__" :
    database = DataBase()

    while True:
        print("Hola mundo")
        database.query("INSERT INTO table () VALUES ()")
        time.sleep(1)
