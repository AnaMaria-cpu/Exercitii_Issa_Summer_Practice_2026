# 1.	Sa se scrie o functie care sa returneze o lista cu primele n numere din sirul lui Fibonacci.
def sir_fibonacci(n):
    lista_f = []
    if n <= 0:
        return lista_f
    lista_f.append(0)

    if n == 1:
        return lista_f
    lista_f.append(1)

    while len(lista_f) < n:
        next_number = lista_f[-1] + lista_f[-2]
        lista_f.append(next_number)
    return lista_f


print(sir_fibonacci(10))
#->[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]