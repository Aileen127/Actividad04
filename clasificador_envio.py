
# Solicitud de datos 
weight = float(input("Ingrese el peso del paquete en kg: "))
distance = float(input("Ingrese la distancia en km: "))
urgency = input("¿El envió es urgente? (si, no): ").lower()
size_package = input("Ingresa el tamaño del paquete (pequeño, mediano, grande): ").lower()

#Definición constantes y variables
URGENT = 50
BIG = 30
DISCOUNT = 20
mount = 25
if distance > 150:
    mount = 35

#Urgente, paquete grande y de más 5 kg o menos de 5 kg
if weight > 5 and urgency == "si" and size_package == "grande":
    total = mount + URGENT + BIG
    print("\n Cálculo total:")
    print(f"El paquete de peso {weight} kg que necesita recorrer una distancia de {distance} km \n Tiene un monto extra de urgencia de Q50 y por tamaño de paquete de Q30 ")
    print(f"Teniendo un total de {total}")
# Urgente, paquete no grande y  más de 5 kg o menos de 5kg
elif weight > 5 and urgency == "si" and size_package == "pequeño" or size_package == "mediano":
    total = URGENT + mount
    print("\n Cálculo total:")
    print(f"El paquete de peso {weight} kg que necesita recorrer una distancia de {distance} km \n Tiene un monto extra de urgencia de Q50")
    print(f"Teniendo un total de {total}")
# No urgente, paquete no grande, menos de 5 kg
elif weight < 5 and urgency == "no" and size_package == "pequeño" or size_package == "mediano":
    total = mount - DISCOUNT
    print("\n Cálculo total:")
    print(f"El paquete de peso {weight} kg que necesita recorrer una distancia de {distance} km \n Con un descuento de Q20")
    print(f"Teniendo un total de {total}")
# No urgente, paquete grande, menos de 5 kg
elif weight < 5 and urgency == "no" and size_package == "grande":
    total = mount + BIG
    print("\n Cálculo total:")
    print(f"El paquete de peso {weight} kg que necesita recorrer una distancia de {distance} km \n Tiene un monto extra por tamaño de paquete de Q30")
    print(f"Teniendo un total de {total}")
# No urgente, paquete no grande, más de 5 kg
elif weight > 5 and urgency == "no" and size_package == "pequeño" or size_package == "mediano":
    total = mount
    print("\n Cálculo total:")
    print(f"El paquete de peso {weight} kg que necesita recorrer una distancia de {distance} km")
    print(f"Teniendo un total de {total}")
else:
    print("Datos ingresados incorrectamente")
