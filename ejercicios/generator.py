import time

# Calcular el número de Fibonacci usando un generator
def generator_fibonacci():
    actual, siguiente = 0, 1

    while True:
        actual, siguiente = siguiente, actual + siguiente
        yield actual

# Ver si el número es par utilizando un generator
def generator_pares(numeros):
    for i in numeros:
        if i%2 == 0:
            yield i


# Calcular el número de Fibonacci método clásico
def classic_fibonacci(limite):
    numeros = []

    actual, siguiente = 0, 1

    while len(numeros) < limite:
        actual, siguiente = siguiente, actual + siguiente
        numeros.append(actual)

    return numeros


# Secuencia de Fibonacci midiendo tiempos
def secuencia_clasica_fibonacci(limite):
    print("Secuencia de Fibonacci - Classic approach")

    comienzo = time.time()

    resultado = classic_fibonacci(limite)

    for i in resultado:
        pass 

    final = time.time() - comienzo

    print(f'Tiempo transcurrido: {final}')


# Secuencia de Fibonacci midiendo tiempos
def secuencia_generator_fibonacci(limite):
    print("Secuencia de Fibonacci - Generator approach")

    contador = 0
    comienzo = time.time()

    for i in generator_fibonacci():
        if contador > limite:
            break

        contador += 1

    final = time.time() - comienzo

    print(f'Tiempo transcurrido: {final}')

# Secuencia de Fibonacci pares midiendo tiempos
def secuencia_generator_fibonacci_pares(limite):
    print("Números pares en una secuencia de Fibonacci - Generator approach")

    contador = 0
    comienzo = time.time()

    for i in generator_pares(generator_fibonacci()):
        if contador > limite:
            break

        contador += 1

    final = time.time() - comienzo

    print(f'Tiempo transcurrido: {final}')


def main():
    numero = 1000000

    # Calculo Fibonacci hasta que pasa de un valor máximo
    # secuencia_clasica_fibonacci(numero)

    # Idem utilizando generator para no consumir tanta memoria
    secuencia_generator_fibonacci(numero)

    # Encauzo la salida de un generador a otro
    secuencia_generator_fibonacci_pares(numero)


if __name__ == '__main__':
    main()