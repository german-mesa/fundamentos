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


def selection_sort(lista):
    for i in range(0, len(lista)-1):
        index_min = i

        for j in range(i+1, len(lista)):
            if lista[j] < lista[index_min]:
                valor_min = j

        if valor_min != i:
            lista[i], lista[index_min] = lista[index_min], lista[i] 

    return lista

# Utilizar la funcion min() mientras vamos haciendo el loop
def selection_sort_min(lista):
    for i in range(0, len(lista)):
        valor_min = min(lista[i:])
        index_min = lista.index(valor_min)

        lista[i], lista[index_min] = lista[index_min], lista[i] 

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

if __name__ == '__main__':
    main()