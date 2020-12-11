import sys
import users.register as register
import conexion
import hashlib

connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

class logout():

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login_user(self):
        username = "admin"
        password = "admin"

         #CIFRADO

        cifrado = hashlib.sha256()  # DESARROLLO DEL OBJETO
        cifrado.update(self.password.encode('utf-8'))


        try:
            query = "SELECT usuario, contraseña FROM usuarios WHERE usuario = %s AND contraseña = %s "
            values = (self.username, cifrado.hexdigest())

            cursor.execute(query, values)
            result = cursor.fetchone()
            print("Ok")

            return result

        except Exception as e:
            print(type(e))
            print(type(e).__name__)
            print("¡Error, nombre de usuario o contraseña desconocida!")
            return e






