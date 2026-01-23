import pymysql.cursors

class DataBase:
    def __init__(self):
        self.connection = pymysql.connect(
            host="localhost",
            user="root",
            password="",
            db="mecanica_rubio",
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