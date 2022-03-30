juegos = [
    ("amongus", 12.5),
    ("minecraft", 84.2),
    ("minecraft", 28.2),
    ("supermario odissey", 45.5),
    ("minecraft", 13.2),
]


def get_tiempo(juego):
    return juego[1]


def get_popularity(numero_valores=1):
    ranking = get_ranking()

    resultado = []

    for index, item in enumerate(ranking.items()):
        if index >= numero_valores:
            break

        resultado.append(item)

    return resultado


def get_ranking():
    # Compongo un diccionario acumulando las partidas
    ranking = {}

    for partida in juegos:
        if partida[0] in ranking:  # Como esta en el diccionario le añado uno mas
            ranking[partida[0]] += 1
        else:  # No esta en el diccionario
            ranking[partida[0]] = 1

    # Ordenar un diccionario por valor
    sorted_ranking = dict(sorted(ranking.items(), key=lambda x: x[1], reverse=True))

    return sorted_ranking


def main():
    # Añadir un registro a una lista
    juegos.append(("supermario odissey", 12.3))

    # Añadir varios registros a una lista
    juegos.extend([("portal2", 45.0), ("amongus", 10.2)])

    # Ordenar por clave
    sorted_juegos = sorted(juegos)
    print(f"Juegos ordenados por nombre - {sorted_juegos}")

    sorted_juegos = sorted(juegos, key=get_tiempo)
    print(f"Juegos ordenados por duración - {sorted_juegos}")

    # Encontrar max y min de una lista de tuples - elegante
    print(f"\nJuego con mayor duración - {max(juegos,key=lambda item:item[1])}")
    print(f"\nJuego con menor duración - {min(juegos,key=lambda item:item[1])}")

    # Encontrar juego más popular - función
    print(f"\nRanking de juegos (función) - {get_ranking()}")
    print(f"\nJuego más popular (función) - {get_popularity()}")

    # Encontrar 3 juegos más populares - librería
    print(f"\nJuego más popular (función) - {get_popularity(3)}")


if __name__ == "__main__":
    main()
