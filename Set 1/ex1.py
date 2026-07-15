# 1. Find the largest common divisor of multiple numbers.
# Define a function  with variable number of parameters to resolve this.

def cmmdc(a, b):
    """
    Return the greatest common divisor of two numbers.
    """
    while b != 0:
        rest = a % b
        a = b
        b = rest

    return a


def cmmdc_mai_multe(*numere):
    rezultat = numere[0]

    for numar in numere[1:]:
        rezultat = cmmdc(rezultat, numar)

    return rezultat



print(cmmdc_mai_multe(24, 48, 36)) #->12