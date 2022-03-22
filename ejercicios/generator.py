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


def main():
    #
    # Ejemplo 1 - Cálculo de la secuencia de Fibonacci
    #

    # Número de valores en la secuencia
    numero = 10
    print(f'Ejemplo 1 - Cálculo de la secuencia de Fibonacci', end='\n')

    # Calculo Fibonacci
    print('\nCalculo la secuencia de Fibonacci')
    secuencia_classic = classic_fibonacci(numero)
    print(*secuencia_classic, end='\n')

    # Idem utilizando generator para no consumir tanta memoria
    print('\nIdem utilizando generator')
    for idx, item in enumerate(generator_fibonacci()):
        if idx == numero:
            break

        print(item, end=',')
    
    print('\nFin del ejemplo 1')

    #
    # Ejemplo 2 - Cálculo de la secuencia de Fibonacci para números grandes
    #

    # Número de valores en la secuencia
    numero = 1000
    print(f'\nEjemplo 2 - Veamos el tiempo que tarda el generator para números grandes {numero}', end='\n')


    # Veamos el tiempo que tarda el clásico para números grandes
    comienzo = time.time()
    secuencia_classic = classic_fibonacci(numero)
    print(f'\nCalculo la secuencia de Fibonacci de forma clásica para {numero} numeros en {time.time() - comienzo}')

    # Veamos el tiempo que tarda el generator para números grandes
    comienzo = time.time()
    for idx, item in enumerate(generator_fibonacci()):
        if idx == numero:
            break
    print(f'\nCalculo la secuencia de Fibonacci con el generador para {numero} numeros en {time.time() - comienzo}')



    # Ejemplo 3 - Encauzo la salida de un generador a otro
    print('\nEncauzo la salida de un generador a otro')
    for idx, item in enumerate(generator_pares(generator_fibonacci())):
        if idx > 5:
            break
    
        print(item, end=',')


if __name__ == '__main__':
    main()