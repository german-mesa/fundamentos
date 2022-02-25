
def count_vowels(word):
    word = word.lower()

    vowels_count = {}

    for vowel in 'aeiou':
        vowels_count[vowel] = word.count(vowel)

    counts = sum(vowels_count.values())
    return counts


def main():
    frase = 'Ahora el que no esta mal informado es porque no quiere'

   # Convierte la frase en palabras
    # CODE HERE -->
    palabras = frase.split()
    # CODE HERE <-- 
    print(f"La lista de palabras es {palabras}")

    # Ordena lista de palabras
    # CODE HERE -->
    palabras.sort()
    # CODE HERE <-- 
    print(f"La lista de palabras ordenada {palabras}")

    # Ordena lista de palabras por su longitud
    # CODE HERE -->
    palabras.sort(key=len)    
    # CODE HERE <-- 
    print(f"La lista de palabras ordenada por longitud {palabras}")

    # Ordena lista de palabras por número de vocales
    # CODE HERE -->
    palabras.sort(key=lambda x: count_vowels(x))
    # CODE HERE <-- 
    print(f"La lista de palabras ordenada por número de vocales {palabras}")

    # Convierte la lista en minúsculas y ordena
    # CODE HERE -->
    palabras_minusculas = [x.lower() for x in palabras]
    palabras_minusculas.sort()    
    # CODE HERE <-- 
    print(f"La lista de palabras en minúsculas ordenada {palabras}")

if __name__ == '__main__':
    main()