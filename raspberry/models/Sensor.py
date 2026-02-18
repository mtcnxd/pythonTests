from DataBase import *

class Sensor:
    def __init__(self):
        self.table = "sensors"
        
        self.database = DataBase()
    
    def find(self, id):
        query = f"SELECT * FROM {self.table} WHERE id = {id}"
        return self.database.select(query)

    def first(self, key):
        query = f"SELECT * FROM {self.table} WHERE {key} LIMIT 1"
        return self.database.select(query)

    def create(self, data):
        columns = ",".join(data.keys())
        placeholders = ",".join(["%s"] * len(data))
        values = tuple(data.values())

        query = f"INSERT INTO {self.table} ({columns}) VALUES ({placeholders})"

        return self.database.query(query, values)