# 1. Sa se scrie o functie care primeste ca parametri doua liste a si b si
# returneaza un tuplu de seturi care sa contina: (a intersectat cu b, a reunit cu b, a - b, b - a)
def set_operations(a, b):
    set_a = set(a)
    set_b = set(b)

    intersection = set_a & set_b
    union = set_a | set_b
    difference_a_b = set_a - set_b
    difference_b_a = set_b - set_a

    return intersection, union, difference_a_b, difference_b_a


print(set_operations([1, 2, 3], [3, 4, 5]))