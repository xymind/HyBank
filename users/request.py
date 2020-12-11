from conexion import conectar
import time
from time import sleep
import datetime
from tqdm import *
from users.test import show
from control_transactions import Control

connect = conectar()
database = connect[0]
cursor = connect[1]



class request_users():
    def __init__(self, username, IBAN):
        self.username = username
        self.IBAN = IBAN


    def tranference(self):

        global time


        query = """UPDATE usuarios SET saldo = saldo + %s WHERE IBAN = %s """
        quanty = float(input("Cantidad: "))

        values = quanty, self.IBAN

        # Control-balance
        saldo_obj = show(self.username)
        saldo_min = saldo_obj.show_balance()

        if saldo_min >= quanty:

            cursor.execute(query, (values))

            day = time.strftime("%d/%m/%y")
            time = time.strftime("%I:%M:%S")

            # Loading
            for index in tqdm(range(100), desc="Realizando tranferencia...",
                              ascii=False, ncols=75):
                sleep(0.02)
            print(f"Ingreso de {quanty} € al IBAN {self.IBAN}")

            database.commit()

            validation = cursor.fetchone()

            #save
            control_transaccion = Control(self.username, 'Transferencia', quanty, self.IBAN, quanty)
            control_transaccion.save_transaction()

            #refresh
            if validation:
                refresh = Control(self.username, "", quanty, self.IBAN, quanty)
                refresh.refresh_acount()


                database.commit()

            return validation

        else:
            print(f"No tienes suficiente saldo para realizar esta transacción, saldo: {saldo_min}")



    def setBalance(self):
        from users.test import show

        global time


        quanty = float(input("Cantidad de dinero a añadir a tu saldo: "))
        query = f"UPDATE usuarios SET saldo = saldo + %s WHERE usuario = %s "
        values = (quanty, self.username)
        cursor.execute(query,values)
        validation = cursor._fetch_row()

        if validation == None:
            database.commit()

            print("query leida")


            control = Control(self.username, 'Ingreso de dinero', quanty, self.IBAN, None)
            control.save_transaction()

            # Loading
            for index in tqdm(range(100), desc="Realizando Ingreso...",
                              ascii=False, ncols=75):
                sleep(0.02)
            print(f"!Hola {self.username} hemos echo un ingreso de {quanty} € !")




    def getBalance(self):
        query = "SELECT usuario, saldo FROM usuarios WHERE usuario = %s"
        values = (self.username)
        cursor.execute(query, (values,))
        validation = cursor.fetchone()

        if validation:
            print(f"Tu saldo es: {validation[1]} €")

        return [validation[1], self] #position 0 is balance

    def show_transactions(self):

        query = "SELECT * FROM Transacciones WHERE id_Clientes = %s"
        val = show(self.username)
        values = (val.show_id(),)
        cursor.execute(query, values)
        validation = cursor.fetchall()

        if validation:
            database.commit()

            # Loading
            for index in tqdm(range(100), desc="Cargando registros ...",
                              ascii=False, ncols=75):
                sleep(0.02)

            for x in validation:
                print(
                    f" *********** TRANSACCIONES *********** \nIDENTIFICADOR DE TRANSACCIÓN: {x[0]} \n TIPO DE TRANSACCIÓN: {x[2]} \n IMPORTE: {x[3]} \n IBAN DESTINO {x[4]} \n FECHA: {x[5]}")


    def give_money(self):

        # Control-balance
        saldo_obj = show(self.username)
        saldo_min = saldo_obj.show_balance()

        quanty = int(input("¿Cuánto dinero quieres sacar?: "))

        if saldo_min >= quanty:
            for index in tqdm(range(100), desc="Retirando Dinero, por favor espere...",
                              ascii=False, ncols=75):
                sleep(0.03)



            query = f"UPDATE usuarios SET saldo = saldo - {quanty} WHERE usuario = '{self.username}'"
            cursor.execute(query)
            validation = cursor.fetchone()
            if validation == None:
                print(f"{quanty}€ retirados correctamente")
                database.commit()

                # control_TR
                control_transaccion = Control(self.username, 'retiranda_balance', quanty, self.IBAN, quanty)
                control_transaccion.save_transaction()

                database.commit()



        else:
            print("error")













