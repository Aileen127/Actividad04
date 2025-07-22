# Simulador de facturación

# Lista en donde se guarda la info. del precio de productos
products = []
# Ciclo que se repite hasta que el usuario desee dejar de usarlo
while True:
    # Prevención de error dentro de la consola
    try:
        print("\nBienvenido al simulador de facturación con IVA")
        price = float(input("Ingrese el precio del producto  "))
        if price > 0:
            products.append(price)
        else:
            print("El precio no debe de ser negativo.")
    except ValueError:
        print("Ha ingresado un dato inválido, intente de nuevo.")

    add_more = input("¿Desea agregar más productos? (si, no)").lower()
    if add_more == "no":
        break




