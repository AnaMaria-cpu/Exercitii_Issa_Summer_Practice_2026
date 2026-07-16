# Sa se scrie o functie care primeste ca parametru un set si
# returneaza un tuplu (a, b),
# a reprezentand numarul de elemente unice din set
# iar b reprezentand numarul de elemente duplicate din set.

def count_unique_and_duplicates(values):
    appearances = {}

    for value in values:
        if value in appearances:
            appearances[value] = appearances[value] + 1
        else:
            appearances[value] = 1

    unique_elements = 0
    duplicate_elements = 0

    for value in appearances:
        if appearances[value] == 1:
            unique_elements = unique_elements + 1
        else:
            duplicate_elements = duplicate_elements + 1

    return unique_elements, duplicate_elements


numbers = [1, 2, 2, 3, 3, 3, 4, 7]

print(count_unique_and_duplicates(numbers))
