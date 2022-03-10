

def cuantos_candidatos(lista_jugadores):
    resultado = 0
    
    for jugador in lista_jugadores:
        if jugador.get('goles') > 20 and jugador.get('posicion') == 'delantero':
            resultado += 1

    return resultado


def cuantos_candidatos_recursiva(lista_jugadores):
    if len(lista_jugadores) == 0:
        resultado = 0

    else:
        jugador = lista_jugadores[0]

        if jugador.get('goles') > 20 and jugador.get('posicion') == 'delantero':
            resultado = 1 + cuantos_candidatos_recursiva(lista_jugadores[1:])
        else:
            resultado = cuantos_candidatos_recursiva(lista_jugadores[1:])

    return resultado


def equipos_con_candidatos(lista_jugadores):
    # Equipos con candidatos
    equipos = {}

    for jugador in lista_jugadores:
        if jugador.get('goles') > 20 and jugador.get('posicion') == 'delantero':
            if jugador.get('club') in equipos.keys():
                equipos[jugador.get('club')] += 1
            else:
                equipos[jugador.get('club')] = 1

    # Ordenar un diccionario por valor
    equipos_ordenados = dict(sorted(equipos.items(), key = lambda x: x[1], reverse = True))

    return equipos_ordenados


def main():
    # Añadir todos los jugadores en una lista
    jugadores = []

    jugador = {'nombre':'Messi', 'goles':25,'posicion':'delantero','club': 'FCBarcelona'}
    jugadores.append(jugador)
    jugador = {'nombre':'Suarez', 'goles':30,'posicion':'delantero','club' :'FCBarcelona'}
    jugadores.append(jugador)
    jugador = {'nombre':'Benzema', 'goles':27,'posicion':'delantero','club':'RMadrid'}
    jugadores.append(jugador)
    jugador = {'nombre':'Rodrygo', 'goles':31,'posicion':'delantero','club':'RMadrid'}
    jugadores.append(jugador)
    jugador = {'nombre':'Bale', 'goles':25,'posicion':'delantero','club':'RMadrid'}
    jugadores.append(jugador)
    jugador = {'nombre':'Morata', 'goles':22,'posicion':'delantero','club' :'ATMAdrid'}
    jugadores.append(jugador)

    # jugadores candidatos
    print(f'Hay {cuantos_candidatos(jugadores)} candidatos')
    print(f'Hay {cuantos_candidatos_recursiva(jugadores)} candidatos (recursiva)')

    # equipos con algún candidato
    print(f'Ranking de equipos con candidatos - {equipos_con_candidatos(jugadores)}')


if __name__ == '__main__':
    main()
