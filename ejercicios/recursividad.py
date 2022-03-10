# Calcular el sumatorio de un número positivo
def sumatorio(value):
    if value == 0:
        return 0
    else:
        return value + sumatorio(value - 1)


# Calcular el factorial de un número positivo
def factorial(value):
    if value == 0:
        return 1
    else:
        return value * factorial(value - 1)


# Calcular la serie de Fibonacci - calcula el elemento n sumando los dos anteriores n-1 + n-2
def fibonacci(value):
    if value == 0:
        return 0
    elif value == 1:
        return 1
    else:
        return fibonacci(value - 1) + fibonacci(value - 2)


# Sumatorio de los componentes de una lista
def sumatorioLista(lista):
    if len(lista) == 0:
        return 0
    else:
        return lista[0] + sumatorioLista(lista[1:])


# Máximo de los componentes de una lista
def maximoLista(lista):
    if len(lista) == 1:
        return lista[0]

    else:
        return max(lista[0], maximoLista(lista[1:]))


# Mínimo de los componentes de una lista
def minimoLista(lista):
    if len(lista) == 1:
        return lista[0]

    else:
        return min(lista[0], minimoLista(lista[1:]))


if __name__ == '__main__':    
    print(f"El sumatorio de 5 es {sumatorio(5)}")  # 15
    print(f"El factorial de 5 es {factorial(5)}")  # 120

    print(f"El número de Fibonacci de 0 es {fibonacci(0)}")  # 1
    print(f"El número de Fibonacci de 1 es {fibonacci(1)}")  # 1
    print(f"El número de Fibonacci de 10 es {fibonacci(10)}")  # 55

    numeros = [2, 3, 5, 2, 11, 1, 7]
    print(
        f"La suma de los elementos de la lista [2, 3, 5, 2, 11, 1, 7] es {sumatorioLista(numeros)} = {sum(numeros)}")

    print(
        f"El máximo de los elementos de la lista [2, 3, 5, 2, 11, 1, 7] es {maximoLista(numeros)} = {max(numeros)}")

    print(
        f"El mínimo de los elementos de la lista [2, 3, 5, 2, 11, 1, 7] es {minimoLista(numeros)} = {min(numeros)}")
