
empleados = {
    'Alan Turing': { 
        'age': 25, 
        'salary': 1000 
    }
}


def contratar_empleado(empleado):
    empleados.update(empleado)

def despedir_empleado(empleado):
    empleados.pop(empleado, None) 

def main():
    # Contrato unos cuantos empleado
    contratar_empleado({'John Hopkins':{'age': 18, 'salary': 1000}})
    contratar_empleado({'Sharon Lin':{'age': 30, 'salary': 8000}})
    contratar_empleado({'Mikhail Tal':{'age': 40, 'salary': 15000}})
    print(empleados)

    # Sobreescribo un empleado
    contratar_empleado({'John Hopkins':{'age': 20, 'salary': 1000}})
    print(empleados)

    # Despedir un empleado
    despedir_empleado('Sharon Lin')
    print(empleados)

if __name__ == '__main__':
    main()