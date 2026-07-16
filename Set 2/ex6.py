# 6.	Sa se scrie o functie care primeste ca parametru un numar variabil de liste si un numar intreg x.
# Sa se returneze o lista care sa contina elementele care apar de exact x ori in listele primite.
# Exemplu: pentru listele [1,2,3], [2,3,4], [4,5,6], [7, 1, "test"] si x = 2 se va returna
# [1, 2, 3, 4]
# 1 se afla in lista 1 si 4,
# 2 se afla in lista 1 si 2,
# 3 se afla in listele 1 si 2,
# 4 se afla in listele 2 si 3

def nr_repetat_x_ori(x, *liste):
    numbers = []
    for lista_curenta in liste:
        for element in lista_curenta:
            if element not in numbers:
                numbers.append(element)
    result = []
    for element in numbers:
        number_of_lists = 0
        for lista_curenta in liste:
            if element in lista_curenta:
                number_of_lists = number_of_lists + 1
        if number_of_lists == x:
            result.append(element)
    return result
print(
    nr_repetat_x_ori(
        2,
        [1,2,3],
        [2,3,4],
        [4,5,6],
        [7,1,"test"]
    )
)
