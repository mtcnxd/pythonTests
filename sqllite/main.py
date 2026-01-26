from DataBaseLite import DataBaseLite
import random
import time

sqlite = DataBaseLite()

if __name__ == "__main__":
    sqlite.create_table()
    names = ["Marcos", "Tzuc", "Ana", "Luis", "Carla", "Jose", "Marta", "Pedro", "Lucia", "Sofia"]

    for name in names:
        sqlite.insert_data(name, random.randint(10, 99))
        time.sleep(0.1)

    data = sqlite.query_data()
    sqlite.close()

    for row in data:
        print(row)