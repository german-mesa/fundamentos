import matplotlib.pyplot as plt


def funcion(value):
    if value < 1:
        return pow(value, 2) - 3 * value
    elif value == 1:
        return 10
    else:
        return 4 * value + 2


def main():
    x = []
    y = []

    # list - inicializar, append, borrado de elementos, sumas, conteos,...
    for i in range(-10, 11, 1):
        x.append(i)
        y.append(funcion(i))

    plt.plot(x, y)
    plt.show()

    # Ordenando listas de números
    numbers = [2, 3, 5, 2, 11, 2, 7]
    print(f"La lista es {numbers}")

    numbers.extend([9, 12, 24])
    print(f"Extendemos la lista con [9, 12, 24]. La lista es ahora {numbers}")

    numbers.sort()
    print(f"La lista ordenada en orden creciente es {numbers}")

    numbers.sort(reverse=True)
    print(f"La lista ordenada en orden decreciente es {numbers}")

    print(f"La lista suma ahora {sum(numbers)}")
    print(f"Su valor máximo es {max(numbers)}")
    print(f"Su valor mínimo es {min(numbers)}")
    print(f"El numero 2 aparece {numbers.count(2)} veces")

    # Lista de vocales
    vocales = ['a', 'e', 'i', 'u']

    # Insertamos 'o' en la 4 posición
    vocales.insert(3, 'o')

    vocales.sort()
    print(f"La lista de vocales ordenada en orden creciente es {vocales}")

    # Ordenando listas de strings
    palabras = ['El', 'papa', 'de', 'Patxi', 'es', 'pelotari']

    palabras.sort(key=len)
    print(f"La lista de palabras ordenada por longitud {palabras}")


if __name__ == '__main__':
    main()
