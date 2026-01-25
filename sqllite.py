import sqlite3

# Connect to the database file (my_database.db)
# Using 'with' automatically handles closing the connection
try:
    with sqlite3.connect('my_database.db') as connection:
        cursor = connection.cursor()

        # Create a table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                age INTEGER
            )
        ''')

        # Insert data into the table
        cursor.execute("INSERT INTO users (name, age) VALUES ('Alice', 30)")
        cursor.execute("INSERT INTO users (name, age) VALUES ('Bob', 25)")

        # Commit the changes (using the 'with' statement handles this automatically)
        # connection.commit()

        # Query data from the table
        cursor.execute("SELECT name, age FROM users")
        rows = cursor.fetchall()

        print("Users in the database:")
        for row in rows:
            print(f"Name: {row[0]}, Age: {row[1]}")

except sqlite3.Error as e:
    print(f"A database error occurred: {e}")

# The connection is automatically closed when the 'with' block is exited
