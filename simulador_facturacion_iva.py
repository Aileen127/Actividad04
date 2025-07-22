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

# Preguntas especificas
total_list = sum(products)
C_CARD = 0.10
IVA = 0.12
tip = input("¿Desea dejar propina? (si, no)").lower()
if tip == "si":
    mount_tip = int(input("Ingresa el monto de propina que deseas dejar"))
    if mount_tip > 0 and mount_tip < 100:
        total_tip = mount_tip / 100


        client_card = input("¿Tiene tarjeta de cliente frecuente? (si, no)").lower()
        if client_card == "si":
            discount_client_card = total_list * C_CARD
            iva_mount = total_list * IVA
            total = total_list - discount_client_card + iva_mount - total_tip

            print("\nTotales calculados")
            print(f"- Subtotal:{total_list} \n - IVA: {iva_mount} \n - Propina: {total_tip} \n - Descuento: {discount_client_card} \n Total: {total}")
        elif client_card == "no":

    else:
        print("Ingresa un dato válido.")
elif tip == "no":
