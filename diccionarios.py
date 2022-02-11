# Ordenando diccionarios utilizando claves
employees = [
    {'Name': 'Alan Turing', 'age': 25, 'salary': 10000},
    {'Name': 'Sharon Lin', 'age': 30, 'salary': 8000},
    {'Name': 'John Hopkins', 'age': 18, 'salary': 1000},
    {'Name': 'Mikhail Tal', 'age': 40, 'salary': 15000},
]


# Funciones que devuelven datos del empleado
def get_name(employee):
    return employee.get('Name')


def get_age(employee):
    return employee.get('age')


def get_salary(employee):
    return employee.get('salary')


def sort_lambda():
    print("Ordeno la lista de empleados con funciones lambda", end='\n')

    # Ordenando por nombre - ascendiente
    employees.sort(key=lambda x: x.get('Name'))
    print("Ordenando por nombre - ascendiente")
    print(employees, end='\n\n')

    # Ordenando por edad - ascendiente
    employees.sort(key=lambda x: x.get('age'))
    print("Ordenando por edad - ascendiente")
    print(employees, end='\n\n')

    # Ordenando por salario - descendiente
    employees.sort(key=lambda x: x.get('salary'), reverse=True)
    print("Ordenando por salario - descendiente")
    print(employees, end='\n\n')


def sort_functions():
    print("Ordeno la lista de empleados con funciones auxiliares", end='\n')

    # Ordenando por nombre - ascendiente
    employees.sort(key=get_name)
    print("Ordenando por nombre - ascendiente")
    print(employees, end='\n\n')

    # Ordenando por edad - ascendiente
    employees.sort(key=get_age)
    print("Ordenando por edad - ascendiente")
    print(employees, end='\n\n')

    # Ordenando por salario - descendiente
    employees.sort(key=get_salary, reverse=True)
    print("Ordenando por salario - descendiente")
    print(employees, end='\n\n')


def main():
    sort_functions()

    sort_lambda()


if __name__ == '__main__':
    main()
