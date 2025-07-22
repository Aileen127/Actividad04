# Calculadora de impuestos progresivos

# Solicitación de variables
MONTO_DEPENDIENTE = 1000
ingreso_anual = float(input("Ingresa el mónto de ingresos anuales en quetzales: "))

if ingreso_anual >= 0 and ingreso_anual <= 30000:
    dependiente = int(input("Ingresa la cantidad de dependientes: "))
    if dependiente > 2:
        print("Usted no paga impuestos.")
    elif dependiente > 0 and dependiente <= 2:
        impuesto = ingreso_anual * 0.05
        total = ingreso_anual - (MONTO_DEPENDIENTE * dependiente) - impuesto
        print(f"El ingreso total con impuestos y deducción de dependientes es de Q{total}")

elif ingreso_anual > 30000 and ingreso_anual <= 60000:
    if ingreso_anual <= 40000:
        dependiente = int(input("Ingresa la cantidad de dependientes: "))
        if dependiente > 2:
            print("Usted no paga impuestos.")
        elif dependiente > 0 and dependiente <= 2:
            impuesto = ingreso_anual * 0.05
            total = ingreso_anual - (MONTO_DEPENDIENTE * dependiente) - impuesto
            print(f"El ingreso total con impuestos y deducción de dependientes es de Q{total}")
    elif ingreso_anual > 40000:
        dependiente = int(input("Ingresa la cantidad de dependientes: "))
        impuesto = ingreso_anual * 0.05
        total = ingreso_anual - (MONTO_DEPENDIENTE * dependiente) - impuesto
        print(f"El ingreso total con impuestos y deducción de dependientes es de Q{total}")