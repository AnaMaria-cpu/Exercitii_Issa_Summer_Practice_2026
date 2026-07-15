# 9. Write a function that returns the largest prime number from a string
# given as a parameter or -1 if the character string contains no prime number.
# Ex: input: 'ahsfaisd35biaishai23isisvdshcbsi271cidsbfsd97sidsda'; output: 271
def este_prim(numar):
    if numar < 2:
        return False

    for divizor in range(2, numar):
        if numar % divizor == 0:
            return False

    return True


def cel_mai_mare_prim(text):
    numere = []
    numar_curent = ""

    for caracter in text:
        if caracter.isdigit():
            numar_curent = numar_curent + caracter
        else:
            if numar_curent != "":
                numere.append(int(numar_curent))
                numar_curent = ""

    if numar_curent != "":
        numere.append(int(numar_curent))

    rezultat = -1

    for numar in numere:
        if este_prim(numar) and numar > rezultat:
            rezultat = numar

    return rezultat


text = "ahsfaisd35biaishai23isisvdshcbsi271cidsbfsd97sidsda"
print(cel_mai_mare_prim(text))
