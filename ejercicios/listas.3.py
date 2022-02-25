def hashtag(lista):
    frase = ""
    temp = []

    for palabra in lista:
        if str.isupper(palabra):
            palabra = "#" + palabra

        temp.append(palabra)
        frase = frase + " " + palabra 

    return temp, frase


def cuenta_vocales(palabra):
    minusculas = palabra.lower()

    contador_vocales = {}

    for vocal in 'aeiou':
        contador_vocales[vocal] = minusculas.count(vocal)

    return sum(contador_vocales.values())


def suma_lista(lista):
    if len(lista) == 0:
        return 0
    else:
        return lista[0] + suma_lista(lista[1:])


def max_lista(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        return max(lista[0], max_lista(lista[1:]))

def min_lista(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        return min(lista[0], min_lista(lista[1:]))

def main():
    frase = 'Ahora el que no esta MAL informado es porque no QUIERE'

    # Convierte la frase en palabras
    # CODE HERE -->
    palabras = frase.split()
    # CODE HERE <-- 
    print(f"La lista de palabras es {palabras}")

    # Poner un # a las palabras mayúsculas
    palabras, frase = hashtag(palabras)
    print(f"La frase es {frase}")

    # Ordena lista de palabras
    # CODE HERE -->
    palabras.sort()
    # CODE HERE <-- 
    print(f"La lista de palabras ordenada {palabras}")

    # Ordena lista de palabras por su longitud
    # CODE HERE -->
    palabras.sort(key=len)
    # CODE HERE <-- 
    print(f"La lista de palabras ordenada por longitud {palabras}")

    # Ordena lista de palabras por número de vocales
    # CODE HERE -->
    palabras.sort(key=lambda x: cuenta_vocales(x))
    # CODE HERE <-- 
    print(f"La lista de palabras ordenada por número de vocales {palabras}")

    # Lista de números
    numeros = [2, 3, 5, 2, 11, 2, 7]

    print(f"Su valor máximo es {max_lista(numeros)} =  {max(numeros)}")
    print(f"Su valor mínimo es {min_lista(numeros)} = {min(numeros)}")
    print(f"Su valor suma es {suma_lista(numeros)} = {sum(numeros)}")


if __name__ == '__main__':
    main()