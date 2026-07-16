# Sa se scrie o functie care primeste un numar variabil de seturi si
# returneaza un dictionar cu urmatoarele operatii dintre toate seturile doua cate doua:
# reuniune, intersectie, a-b, b-a.
# Cheia va avea urmatoarea forma: "a op b", unde a si b sunt doua seturi, iar op este operatorul aplicat: |, &, -.
# Valoarea va fi numarul de elemente din rezultatul operatiei.
# Ex: {1,2}, {2, 3} =>
# {
#    "{1, 2} | {2, 3}": 3,
#    "{1, 2} & {2, 3}": 1,
#    "{1, 2} - {2, 3}": 1,
#    ...
# }


def operations_between_sets(*sets):
    result = {}

    for i in range(len(sets)):
        for j in range(i + 1, len(sets)):
            first_set = sets[i]
            second_set = sets[j]

            union_key = (
                str(first_set)
                + " | "
                + str(second_set)
            )

            intersection_key = (
                str(first_set)
                + " & "
                + str(second_set)
            )

            first_difference_key = (
                str(first_set)
                + " - "
                + str(second_set)
            )

            second_difference_key = (
                str(second_set)
                + " - "
                + str(first_set)
            )

            result[union_key] = len(
                first_set | second_set
            )

            result[intersection_key] = len(
                first_set & second_set
            )

            result[first_difference_key] = len(
                first_set - second_set
            )

            result[second_difference_key] = len(
                second_set - first_set
            )

    return result

answer = operations_between_sets(
    {1, 2},
    {2, 3},

)

for key in answer:
    print(key, ":", answer[key])