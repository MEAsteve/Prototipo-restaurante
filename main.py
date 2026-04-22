from login import registrar_usuario 
from login import loggin
from menu import menu

while True:
        print("\n1. Registrar")
        print("2. Login")
        print("3. Salir")

        opcion = input("Seleccione: ")

        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            llave=loggin()
            if llave == True :
                menu()
            elif  llave==False :
                print("Paila mijo")
                
        elif opcion == "3":
            break
        else:
            print("Opción inválida")