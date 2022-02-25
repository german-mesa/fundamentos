from asyncio import SendfileNotAvailableError


juegos = [('amongus', 12.5), ('minecraft', 24.2), ('minecraft', 28.2), ('supermario odissey', 45.5)]

def get_duracion(juego):
    return juego[1]

def main():
    # Añadir un registro a una lista
    juegos.append(('supermario odissey', 12.3))

    # Añadir varios registros a una lista
    juegos.extend([("portal2", 45.0), ("amongus", 10.2)])

    # Ordenar por clave
    sorted_juegos = sorted(juegos)
    print(f'Juegos ordenados por nombre {sorted_juegos}')

    sorted_juegos = sorted(juegos, key=get_duracion)
    print(f'Juegos ordenados por duración {sorted_juegos}')
    
    # Loop sobre una lista
    print(f'\nLoop en diccionario utilizando enumerate() {max(sorted_juegos)}')

    print(f'\nLoop en diccionario utilizando items()')


    # Algunas cosas que pueden hacerse con loops
    print(f'\nAlgunas cosas que pueden hacerse con loops')


if __name__ == '__main__':
    main()