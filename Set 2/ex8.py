# 8.	Sa se scrie o functie care primeste un numar variabil de liste si returneaza o lista de tuple astfel:
# primul tuplu sa contina primele elemente din liste, al doilea element sa contina elementele de pe pozitia 2 din liste, etc.
# Ex: pentru listele [1,2,3], [5,6,7], ["a", "b", "c"] se va returna: [(1,5,"a"), (2,6,"b"), (3,7,"c")].

# Observatie:
# In cazul in care listele primite ca input nu au acelasi numar de elemente,
# elementele lipsa vor fi inlocuite cu None pentru a putea fi generate max([len(x) for x in input_lists]) tuple.
#
# Pe scurt: implementati zip! (fara sa folositi zip) 😊

def my_zip(*lists):
    result = []
    maximum_length = 0

    for current_list in lists:
        if len(current_list) > maximum_length:
            maximum_length = len(current_list)

    for position in range(maximum_length):
        current_tuple = []

        for current_list in lists:
            if position < len(current_list):
                current_tuple.append(current_list[position])
            else:
                current_tuple.append(None)

        result.append(tuple(current_tuple))

    return result


print(my_zip([1, 2, 3], [5, 6, 7 ], ["a", "b", "c"]))