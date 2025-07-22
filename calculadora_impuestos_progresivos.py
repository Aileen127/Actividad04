# Calculadora de impuestos progresivos

# Solicitación de variables
MONTO_DEPENDIENTE = 1000
ingreso_anual = float(input("Ingresa el mónto de ingresos anuales en quetzales: "))

# Monto ingreso de 0 a 30000
if ingreso_anual >= 0 and ingreso_anual <= 30000:
    dependiente = int(input("Ingresa la cantidad de dependientes: "))
    if dependiente > 2:
        print("Usted no paga impuestos.")
    elif dependiente > 0 and dependiente <= 2:
        impuesto = ingreso_anual * 0.05
        total = ingreso_anual - (MONTO_DEPENDIENTE * dependiente) - impuesto
        print(f"El ingreso total con impuestos y deducción de dependientes es de Q{total}")

# Monto de 30000 a 60000
elif ingreso_anual > 30000 and ingreso_anual <= 60000:
    if ingreso_anual <= 40000:
        dependiente = int(input("Ingresa la cantidad de dependientes: "))
        if dependiente > 2:
            print("Usted no paga impuestos.")
        elif dependiente > 0 and dependiente <= 2:
            impuesto = ingreso_anual * 0.10
            total2 = ingreso_anual - (MONTO_DEPENDIENTE * dependiente) - impuesto
            print(f"El ingreso total con impuestos y deducción de dependientes es de Q{total2}")
    # Monto condición extra
    elif ingreso_anual > 40000:
        dependiente = int(input("Ingresa la cantidad de dependientes: "))
        impuesto = ingreso_anual * 0.10
        total3 = ingreso_anual - (MONTO_DEPENDIENTE * dependiente) - impuesto
        print(f"El ingreso total con impuestos y deducción de dependientes es de Q{total3}")

# Monto anual 60001 - 100000
elif ingreso_anual > 60000 and ingreso_anual <= 100000:
    dependiente = int(input("Ingresa la cantidad de dependientes: "))
    impuesto = ingreso_anual * 0.15
    total4 = ingreso_anual  - (MONTO_DEPENDIENTE * dependiente) - impuesto
    print(f"El ingreso total con impuestos y deducción de dependientes es de Q{total4}")

# Monto más de 10000
elif ingreso_anual > 10000:
    dependiente = int(input("Ingresa la cantidad de dependientes: "))
    impuesto = ingreso_anual * 0.20
    total5 = ingreso_anual - (MONTO_DEPENDIENTE * dependiente) - impuesto
    print(f"El ingreso total con impuestos y deducción de dependientes es de Q{total5}")