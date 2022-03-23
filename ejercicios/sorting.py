# Cómo funciona el algoritmo
# https://www.youtube.com/watch?v=g_xesqdQqvA&t=231s
def bubble_sort(lista):
    ordenada = False
    tamano = len(lista) - 1

    while not ordenada:
        ordenada = True

        for i in range(0, tamano):
            if lista[i] > lista[i+1]:
                ordenada = False
                lista[i], lista[i+1] = lista[i+1], lista[i]
        
    return lista

# Cómo funciona el algoritmo
# https://www.youtube.com/watch?v=kFeXwkgnQ9U
def quick_sort(lista):
    tamano = len(lista)

    if tamano <= 1:
        return lista
    else:
        pivot = lista.pop()

    lista_menor = []
    lista_mayor = []

    for elemento in lista:
        if elemento > pivot:
            lista_mayor.append(elemento)
        else:
            lista_menor.append(elemento)
            
    return quick_sort(lista_menor) + [pivot] + quick_sort(lista_mayor)

# Cómo funciona el algoritmo
# https://www.youtube.com/watch?v=4CykZVqBuCw
def selection_sort(lista):
    for i in range(0, len(lista)-1):
        index_min = i

        for j in range(i+1, len(lista)):
            if lista[j] < lista[index_min]:
                index_min = j

        if index_min != i:
            lista[i], lista[index_min] = lista[index_min], lista[i] 

    return lista

# Utilizar la funcion min() mientras vamos haciendo el loop
def selection_sort_min(lista):
    for i in range(0, len(lista)):
        valor_min = min(lista[i:])
        index_min = lista.index(valor_min)

        lista[i], lista[index_min] = lista[index_min], lista[i] 

    return lista

# Cómo funciona el algoritmo
# https://www.youtube.com/watch?v=byHi41L9vTM&t=276s
def insertion_sort(lista):
    for i in range(1, len(lista)):
        elemento = lista[i]
  
        while lista[i-1]>elemento and i>0:
            lista[i], lista[i-1] = lista[i-1], lista[i]
            i -= 1

    return lista


def main():
    lista = [3, 7, 5, 4, 8, 9, 12, 11, 24]
    print(f'La lista original es {lista}')

    # Ordeno con algoritmo bubble sort
    lista = [3, 7, 5, 4, 8, 9, 12, 11, 24]
    print(f'La lista ordenada con bubble sort es {bubble_sort(lista)}')

    # Ordeno con algoritmo quick sort
    lista = [3, 7, 5, 4, 8, 9, 12, 11, 24]
    print(f'La lista ordenada con quick sort es {quick_sort(lista)}')

    # Ordeno con algoritmo selection sort
    lista = [3, 7, 5, 4, 8, 9, 12, 11, 24]
    print(f'La lista ordenada con selection sort es {selection_sort(lista)}')

    # Ordeno con algoritmo selection sort
    lista = [3, 7, 5, 4, 8, 9, 12, 11, 24]
    print(f'La lista ordenada con selection sort con la funcion min es {selection_sort_min(lista)}')

    # Ordeno con algoritmo insertion sort
    lista = [3, 7, 5, 4, 8, 9, 12, 11, 24]
    print(f'La lista ordenada con insertion sort es {insertion_sort(lista)}')

if __name__ == '__main__':
    main()