# 1*. In cazul sirului Fibonacci fiecare termen este suma precedentilor 2.
# Sa se scrie o functie care ia ca parametru 2 numere intregi, num_terms, n.
# Num_terms va indica cati termeni vor fi calculati din urmatorul sir.
# Sirul este asemanator Fibonacci cu mentiunea ca fiecare termen este suma ultimilor n termeni.
# Sirul initial este format din n-1 0-uri si un 1. (e.g. n=5 sirul initial este 0 0 0 0 1)

def sir_gen_fib(num_terms, n):
    sir = []
    for i in range(n - 1):
        sir.append(0)
    sir.append(1)
    while len(sir) < num_terms:
        last_numbers = sir[-n:]
        next_number = sum(last_numbers)
        sir.append(next_number)
    return sir


print(sir_gen_fib(10, 3))
# [0, 0, 1, 1, 2, 4, 7, 13, 24, 44] ptr n=3

print(sir_gen_fib(10, 4))
# [0, 0, 0, 1, 1, 2, 4, 8, 15, 29] ptr n=4
