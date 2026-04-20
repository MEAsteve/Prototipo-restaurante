from login import registrar_usuario 
from login import loggin

while True:
        print("\n1. Registrar")
        print("2. Login")
        print("3. Salir")

        opcion = input("Seleccione: ")

        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            loggin()
        elif opcion == "3":
            break
        else:
            print("Opción inválida")