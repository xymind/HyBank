import sys
import conexion
import random
import datetime
import hashlib
import time


#CONECCION DB
connect = conexion.conectar()
database = connect[0]
cursor = connect[1]


class Register(object):

    def __init__(self, username, password, saldo):
        self.username = username
        self.password = password
        self.saldo = saldo



    def register_user(self):
        global IBAN
        global time
        fecha = time.strftime("%d/%m/%y")
        time = time.strftime("%I:%M:%S")
        IBAN = random.randint(1000000, 2000000)

        # CIFRADO
        cifrado = hashlib.sha256()  # DESARROLLO DEL OBJETO
        cifrado.update(self.password.encode('utf-8'))  # permite pasarle dato a cifrar, datos a cifrar en BYTES


        try:
            query = "INSERT INTO usuarios(usuario, contraseña, IBAN, saldo, fecha) VALUES (%s , %s, %s, %s, %s)"
            values = (self.username, cifrado.hexdigest(), IBAN, self.saldo, fecha)

            cursor.execute(query, values)
            database.commit()


            print(f"!Registro satisfactorio{fecha, time}!")

            result = [cursor.rowcount, self]

        except:
            print("¡registro Insatisfactorio!\n intentalo más tarde")
            result = [0, self]


        return result





