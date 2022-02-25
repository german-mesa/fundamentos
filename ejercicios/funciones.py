# Programar en Python la función discontinua f(x) definida como:
# f(x) = x2 –3x, si x < 1
# f(x) = 10, si x = 1
# f(x) = 4x + 2, si x > 1
def funcion1(value):
    if value < 1:
        return pow(value, 2) - 3 * value
    elif value == 1:
        return 10
    else:
        return 4 * value + 2


# Programar en Python la función discontinua f(x) definida como:
# f(x) = x3 –3x2, si x < 1
# f(x) = 10, si x = 1
# f(x) = 4x2 + 2x -5, si x > 1
def funcion2(value):
    if value < 1:
        return pow(value, 3) - 3 * pow(value, 2)
    elif value == 1:
        return 10
    else:
        return 4 * pow(value, 2) + 2 * value - 5


# Funcion que convierte grados Celsius a Fahrenheit
# T(°F) = T(°C) × 9/5 + 32
def convertirCelsiusAFahrenheit(value):
    return round((value * 9 / 5) + 32, 2)


# Funcion que convierte grados Fahrenheit a Celsius
# T(°C) = (T(°F) - 32) × 5/9
def convertirFahrenheitACelsius(value):
    return round((value - 32) * 5 / 9, 2)


if __name__ == '__main__':
    print(f"El valor de la funcion1 para 1 es {funcion1(1)}")  # 10
    print(f"El valor de la funcion1 para 3 es {funcion1(3)}")  # 14
    print(f"El valor de la funcion1 para -1 es {funcion1(-1)}")  # 4

    print(f"El valor de la funcion2 para 1 es {funcion2(1)}")  # 10
    print(f"El valor de la funcion2 para 3 es {funcion2(2)}")  # 15
    print(f"El valor de la funcion2 para -1 es {funcion2(0)}")  # 0

    print(f"20.1ºC son {convertirCelsiusAFahrenheit(20.11)}ºF")
    print(f"68.2ºF son {convertirFahrenheitACelsius(68.18)}ºC")