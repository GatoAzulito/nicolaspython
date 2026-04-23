def shazam():
    palabra="shazam"
    palabra2=input("Ingrese una palabra: ").lower()
    if palabra==palabra2:
        print("La palabra es correcta")
    else:
        print("La palabra es incorrecta")

def usuario():
    nombre_usuario=input("Ingrese su nombre de usuario: ")
    longitud=len(nombre_usuario)
    print(longitud)
    if longitud>3 and longitud<10:
        print("El nombre de usuario tiene una longitud correcta")
    else:
        print("El nombre de usuario tiene una longitud incorrecta")

def contrasena():
    passw=int(input("Ingrese su contraseña: "))
    longitud=len(str(passw))
    if longitud==4:
        print("Contraseña correcta")
    else:
        print("Contraseña incorrecta")
contrasena()
