# Fie functia validate_dict care primeste ca parametru
# un set de tuple care reprezinta reguli de validare pentru un dictionar si
# un dictionar cu chei de tipul string si
#                  valori tot de tipul string.

# O regula este definita astfel: (cheie, "prefix", "middle", "sufix").
# O valoare este considerata valida daca
# - incepe cu "prefix",
# - "middle" se gaseste in interiorul valorii (nu la inceput sau sfarsit) si
# - se sfarsete cu "sufix".

# Functia va returna True daca dictionarul dat ca parametru respecta toate regulile si
# daca nu apar in dictionar decat chei care sunt mentionate si in reguli, False in caz contrar.

# Exemplu:
# regulile [("key1", "", "inside", ""), ("key2", "start", "middle", "winter")] si
# dictionarul {"key2": "starting the engine in the middle of the winter",
# "key1": "come inside, it's too cold outside", "key3": "this is not valid"}
# => False deoarece desi regulile sunt respectate pentru "key1" si "key2", apare "key3" care nu apare in reguli.
#


def validate_dict(rules, dictionary):
    rule_keys = []

    for rule in rules:
        rule_keys.append(rule[0])

    for key in dictionary:
        if key not in rule_keys:
            return False

    for rule in rules:
        key = rule[0]
        prefix = rule[1]
        middle = rule[2]
        suffix = rule[3]

        if key not in dictionary:
            return False

        value = dictionary[key]

        if not value.startswith(prefix):
            return False

        if not value.endswith(suffix):
            return False

        if middle != "" and middle not in value[1:-1]:
            return False

    return True


rules = {
    ("key1", "", "inside", ""),
    ("key2", "start", "middle", "winter")
}

dictionary = {
    "key2": "starting the engine in the middle of the winter",
    "key1": "come inside, it is too cold outside",
    "key3": "this is not valid"
}

print(validate_dict(rules, dictionary))