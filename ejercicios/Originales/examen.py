jugadores = {}

def crearHashtags():
    for item in jugadores.items():
        descripcion = item[1]['descripcion']
        
        palabras = descripcion.split()

        for index, palabra in enumerate(palabras):
            if str.isupper(palabra):
                palabra = '#' + palabra

            palabras[index] = palabra

        item[1]['descripcion'] = ' '.join(palabras)


def incluirPartida(jugador: str, descripcion: str, partida: str, tiempo: float):
    if jugador in jugadores:    # Está en la BBDD
        jugadores[jugador]['descripcion'] = descripcion
        jugadores[jugador]['partidas'].append((partida, tiempo))

    else:                       # No está en la BBDD
        jugadores[jugador] = {'descripcion': descripcion, 'partidas': [(partida, tiempo)]}


def main():
    # Metiendo los jugadores
    incluirPartida('juan', 'Me llamo juan y me gusta MINECRAFT y AMONGUS', 'portal2', 45.0)
    incluirPartida('juan', 'Me llamo Juan y me gusta mucho MINECRAFT y AMONGUS', 'amongus', 10.2)
    incluirPartida('juan', 'Me llamo Juan y me gusta mucho MINECRAFT y AMONGUS', 'amongus', 100.2)
    incluirPartida('pepe', 'Soy pepe y mi juego preferido es MINECRAFT', 'amongus', 12.5)
    incluirPartida('ana', 'Soy ana y suelo jugara a MINECRAFT', 'minecraft', 20.3)
    incluirPartida('ana', 'Soy ana y suelo jugara a MINECRAFT', 'minecraft', 22.3)
    incluirPartida('ana', 'Soy ana y suelo jugara a MINECRAFT', 'amongus', 22.3)

    # Crear hashtags
    crearHashtags()

    print(jugadores)

if __name__ == '__main__':
    main()