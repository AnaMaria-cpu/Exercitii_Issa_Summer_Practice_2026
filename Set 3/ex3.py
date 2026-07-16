# Sa se compare doua dictionare fara a folosi operatorul "==" sau "!=" pentru altceva decat tipuri primitive (int, float, str)
# si sa se returneze un tuplu de liste de diferente astfel:
# (cheile_comune_dar_cu_valori_diferite, cheile_care_se_gasesc_doar_in_primul_dict,
# cheile_care_se_gasesc_doar_in_al_doilea_dict).
# (Atentie, dictionarele trebuiesc parcurse recursiv deoarece la randul lor pot contine alte containere, cum ar fi dictionare, liste, set-uri, etc.)


def values_are_equal(first_value, second_value):
    if type(first_value) != type(second_value):
        return False

    if isinstance(first_value, (int, float, str, bool)):
        return first_value == second_value

    if isinstance(first_value, dict):
        if len(first_value) != len(second_value):
            return False

        for key in first_value:
            if key not in second_value:
                return False

            if not values_are_equal(first_value[key], second_value[key]):
                return False

        return True

    if isinstance(first_value, (list, tuple)):
        if len(first_value) != len(second_value):
            return False

        for i in range(len(first_value)):
            if not values_are_equal(first_value[i], second_value[i]):
                return False

        return True

    if isinstance(first_value, set):
        if len(first_value) != len(second_value):
            return False

        for element in first_value:
            if element not in second_value:
                return False

        return True

    return False


def compare_dictionaries(first_dictionary, second_dictionary):
    different_values = []
    only_in_first = []
    only_in_second = []

    for key in first_dictionary:
        if key not in second_dictionary:
            only_in_first.append(key)
        else:
            first_value = first_dictionary[key]
            second_value = second_dictionary[key]

            if not values_are_equal(first_value, second_value):
                different_values.append(key)

    for key in second_dictionary:
        if key not in first_dictionary:
            only_in_second.append(key)

    return different_values, only_in_first, only_in_second


dictionary_1 = {
    "name": "Ana",
    "age": 21,
    "grades": [9, 10],
    "address": {"city": "Iasi", "zip": 700000},
    "extra": "value"
}

dictionary_2 = {
    "name": "Maria",
    "age": 24,
    "grades": [9, 8],
    "address": {"city": "Iasi", "zip": 700001},
    "country": "Romania"
}

print(compare_dictionaries(dictionary_1, dictionary_2))