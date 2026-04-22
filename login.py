# LISTAS DE USUARIOS
usuarios = ["admin", "marlon", "kevin"]
claves = ["admin123*", "1234", "abcd"]
def loggin():
    intentos = 0
    acceso = False

    while intentos < 4 and acceso == False:

        user = input("Usuario: ")
        clave = input("Contraseña: ")

        encontrado = False

        for i in range(len(usuarios)):
            if user == usuarios[i] and clave == claves[i]:
                encontrado = True

        if encontrado == True:
            print("Acceso correcto")
            acceso = True
        else:
            print("Datos incorrectos")
            intentos = intentos + 1
            print("Intento", intentos, "de 4")

    if acceso == True:
        print("Bienvenido al sistema")
    else:
        print("Acceso bloqueado")
    return acceso
    
    
def registrar_usuario():
    correo = input("Ingrese correo: ")
    password = input("Ingrese contraseña: ")
    usuarios.append( correo )
    claves.append( password)
    print("Usuario registrado correctamente\n")    