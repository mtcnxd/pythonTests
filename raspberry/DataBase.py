import pymysql.cursors

class DataBase:
    def __init__(self):
        self.connection = pymysql.connect(
            host="127.0.0.1",
            user="marcos",
            password="",
            db="",
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor
        )

    def __del__(self):
        self.connection.close()

    def select(self, sql, params=None):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(sql, params)
                result = cursor.fetchall()
            return result

        except Exception as e:
            print(f"Error al ejecutar la consulta: {e}")
            return None

    def query(self, query, values):
        try:
            with self.connection.cursor():
                cursor.execute(query, values)
                self.commit()
        except Exception as e:
            print(f"An error ocurred: {e}")


'''
cursor = self.connection.cursor()
cursor.execute(query, values)
self.connection.commit()
'''