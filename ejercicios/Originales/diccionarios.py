
empleados = {
    'Alan Turing': { 
        'edad': 25, 
        'salario': 1000 
    }
}

def contar_edad():
    grupo = {}

    for _ , item in enumerate(empleados):
        if empleados[item]['edad'] in grupo:
            grupo[empleados[item]['edad']] +=1
        else:
            grupo[empleados[item]['edad']] =1

    return grupo

def edad_maxima():
    empleados_sorted = sorted(empleados, key=get_edad, reverse=True)
    return empleados[empleados_sorted[0]]['edad']

def salario_maximo():
    empleados_sorted = sorted(empleados, key=get_salario, reverse=True)
    return empleados[empleados_sorted[0]]['salario']

def get_edad(empleado):
    return empleados[empleado]['edad']

def get_salario(empleado):
    return empleados[empleado]['salario']

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
    empleados['John Hopkins']['salario'] = 20000

    # Eliminar un registro de un diccionario 
    empleados.pop('Sharon Lin', None)
 
    print(f'\nDiccionario tras meter y modificar datos:\n {empleados}')

    # Ordenar por clave
    empleados_sorted = sorted(empleados)
    print(f'\nOrdenando diccionario por clave:\n {empleados_sorted}')

    empleados_sorted = sorted(empleados, reverse=True)
    print(f'\nOrdenando diccionario inversamente por clave:\n {empleados_sorted}')

    # Algunas cosas que pueden hacerse con ordenaciones
    print(f'\nAlgunas cosas que pueden hacerse con ordenaciones')
    print(f'La edad máxima de la plantilla es {edad_maxima()}')
    print(f'El salario máximo de la plantilla es {salario_maximo()}')

    # Loop sobre un diccionario
    print(f'\nLoop en diccionario utilizando enumerate()')
    for index, item in enumerate(empleados):
        print(f'{index} - {item}')

    print(f'\nLoop en diccionario utilizando items()')
    for index, item in empleados.items():
        print(f'{index} - {item}')

    print(f'\nLoop en diccionario utilizando items()')
    for item in empleados.items():
        print(f'{item}')

    # Algunas cosas que pueden hacerse con loops
    print(f'\nAlgunas cosas que pueden hacerse con loops')
    print(f'Los grupos de edad son {contar_edad()}')


if __name__ == '__main__':
    main()