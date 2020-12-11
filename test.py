from conexion import conectar
import datetime
import time

connect = conectar()
db = connect[0]
cursor = connect[1]

class show():
    def __init__(self, username):
        self.username = username



    ##return Id_Cliente

    def show_id(self):
        connect = conectar()
        db = connect[0]
        cursor = connect[1]
        query = f"SELECT id_Cliente FROM usuarios WHERE usuario = '{self.username}'"
        # val = (self.username)

        cursor.execute(query)

        val = cursor.fetchone()
        if val:
            return val[0]



    def show_balance(self):
        connect = conectar()
        db = connect[0]
        cursor = connect[1]

        query = f"SELECT saldo FROM usuarios WHERE usuario = '{self.username}'"

        cursor.execute(query)
        val = cursor.fetchone()

        if val:
            return val[0]

