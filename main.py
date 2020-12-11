import users.register as register
import users.login as login
import users.request as request
import datetime
import time

class usuario():

    def option_user(self):
        options = """ 1: Realizar tranferencia \n 2: Ingresar saldo \n 3: Consultar saldo \n 4: Ver movimientos \n 5: Retirar dinero: \n 6: Salir"""

        global option

        print("Bienvenido a HyPlexBank \n Elige opción: \n -1:Iniciar sesión \n -2:Registrarte \n -3:Salir")
        try:
            option = int(input("Introduce la opción que deseas: "))
        except:
            option = int(input("Opción incorrecta, Vuelve a elegir opción: "))


        if option == 1:


            username = input("Introduce tu usuario: ")
            password = str(input("Introduce tu contraseña: "))

            user_sesion = login.logout(username, password)
            logueo = user_sesion.login_user()

            if logueo:
                global time
                fecha = time.strftime("%d/%m/%y")
                time = time.strftime("%I:%M:%S")

                print(f"Bienvenido {logueo[0]} has ingresado correctamente , fecha {fecha, time}")

                print(options)

                options_user = int(input("Introduce opcion: "))


                while options_user > 0 and options_user <= 6:
                    if options_user == 1:
                        destination = input("Escribe el IBAN del destinatario:  ")

                        tranference_user = request.request_users(username, destination)

                        tranference_user.tranference()

                        tranference_user.getBalance()
                        print(options)
                        options_user = int(input("Introduce opcion: "))



                    elif options_user == 2:
                        set_balance_users = request.request_users(username, "")
                        set_balance_users.setBalance()
                        print(options)
                        options_user = int(input("Introduce opcion: "))






                    elif options_user == 3:
                        get_balance_users = request.request_users(username, "")
                        get_balance_users.getBalance()
                        print(options)
                        options_user = int(input("Introduce opcion: "))


                    elif options_user == 4:
                        get_tranferences = request.request_users(username, "")
                        get_tranferences.show_transactions()
                        print(options)
                        options_user = int(input("Introduce opcion: "))

                    elif options_user == 5:
                        give_money = request.request_users(username, "")
                        give_money.give_money()
                        print(options)
                        options_user = int(input("Introduce opcion: "))


                    elif options_user == 6:
                        print("Bye!")
                        exit()

                else:
                    print("Datos Erróneos")


        elif option == 2:
            username = input("Introduce un nombre para el registro: ")
            password = str(input("Introduce una contraseña: "))
            saldo = 0

            user_register = register.Register(username, password, saldo)
            registro = user_register.register_user()

            if registro[0] >= 1:
                print(options)
                options_user = int(input("Introduce opcion: "))

                if options_user == 1:

                    destination = input("Escribe el IBAN del destinatario:  ")

                    tranference_user = request.request_users(username, destination)

                    tranference_user.tranference()

                    tranference_user.getBalance()
                    print(options)
                    options_user = int(input("Introduce opcion: "))

                elif options_user == 2:
                    set_balance_users = request.request_users(username, "")
                    set_balance_users.setBalance()
                    print(options)
                    options_user = int(input("Introduce opcion: "))



                elif options_user == 3:
                    get_balance_users = request.request_users(username, "")
                    get_balance_users.getBalance()
                    print(options)
                    options_user = int(input("Introduce opcion: "))


                elif options_user == 4:
                    get_tranferences = request.request_users(username, "")
                    get_tranferences.show_transactions()
                    print(options)
                    options_user = int(input("Introduce opcion: "))




                elif options_user == 5:
                    give_money = request.request_users(username, "")
                    give_money.give_money()
                    print(options)
                    options_user = int(input("Introduce opcion: "))



                elif options_user == 6:
                    print("Bye")
                    exit()


            else:
                print("No te has registrado correctamente!")



if __name__ == "__main__":

    y = usuario()
    y.option_user()







