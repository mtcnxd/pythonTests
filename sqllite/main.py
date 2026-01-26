from DataBaseLite import DataBaseLite

sqlite = DataBaseLite()

if __name__ == "__main__":
    sqlite.create_table()
    sqlite.insert_data("Marcos", 40)
    sqlite.insert_data("Tzuc", 41)
    data = sqlite.query_data()
    sqlite.close()

    for row in data:
        print(row)