import mysql.connector


def conectar():
    try:
        database = mysql.connector.connect(host='localhost',
                                           database="clientes",
                                           user='root',
                                           password='',
                                           raise_on_warnings=True)
        cursor = database.cursor(buffered=True)

        return [database, cursor]
    except:
        print("Base de datos inacesible")


