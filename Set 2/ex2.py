# 2.	Sa se scrie o functie care primeste o lista de numere si
# returneaza o lista cu numerele prime care se gasesc in ea
def is_prime(number):
    if number < 2:
        return False

    for divisor in range(2, number):
        if number % divisor == 0:
            return False

    return True
def scoate_nr_prime(*numere):
    lista_nr_prime = []
    for item in numere:
        if is_prime(item):
            lista_nr_prime.append(item)
    return lista_nr_prime

print(scoate_nr_prime(5, 1))
print(scoate_nr_prime(5, 3,26,89, 113))
