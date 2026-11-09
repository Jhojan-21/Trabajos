
import random
import math

print("   CALCULO DE AREA POR MONTECARLO")


# Solicitar datos al usuario
a = float(input("Ingrese el valor de a (elipse): "))
b = float(input("Ingrese el valor de b (elipse): "))
c = float(input("Ingrese el valor de c (hiperbola): "))
d = float(input("Ingrese el valor de d (hiperbola): "))

cantidad = int(input("Ingrese la cantidad de puntos aleatorios: "))

# Validar los datos
if a <= 0 or b <= 0 or c <= 0 or d <= 0 or cantidad <= 0:
    print("Error: todos los valores deben ser positivos.")
else:

    puntos_elipse = 0
    puntos_interseccion = 0

    # Generar puntos aleatorios
    for i in range(cantidad):

        x = random.uniform(-a, a)
        y = random.uniform(-b, b)

        # Comprobar si el punto está dentro de la elipse
        dentro_elipse = (x**2 / a**2) + (y**2 / b**2) <= 1

        # Comprobar si el punto está dentro de la hipérbola
        dentro_hiperbola = (x**2 / c**2) - (y**2 / d**2) >= 1

        if dentro_elipse:
            puntos_elipse += 1

            if dentro_hiperbola:
                puntos_interseccion += 1

    # Calcular área de la elipse
    area_elipse = math.pi * a * b

    # Calcular área aproximada de la intersección
    if puntos_elipse > 0:
        area_interseccion = (
            puntos_interseccion / puntos_elipse
        ) * area_elipse
    else:
        area_interseccion = 0
        
    print("\n===== RESULTADOS =====")

    print("Puntos dentro de la elipse:", puntos_elipse)

    print("Puntos en la interseccion:",
          puntos_interseccion)

    print("Area de la elipse:",
          round(area_elipse, 4))

    print("Area aproximada de la interseccion:",
          round(area_interseccion, 4))

