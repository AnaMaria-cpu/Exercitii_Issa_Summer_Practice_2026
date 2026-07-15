# 3. Scrieti o functie care returneaza numarul de cuvinte care exista intr-un string.
# Cuvintele sunt separate de spatii, si/sau semne de punctuatie (, ;, ? ! . )
# Intre 2 cuvinte pot aparea in orice combinatie spatii si semne de punctuatie

def nr_words(text: str):
    semne=[' ', ',', '?', '!','.']
    for semn in semne:
        text = text.replace(semn, " ")

    words = text.split()
    return len(words)
print(nr_words('hello..world'))
