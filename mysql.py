import mysql

try:
    connection = mysql.connect ('localhost', 'marcos', 'Tucm+1985', 'mecanica_rubio')
    with connection:
        cursor = connection.cursor()
        cursor.execute("select * from autos;")

except:
    print ("Error")
