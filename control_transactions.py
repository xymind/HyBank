import conexion
import users.login as login
import users.register as register
import datetime
import time
from time import sleep
import users.test

connect = conexion.conectar()
database = connect[0]
cursor = connect[1]


class Control():

    def __init__(self,username, name_t, cantidad_T, destino, quanty ):

        self.username = username
        self.name_T = name_t
        self.cantidad_T = cantidad_T
        self.destino = destino
        self.quanty = quanty


    def save_transaction(self):
        from users.test import show
        global time


        validation_user = show(self.username)
        validation = validation_user.show_id()


        sql = """INSERT INTO Transacciones(id_Clientes, name_T, cantidad_T, destino, fecha_t)
                                                    VALUES (%s, %s, %s, %s, CURDATE())"""

        values = (validation, self.name_T, self.cantidad_T, self.destino)

        cursor.execute(sql, values)
        vldt = cursor.fetchone()
        database.commit()
        print("query solved")



        return [vldt, self]


    def refresh_acount(self):
        # actualizar cuenta:
        upgrade_balance = "UPDATE usuarios SET saldo = saldo - %s WHERE usuario = %s "
        upgrade_balance_values = (self.quanty, self.username)
        cursor.execute(upgrade_balance, upgrade_balance_values)
        database.commit()
        cursor.close()
        database.close()
        print("acount refresh")


        return [validation, self]











