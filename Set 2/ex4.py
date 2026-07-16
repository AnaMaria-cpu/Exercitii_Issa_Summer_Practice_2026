# 4.	Sa se scrie o functie care primeste ca parametri doua liste a si b si returneaza:
# a intersectat cu b, a reunit cu b, a - b, b – a fara a folosi set-uri.
# a=[1 2 3]
# b=[5 2 6]

# a intersect b = [2]
# a reunit cu b = [1 2 3 5 6]
# a-b = [1 3]
# b-a=[5 6]
def list_operations(a, b):
    intersection = []
    union = []
    difference_a_b = []
    difference_b_a = []

    for element in a:
        if element in b and element not in intersection:
            intersection.append(element)

    for element in a:
        if element not in union:
            union.append(element)

    for element in b:
        if element not in union:
            union.append(element)

    for element in a:
        if element not in b and element not in difference_a_b:
            difference_a_b.append(element)

    for element in b:
        if element not in a and element not in difference_b_a:
            difference_b_a.append(element)

    return intersection, union, difference_a_b, difference_b_a


print(list_operations([1, 2, 3, 3], [3, 4, 5]))
