


empleados = {
    "Alan Turing": { 
        "age": 25, 
        "salary": 1000 
    }
}


def contratar_empleado(empleado):
    empleados[empleado.keys()] = ''
    # empleados['John Hopkins'] = empleado
    pass


def main():
    contratar_empleado({'John Hopkins':{'age': 18, 'salary': 1000}})
    print(empleados)

if __name__ == '__main__':
    main()