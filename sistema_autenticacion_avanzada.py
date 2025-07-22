# Sistema de autenticación

# Listas de usuarios
users = ["Juan", "Maria", "Pedro"]
# Listas de contraseñas
passwords = ["Hola123", "flan098", "159num"]

# Ciclo for que cuenta las oportunidades de ingreso
for attempt in range(3):
    user = input("Ingresa el usuario por favor: ")
    if user in users:
        password = input("Ingresa la contraseña por favor: ")
        if password in passwords:
            print("\n Bienvenido al menú")
            print("1. Ver perfil")
            print("2. Cambiar contraseña")
            print("Cerrar sesión")
        else:
            print("Acceso denegado")
    else:
        print("Acceso denegado.")
