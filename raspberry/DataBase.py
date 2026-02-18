import pymysql.cursors

class DataBase:
    def __init__(self):
        try: 
            self.connection = pymysql.connect(
                host="127.0.0.1",
                user="root",
                password="password",
                db="BitsoData",
                charset="utf8mb4",
            )
            self.cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        except e:
            print("AN ERROR OCURRED WHILE CONNECTING: {e}")

    def __del__(self):
        self.connection.close()

    def select(self, query):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query)
                return cursor.fetchall()

        except Exception as e:
            self.connection.rollback()
            print(f"AN ERROR OCURRED WHILE EXECUTE QUERY: {e}")
            return None

    def query(self, query, values):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, values)
                self.connection.commit()
        
        except Exception as e:
            print(f"AN ERROR OCURRED WHILE INSERT DATA: {e}")