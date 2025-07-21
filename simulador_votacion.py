# Simulador votacion

# Menu
print("\n Bienvenido al menú de votaciones")

while True:
# Verificaciones

    # Verificacion name
    name = str(input("Ingresa tu nombre completo: ")).strip()
    if len(name) > 5:
        print("Nombre ingresado correctamente")
    else:
        print("El nombre debe de tener más de 5 letras.")
        break

    # Verificacion dpi
    dpi = input("Ingresa tu número de dpi: ").strip()

    if len(dpi) == 13:
        print("El dpi es valido")
    else:
        print("El dpi no cuenta con los caracteres suficientes.")
        break

    #Verificación departamento
    state = str(input("Ingresa el departamento en el que reside")).lower()
    if state = "péten" or state = "alta verapaz":
        special_age = int(input("Ingresa el año en el que naciste: "))
        if special_age >= 2008:
            print(f"Bienvenido {name}, su centro de votación esta en {state}")
        elif special_age < 2008:
            print("Edad no válida para votar")



