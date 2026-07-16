# 7. Sa se scrie o functie care primeste ca parametri
# - un numar x default egal cu 1,
# - un numar variabil de siruri de caractere si
# - un flag boolean setat default pe True.
# Pentru fiecare sir de caractere, sa se genereze o lista care sa contina caracterele care au
# codul ASCII divizibil cu x in caz ca flag-ul este setat pe True,
# in caz contrar sa contina caracterele care au codul ASCII nedivizibil cu x.

# Exemplu:
# x=2, "test", "hello", "lab002", flag=False
# va returna (["e", "s"], ["e", "o"], ["a"]).
# Atentie:
# functia trebuie sa returneze un numar variabil de liste care sa corespunda cu numarul de siruri de caractere primite ca input.

def filter_ascii(*strings, x=1, flag=True):
    result = []

    for text in strings:
        characters = []

        for character in text:
            ascii_code = ord(character)

            if flag == True and ascii_code % x == 0:
                characters.append(character)
            elif flag == False and ascii_code % x != 0:
                characters.append(character)

        result.append(characters)

    return tuple(result)


print(filter_ascii("test", "hello", "lab002", x=2, flag=False))