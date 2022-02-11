jugadores = {
    'Alan Turing': {
        'descripcion': 'Soy Alan y mi juego preferido es MINECRAFT.',
        'partidas': [('amongus', 12.5), ('minecraft', 24.2), ('minecraft', 28.2), ('supermario odissey', 45.5)]
    },
    'Sharon Lin': {
        'descripcion': 'Me llamo Sharon y me gusta MINECRAFT y AMONGUS.',
        'partidas': [('minecraft', 45.0), ('amongus', 10.2)]
    }
}


# Partidas por jugador
def obtenerPartidasJugador(jugador: str):
    return jugadores[jugador].get('partidas')


# Todas las partidas jugadas por todos los jugadores
def obtenerPartidas():
    partidas = []

    for jugador in jugadores:
        partidas.extend(obtenerPartidasJugador(jugador))

    return partidas


# Esta el juego en la lista de partidas
def existePartida(juego: str, partidas):
    if partidas:
        if juego == partidas[0][0]:
            return True
        else:
            return True and existePartida(juego, partidas[1:])
    else:
        return False


# Ha jugado el jugador al menos una vez
def validarPartidaJugador(jugador: str, juego: str) -> bool:
    if jugador in jugadores:
        return existePartida(juego, obtenerPartidasJugador(jugador))
    else:
        return False


# ¿Cuál es el juego más popular?
def obtenerRankingJuegos():
    # Cuento los juegos en un diccionario
    ranking = {}

    for partida in obtenerPartidas():
        if partida[0] in ranking:  # Como esta en la coleccion le añado uno mas
            ranking[partida[0]] += 1
        else:  # No esta en la coleccion
            ranking[partida[0]] = 1

    # Lo convierto a lista para ordenar de mayor a menor
    ranking = list(ranking.items())
    ranking.sort(key=lambda x: x[1], reverse=True)

    return ranking[0]


# Obtiene el ranking de los `m` mejores jugadores del juego
def obtenerRankingJugadores(juego: str, m: int) -> list:
    ranking = {}

    for jugador in jugadores:
        for partida in obtenerPartidasJugador(jugador):
            if partida[0] == juego:
                if jugador in ranking:
                    if ranking[jugador] > partida[1]:
                        ranking[jugador] = partida[1]
                else:
                    ranking[jugador] = partida[1]

    # Lo convierto a lista para ordenar de menor a mayor
    ranking = list(ranking.items())
    ranking.sort(key=lambda x: x[1])

    if m > len(ranking):
        m = len(ranking) - 1

    return ranking[:m]


# Añadir hastags en la descripción de cada jugador
def crearHashtags():
    for jugador in jugadores:
        descripcion = ""

        for word in str.split(jugadores[jugador]['descripcion']):
            if str.isupper(word):
                descripcion += "#"
            descripcion += word + " "

        jugadores[jugador]['descripcion'] = descripcion


# Añadir partida en la BBDD
def incluirPartida(jugador: str, descripcion: str, partida: str, tiempo: float):
    if jugador in jugadores:  # Update existing player
        jugadores[jugador]['descripcion'] = descripcion
        jugadores[jugador]['partidas'].append((partida, tiempo))

    else:  # Add a new player
        jugadores[jugador] = {'descripcion': descripcion, 'partidas': [(partida, tiempo)]}


# Incluir partidas en la BBDD
def creaBBDDJugadores():
    incluirPartida('Alan Turing', 'Me llamo Alan y me gusta mucho MINECRAFT y AMONGUS', 'amongus', 12.5)
    incluirPartida('Mikhail Tal', 'Soy Mikhail y suelo jugara a MINECRAFT', 'minecraft', 20.3)
    incluirPartida('Mikhail Tal', 'Soy Mikhail y suelo jugara a MINECRAFT', 'minecraft', 22.3)
    incluirPartida('Mikhail Tal', 'Soy Mikhail y suelo jugara a MINECRAFT', 'amongus', 22.3)


def main():
    # Añadiendo jugadores al diccionario - 2 puntos
    creaBBDDJugadores()

    # Juegos más popular - 3 puntos
    print(f"El juego más popular es {obtenerRankingJuegos()}")

    # Hastags - 2 puntos
    crearHashtags()

    # Ranking de jugadores - 3 puntos
    print(f"Los mejores jugadores de MINECRAFT son {obtenerRankingJugadores('minecraft', 3)}")

    # ¿Ha jugado alguna vez al juego? - 2 puntos
    print(
        f"¿Ha jugado Mikhail Tal al MINECRAFT alguna vez? {validarPartidaJugador('Mikhail Tal', 'minecraft')}")  # True
    print(f"¿Ha jugado Mikhail Tal al TETO alguna vez? {validarPartidaJugador('Mikhail Tal', 'teto')}")  # False
    print(
        f"¿Ha jugado Mikhail Tato al MINECRAFT alguna vez? {validarPartidaJugador('Mikhail Tato', 'minecraft')}")  # False


if __name__ == '__main__':
    main()
