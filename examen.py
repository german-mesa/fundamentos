# Partidas por jugador
def obtenerPartidasJugador(bbdd, jugador: str):
    return bbdd[jugador].get('partidas')


# Todas las partidas jugadas por todos los jugadores
def obtenerPartidas(bbdd):
    partidas = []

    for jugador in bbdd:
        partidas.extend(obtenerPartidasJugador(bbdd, jugador))

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
def validarPartidaJugador(bbdd, jugador: str, juego: str) -> bool:
    if jugador in bbdd:
        return existePartida(juego, obtenerPartidasJugador(bbdd, jugador))
    else:
        return False


# ¿Cuál es el juego más popular?
def obtenerRankingJuegos(bbdd):
    # Cuento los juegos en un diccionario
    ranking = {}

    for partida in obtenerPartidas(bbdd):
        if partida[0] in ranking:  # Como esta en la coleccion le añado uno mas
            ranking[partida[0]] += 1
        else:  # No esta en la coleccion
            ranking[partida[0]] = 1

    # Lo convierto a lista para ordenar de mayor a menor
    ranking = list(ranking.items())
    ranking.sort(key=lambda x: x[1], reverse=True)

    return ranking[0]


# Obtiene el ranking de los `m` mejores jugadores del juego
def obtenerRankingJugadores(bbdd, juego: str, m: int) -> list:
    ranking = {}

    for jugador in bbdd:
        for partida in obtenerPartidasJugador(bbdd, jugador):
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
        m = len(ranking)

    return ranking[:m]


# Añadir hastags en la descripción de cada jugador
def crearHashtags(bbdd):
    for jugador in bbdd:
        descripcion = ""

        for word in str.split(bbdd[jugador]['descripcion']):
            if str.isupper(word):
                descripcion += "#"
            descripcion += word + " "

        bbdd[jugador]['descripcion'] = descripcion


# Añadir partida en la BBDD
def incluirPartida(bbdd, jugador: str, descripcion: str, partida: str, tiempo: float):
    if jugador in bbdd:  # Update existing player
        bbdd[jugador]['descripcion'] = descripcion
        bbdd[jugador]['partidas'].append((partida, tiempo))

    else:  # Add a new player
        bbdd[jugador] = {'descripcion': descripcion, 'partidas': [(partida, tiempo)]}


# Incluir partidas en la BBDD
def creaBBDDJugadores(bbdd):
    incluirPartida(bbdd, "juan", "Me llamo juan y me gusta MINECRAFT y AMONGUS", "portal2", 45.0)
    incluirPartida(bbdd, "juan", "Me llamo Juan y me gusta mucho MINECRAFT y AMONGUS", "amongus", 10.2)
    incluirPartida(bbdd, "juan", "Me llamo Juan y me gusta mucho MINECRAFT y AMONGUS", "amongus", 100.2)
    incluirPartida(bbdd, "pepe", "Soy pepe y mi juego preferido es MINECRAFT", "amongus", 12.5)
    incluirPartida(bbdd, "ana", "Soy ana y suelo jugara a MINECRAFT", "minecraft", 20.3)
    incluirPartida(bbdd, "ana", "Soy ana y suelo jugara a MINECRAFT", "minecraft", 22.3)
    incluirPartida(bbdd, "ana", "Soy ana y suelo jugara a MINECRAFT", "amongus", 22.3)
    return bbdd


def main():
    # Añadiendo jugadores al diccionario - 2 puntos
    jugadores = creaBBDDJugadores({})

    # Juegos más popular - 3 puntos
    print(f"El juego más popular es {obtenerRankingJuegos(jugadores)}")

    # Hastags - 2 puntos
    crearHashtags(jugadores)

    # Ranking de jugadores - 3 puntos
    print(f"Los mejores jugadores de AMONGUS son {obtenerRankingJugadores(jugadores, 'amongus', 3)}")
    print(f"Los mejores jugadores de AMONGUS son {obtenerRankingJugadores(jugadores, 'amongus', 2)}")

    # ¿Ha jugado alguna vez al juego? - 2 puntos
    print(f"¿Ha jugado Juan al amongus alguna vez? {validarPartidaJugador(jugadores, 'juan', 'amongus')}")
    print(f"¿Ha jugado Juan al Garrys Mod alguna vez? {validarPartidaJugador(jugadores, 'juan', 'Garrys Mod')}")
    print(f"¿Ha jugado antonio al rdd alguna vez? {validarPartidaJugador(jugadores, 'antonio', 'rdd')}")


if __name__ == '__main__':
    main()
