import math
import numpy as np


def main():
    # Lists
    numbers = [49, 64, 81, 100, 121]

    # Utilizando map
    sqrt_numbers = list(map(math.sqrt, numbers))
    print(f'Raíz cuadrada de una lista (map): {sqrt_numbers}')

    # Utilizando comprenhension
    sqrt_numbers = [math.sqrt(i) for i in numbers]
    print(f'Raíz cuadrada de una lista (comprenhension): {sqrt_numbers}')

    # Creo tuples utilizando comprenhension
    sqrt_numbers = [(i, math.sqrt(i)) for i in numbers]
    print(f'Raíz cuadrada de una lista: {sqrt_numbers}')
    
    # Utilizando numpy - librería
    sqrt_numbers = np.sqrt(numbers)
    print(f'Raíz cuadrada de una lista (numpy): {sqrt_numbers}')

    # Dictionary
    compra = {'leche': 1.02, 'café': 2.5, 'pan': 0.95}

    # Creo diccionario utilizando loop
    compra_nueva = {}

    for key, value in compra.items():
        compra_nueva[key] = value
    print(compra_nueva)

    # Creo diccionario utilizando comprenhension
    compra_nueva = {key: value*1.10 for key, value in compra.items()}
    print(compra_nueva)

    # Creo diccionario utilizando loop con condiciones
    for key, value in compra.items():
        if value > 2.0:
            compra_nueva[key] = value * 1.10
        else:
            compra_nueva[key] = value
    print(compra_nueva)

    # Creo diccionario utilizando comprenhension con condiciones
    compra_nueva = {key: value*1.10 if value > 2.0 else value for key, value in compra.items()}
    print(compra_nueva)


if __name__ == '__main__':
    main()