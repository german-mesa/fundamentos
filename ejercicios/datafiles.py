import os
import time

def csv_reader_generator(file_name):
    for row in open(file_name, "r"):
        yield row


def csv_reader_tradicional(file_name):
    with open(file_name) as f:
        resultado = f.read().split("\n")
        return resultado


def main():
    nombre_fichero = os.path.join(os.getcwd(), 'data', 'big_file_indeed.csv')
    
    # Método tradicional
    start_time = time.time()
    contador = 0

    for fila in csv_reader_tradicional(nombre_fichero):
        contador += 1
    print(f"El número de filas es {contador-1} -  {time.time() - start_time}")

    # Usando generadores
    start_time = time.time()
    contador = 0

    for fila in csv_reader_generator(nombre_fichero):
        contador += 1

    print(f"El número de filas es {contador} -  {time.time() - start_time}")


if __name__ == '__main__':
    main()


 # 0 = negative, 2 = neutral, 4 = positive   