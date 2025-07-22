
# Solicitud de datos 
weight = float(input("Ingrese el peso del paquete en kg: "))
distance = float(input("Ingrese la distancia en km: "))
urgency = input("¿El envió es urgente? (si, no): ").lower()
size_package = input("Ingresa el tamaño del paquete (pequeño, mediano, grande): ").lower()

#Definición constantes
URGENT = 50
BIG = 30
DISCOUNT = 20
MOUNT = 25

#Urgente, paquete grande y de más 5 kg
if weight > 5 and urgency == "si" and size_package == "grande":
    total = weight + URGENT + BIG + MOUNT
    print("\n Cálculo total:")
    print(f"El paquete de peso {weight} kg que necesita recorrer una distancia de {distance} km \n Tiene un monto extra de urgencia de Q50 y por tamaño de paquete de Q30 ")
    print(f"Teniendo un total de {total}")
# Urgente, paquete no grande y  más de 5 kg
elif weight > 5 and urgency == "si" and size_package == "pequeño" or size_package == "mediano":
    total = weight + URGENT + MOUNT
    print("\n Cálculo total:")
    print(f"El paquete de peso {weight} kg que necesita recorrer una distancia de {distance} km \n Tiene un monto extra de urgencia de Q50")
    print(f"Teniendo un total de {total}")
# Urgente, paquete no grande, menos de 5 kg


