
empleados = {
    'Alan Turing': { 
        'edad': 25, 
        'salario': 1000 
    }
}

def edad_maxima():
    maximo = 0

    for _ , item in enumerate(empleados):
        if empleados[item]['edad'] > maximo:
            maximo = empleados[item]['edad']

    return maximo

def contar_edad():
    grupo = {}

    for _ , item in enumerate(empleados):
        if empleados[item]['edad'] in grupo:
            grupo[empleados[item]['edad']] +=1
        else:
            grupo[empleados[item]['edad']] =1

    return grupo

def ordenar_edad(reverse=False):
    return {k: v for k, v in sorted(empleados.items(), key=lambda item: item[1]['salario'], reverse=reverse)}


def main():
    # Vaciar el diccionario
    empleados.clear()

    # Añadir un registro a un diccionario
    empleados.update({'Mikhail Tal':{'edad': 40, 'salario': 17000}})
    empleados.update({'John Hopkins':{'edad': 18, 'salario': 1000}})
    empleados.update({'Sharon Lin':{'edad': 30, 'salario': 8000}})
    empleados.update({'Pichi Cual':{'edad': 40, 'salario': 15000}})

    # Sobreescribo un registro de un diccionario
    empleados.update({'John Hopkins':{'edad': 30}})

    # Actualizar edad y salario
    empleados['John Hopkins']['salario'] = 2000

    # Eliminar un registro de un diccionario 
    empleados.pop('Sharon Lin', None)
 
    # Loop sobre un diccionario
    for index, item in empleados.items():
        print(f'{index} - {item}')

    for index, item in enumerate(empleados):
        print(f'{index} - {item}')

    for item in empleados.items():
        print(f'{item}')

    # Algunas cosas que pueden hacerse con loops
    print(f'La edad máxima de la plantilla es {edad_maxima()}')
    print(f'Los grupos de edad son {contar_edad()}')

    # Cosas que pueden hacerse con lambdas
    print(f'El diccionario puede ordenarse por edad {ordenar_edad()}')
    print(f'El diccionario puede ordenarse por edad inversa {ordenar_edad(reverse=True)}')

if __name__ == '__main__':
    main()